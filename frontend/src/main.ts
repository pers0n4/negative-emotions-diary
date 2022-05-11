import { Quasar } from "quasar";
import quasarIconSet from "quasar/icon-set/svg-mdi-v6";
import quasarLang from "quasar/lang/ko-KR";
import { createApp } from "vue";

// Import icon libraries
import "@quasar/extras/mdi-v6/mdi-v6.css";

// Import Quasar css
import "quasar/src/css/index.sass";

import App from "./App.vue";
import axios from "./plugins/axios";
import router from "./router";
import store from "./store";

createApp(App)
  .use(router)
  .use(store)
  .use(axios)
  .use(Quasar, {
    lang: quasarLang,
    iconSet: quasarIconSet,
  })
  .mount("#app");
