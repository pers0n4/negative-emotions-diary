import { createRouter, createWebHistory } from "vue-router";
import store from "./store";

const routes = [
  {
    path: "/",
    redirect: { name: "SignIn" },
  },
  {
    path: "/signin",
    name: "SignIn",
    component: () => import("./pages/SignIn.vue"),
    meta: { guest: true },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("./pages/SignUp.vue"),
    meta: { guest: true },
  },
  {
    path: "/diaries/write",
    name: "DiaryWrite",
    component: () => import("./pages/DiaryWrite.vue"),
    meta: { auth: true },
  },
  {
    path: "/diaries",
    name: "DiaryRead",
    component: () => import("./pages/DiaryRead.vue"),
    meta: { auth: true },
  },
  {
    path: "/graph",
    name: "Graph",
    component: () => import("./pages/Graph.vue"),
  },
  {
    path: "/affect",
    name: "Affect",
    component: () => import("./pages/Affect.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: import("./pages/NotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ top: 0 }),
});

router.beforeEach(async (to, _from, next) => {
  if (to.meta.auth && !store.getters["auth/isAuthenticated"]) {
    next({ name: "SignIn" });
    return;
  } else if (to.meta.guest && store.getters["auth/isAuthenticated"]) {
    next({ name: "DiaryRead" });
    return;
  }
  next();
});

export default router;
