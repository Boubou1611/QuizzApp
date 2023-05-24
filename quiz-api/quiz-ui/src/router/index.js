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
      path: "/your-score",
      name: "PersonnalScore",
      component: () => import("../views/PersonnalScore.vue"),
    },
    {
      path: "/admin",
      name: "admin-panel",
      component: () => import("../views/Administration.vue"),
    },
    {
      path: "/admin-create",
      name: "admin-create",
      component: () => import("../views/CreateQuestion.vue"),
    },
    {
      path: "/admin-display",
      name: "admin-display",
      component: () => import("../views/QuestionAdminDisplay.vue"),
    },
    {
      path: "/admin-edit",
      name: "admin-edit",
      component: () => import("../views/QuestionEdit.vue"),
    },
  ],
});

export default router;
