import { Module } from "vuex";
import { axios } from "../plugins/axios";
import type { RootState } from "./index";

export interface AuthState {
  token: string | null;
}

export const auth: Module<AuthState, RootState> = {
  namespaced: true,
  state: () => ({
    token: window?.localStorage.getItem("access_token") || null,
  }),
  getters: {
    isAuthenticated(state) {
      return Boolean(state.token);
    },
  },
  mutations: {
    setToken(state, token: string) {
      state.token = token;
      window?.localStorage.setItem("access_token", token);
    },
    removeToken(state) {
      state.token = null;
      window?.localStorage.removeItem("access_token");
      delete axios.defaults.headers.common["Authorization"];
    },
  },
  actions: {
    async register(_context, { email, password }) {
      return axios.post("/users", { email, password });
    },
    async login(
      { commit },
      userData: {
        username: string;
        password: string;
      },
    ) {
      const response = await axios.post("/auth/token", userData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      commit("setToken", response.data.access_token);
      return response;
    },
    async logout({ commit }) {
      commit("removeToken");
    },
  },
};
