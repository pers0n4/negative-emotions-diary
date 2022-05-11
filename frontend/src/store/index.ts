import { createStore } from "vuex";

export interface RootState {
  token: string | null;
}

export default createStore<RootState>({
  state() {
    return {
      token: null,
    };
  },
});
