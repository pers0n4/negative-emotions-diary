import Axios from "axios";

const axios = Axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

axios.interceptors.request.use(
  (config) => {
    console.log("axios.js request : ", config);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

axios.interceptors.response.use(
  (res) => {
    console.log("axios.js response : ", res);
    return res;
  },
  (error) => {
    return Promise.reject(error);
  },
);

export default axios;
