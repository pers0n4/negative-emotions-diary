import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: { name: "SignIn" },
  },
  {
    path: "/signin",
    name: "SignIn",
    component: () => import("./pages/SignIn.vue"),
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("./pages/SignUp.vue"),
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

export default router;
