<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      this.registeredScores = await quizApiService.getQuizInfo();
      console.log(this.registeredScores);
    } catch (err) {
      console.error(err);
    }
  },
};
</script>

<template>
  <h1>Home page</h1>

  <div
    v-for="scoreEntry in this.registeredScores.data.scores"
    :key="scoreEntry.id"
  >
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>

  <!-- <router-link to="new-quiz-page">Démarrer le quiz !</router-link>-->
  <RouterLink to="/new-quiz-page">Démarrer le quiz !</RouterLink>
</template>
