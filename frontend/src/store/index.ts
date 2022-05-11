import { createStore } from "vuex";
import { axios } from "../plugins/axios";

export interface RootState {
  token: string | null;
}

export default createStore<RootState>({
  state() {
    return {
      token: null,
    };
  },
  getters: {
    token: (state) => state.token,
  },
  mutations: {
    setToken(state, token: string) {
      state.token = token;
    },
  },
  actions: {
    async signup(_context, { email, password }) {
      return axios.post("/users", { email, password });
    },
    async authenticate(
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
  },
});
