import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: { name: "main" },
  },
  {
    path: "/signin",
    name: "SignIn",
    component: () => import("./pages/SignIn.vue"),
  },
  {
    path: "/main",
    name: "main",
    component: () => import("./pages/main.vue"),
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("./pages/SignUp.vue"),
  },
  {
    path: "/wdiary",
    name: "Wdiary",
    component: () => import("./pages/Wdiary.vue"),
  },
  {
    path: "/emotions_graph",
    name: "emotions_graph",
    component: () => import("./pages/emotions_graph.vue")
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