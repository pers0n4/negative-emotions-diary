import Axios, { AxiosInstance } from "axios";
import type { Plugin } from "vue";

declare module "@vue/runtime-core" {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

export const axios = Axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

axios.interceptors.request.use(
  (config) => {
    console.log("axios.js request : ", config);
    config.headers.Authorization = `Bearer ${localStorage.getItem(
      "access_token",
    )}`;
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

export default {
  install: (app) => {
    app.config.globalProperties.$axios = axios;
  },
} as Plugin;
