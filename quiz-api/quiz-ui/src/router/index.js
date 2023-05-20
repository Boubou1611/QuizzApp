import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/admin-login",
      name: "AdministrationLogin",
      component: () => import("../views/AdministrationLogin.vue"),
    },
    {
      path: "/new-quiz-page",
      name: "NewQuizPage",
      component: () => import("../views/NewQuizPage.vue"),
    },
    {
      path: "/questions",
      name: "QuestionManager",
      component: () => import("../views/QuestionManager.vue"),
    },
    {
      path: "/your-score/:score",
      name: "PersonnalScore",
      component: () => import("../views/PersonnalScore.vue"),
    },
    {
      path: "/admin",
      name: "Administration",
      component: () => import("../views/Administration.vue"),
    },
  ],
});

export default router;
