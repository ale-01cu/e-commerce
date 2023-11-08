import axios from "axios";

const API_URL = "http://localhost:8000/";

const getProfile = () => {
  const access = JSON.parse(localStorage.getItem("access"));
  return axios
    .get(API_URL + "/api/profile/", {
      headers: {
        Authorization: "Bearer " + access,
        Accept: "application/json",
      },
    })
    .then((response) => {
      if (response.status === 200) localStorage.setItem("profile", JSON.stringify(response.data));
      return response.data;
    });
};

const ProfileService={getProfile,};

export default ProfileService