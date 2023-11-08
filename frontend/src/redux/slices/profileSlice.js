import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import ProfileService from "../../services/profile.service";
import { setMessage } from "./messageSlice";

export const getProfile = createAsyncThunk(
  "profile/getProfile",
  async (thunkAPI) => {
    try {
      const data = await ProfileService.getProfile();
      return data;
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

const profileSlice = createSlice({
  name: "profile",
  initialState: { profile: null },
  reducers: {
    removeProfile(state) {
      state.profile = null;
    },
  },

  extraReducers: (builder) => {
    builder.addCase(getProfile.fulfilled, (state, action) => {
      state.profile = action.payload;
    });
  },
});

export const { removeProfile } = profileSlice.actions;
export default profileSlice.reducer;
