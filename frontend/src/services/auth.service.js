import axios from "axios";

const API_URL = "http://localhost:8000";

const check_authenticated = () => {
  const token = JSON.parse(localStorage.getItem("access"));
  return axios.post(API_URL + "/api/auth/jwt/verify/", {
    token,
    headers: { Accept: "application/json", "Content-Type": "application/json" },
  });
};

const register = (
  first_name,
  last_name,
  email,
  password,
  re_password,
  phone_number,
  birthdate
) => {
  return axios.post(
    API_URL + "/api/auth/users/",
    {
      first_name,
      last_name,
      email,
      password,
      re_password,
      phone_number,
      birthdate,
    },
    { headers: { "Content-Type": "application/json" } }
  );
};

const getUser = () => {
  const access = JSON.parse(localStorage.getItem("access"));
  return axios
    .get(API_URL + "/api/auth/users/me/", {
      headers: {
        Authorization: "Bearer " + access,
        Accept: "application/json",
      },
    })
    .then((response) => {
      if (response.status === 200)
        localStorage.setItem("user", JSON.stringify(response.data));
      return response.data;
    });
};

const activate = (uid, token) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const body = JSON.stringify({
    uid,
    token,
  });
  return axios
    .post(API_URL + "/api/auth/users/activation/", body, config)
    .then((response) => {
      return response;
    });
};

const refresh = () => {
  const config = {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  };

  const refresh = JSON.parse(localStorage.getItem("refresh"));
  return axios
    .post(API_URL + "/api/auth/jwt/refresh/", {refresh}, config)
    .then((response) => {
      localStorage.setItem("access", JSON.stringify(response.data.access));
      return response;
    });
};

const login = (email, password) => {
  return axios
    .post(
      API_URL + "/api/auth/jwt/create/",
      {
        email,
        password,
      },
      { headers: { "Content-Type": "application/json" } }
    )
    .then((response) => {
      {
        localStorage.setItem("access", JSON.stringify(response.data.access));
        localStorage.setItem("refresh", JSON.stringify(response.data.refresh));
      }

      return response.data;
    });
};

const reset_password = (email) => {
  return axios
    .post(
      API_URL + "/api/auth/users/reset_password/",
      {
        email,
      },
      { headers: { "Content-Type": "application/json" } }
    )
    .then((response) => {
      return response;
    });
};

const reset_password_confirm = (uid, token, new_password, re_new_password) => {
  return axios
    .post(
      API_URL + "/api/auth/users/reset_password/",
      {
        uid,
        token,
        new_password,
        re_new_password,
      },
      { headers: { "Content-Type": "application/json" } }
    )
    .then((response) => {
      return response;
    });
};

const authService = {
  check_authenticated,
  register,
  login,
  getUser,
  activate,
  refresh,
  reset_password,
  reset_password_confirm,
};

export default authService;
