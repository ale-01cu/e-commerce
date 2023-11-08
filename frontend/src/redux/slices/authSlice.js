import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { setMessage } from "./messageSlice";

import AuthService from "../../services/auth.service";
import { getProfile } from "./profileSlice";

export const check_authenticated = createAsyncThunk(
  "auth/check_authenticated",
  async (_, thunkAPI) => {
    try {
      const response = await AuthService.check_authenticated();
      if (response.status === 200) {
        await thunkAPI.dispatch(getUser());
        await thunkAPI.dispatch(getProfile());
      }
      return response.data;
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      thunkAPI.dispatch(setMessage(message));
      return thunkAPI.rejectWithValue();
    }
  }
);

export const register = createAsyncThunk(
  "auth/register",
  async (
    {
      first_name,
      last_name,
      email,
      password,
      re_password,
      phone_number,
      birthdate,
    },
    thunkAPI
  ) => {
    try {
      thunkAPI.dispatch(set_auth_loading());
      const response = await AuthService.register(
        first_name,
        last_name,
        email,
        password,
        re_password,
        phone_number,
        birthdate
      );
      thunkAPI.dispatch(setMessage("Se ha creado su cuenta con exito. Revise su curreo para activarla"));
      thunkAPI.dispatch(remove_auth_loading());
      return response.data;
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      thunkAPI.dispatch(setMessage("Ocurrio un error al crear su cuenta"));
      thunkAPI.dispatch(remove_auth_loading());
      return thunkAPI.rejectWithValue();
    }
  }
);

export const getUser = createAsyncThunk("getUser", async (_, thunkAPI) => {
  try {
    const data = await AuthService.getUser();
    return data;
  } catch (err) {
    return thunkAPI.rejectWithValue(err.response.data);
  }
});

export const login = createAsyncThunk(
  "auth/login",
  async ({ loginname, password }, thunkAPI) => {
    try {
      const data = await AuthService.login(loginname, password);
      await thunkAPI.dispatch(getUser());
      await thunkAPI.dispatch(getProfile());
      return data;
    } catch (error) {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      console.log(error);
      let message;
      if (error.response.status === 401) message = "Usuario no permitido";
      else message = "Error que ni idea";
      thunkAPI.dispatch(setMessage(message));
      return thunkAPI.rejectWithValue();
    }
  }
);

export const activate = createAsyncThunk(
  "auth/activate",
  async ({ uid, token }, thunkAPI) => {
    try {
      const response = await AuthService.activate(uid, token);
      if (response.status === 204)
        thunkAPI.dispatch(setMessage("Se activó la cuenta correctamente"));
      else
        thunkAPI.dispatch(setMessage("Ocurrió un error al activar la cuenta"));
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      thunkAPI.dispatch(setMessage("Ocurrió un error al activar la cuenta"));
      return thunkAPI.rejectWithValue();
    }
  }
);

export const refresh = createAsyncThunk("auth/refresh", async (_, thunkAPI) => {
  try {
    const response = await AuthService.refresh();
    if (response.status === 401) thunkAPI.dispatch(logout);
    return response.data;
  } catch (error) {
    const message =
      (error.response && error.response.data && error.response.data.message) ||
      error.message ||
      error.toString();
    return thunkAPI.rejectWithValue();
  }
});

export const reset_password = createAsyncThunk(
  "auth/reset_password",
  async ({ email }, thunkAPI) => {
    try {
      const response = await AuthService.reset_password(email);
      if (response.status === 204)
        thunkAPI.dispatch(
          setMessage("Se ha enviado un correo para reiniciar su contraseña")
        );
      else
        thunkAPI.dispatch(
          setMessage("Ha ocurrido un error al intentar reiniciar su contraseña")
        );
      return response.data;
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      thunkAPI.dispatch(
        setMessage("Ha ocurrido un error al intentar reiniciar su contraseña")
      );
      return thunkAPI.rejectWithValue();
    }
  }
);

export const reset_password_confirm = createAsyncThunk(
  "auth/reset_password_confirm",
  async ({ uid, token, new_password, re_new_password }, thunkAPI) => {
    try {
      if (new_password != re_new_password) {
        thunkAPI.dispatch(setMessage("Las contraseñas no coinciden"));
        thunkAPI.rejectWithValue();
      }

      const response = await AuthService.reset_password_confirm(
        uid,
        token,
        new_password,
        re_new_password
      );
      if (response.status === 204)
        thunkAPI.dispatch(
          setMessage("Se ha reiniciado su contraseña con exito")
        );
      else thunkAPI.dispatch(setMessage("Error al reiniciar su contraseña"));
      return response.data;
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      thunkAPI.dispatch(
        setMessage("Ha ocurrido un error al intentar reiniciar su contraseña")
      );
      return thunkAPI.rejectWithValue();
    }
  }
);

const initialState = {
  access: localStorage.getItem("access"),
  refresh: localStorage.getItem("refresh"),
  isLoggedIn: null,
  user: null,
  loading: null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    set_auth_loading: (state) => {
      state.loading = true;
    },
    remove_auth_loading: (state) => {
      state.loading = false;
    },
    logout: (state) => {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      state.isLoggedIn = false;
      state.access = null;
      state.refresh = null;
      state.user = null;
    },
  },

  extraReducers: (builder) => {
    builder
      .addCase(login.fulfilled, (state) => {
        state.isLoggedIn = true;
        state.access = localStorage.getItem("access");
        state.refresh = localStorage.getItem("refresh");
      })
      .addCase(getUser.fulfilled, (state, action) => {
        state.user = action.payload;
      })
      .addCase(getUser.rejected, (state) => {
        state.user = null;
      })
      .addCase(refresh.fulfilled, (state) => {
        state.access = localStorage.getItem("access");
      })
      .addCase(check_authenticated.fulfilled, (state) => {
        state.isLoggedIn = true;
      })
      .addCase(check_authenticated.rejected, (state) => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        state.isLoggedIn = false;
        state.access = null;
        state.refresh = null;
      });
  },
});

export const { logout, set_auth_loading, remove_auth_loading } =
  authSlice.actions;
export default authSlice.reducer;
