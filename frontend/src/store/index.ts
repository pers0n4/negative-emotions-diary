import { createStore } from "vuex";
import { auth } from "./auth";
import type { AuthState } from "./auth";

export interface RootState {
  auth: AuthState;
}

export default createStore<RootState>({
  modules: {
    auth,
  },
});
