<template>
  <div class="score-page">
    <div class="your-score">
      <h1>Votre score est de {{ currentScore }}</h1>
    </div>

    <div class="past-rankings">
      <h2>Votre classement par rapport aux participations passées</h2>
      <ul>
        <li v-for="(score, index) in filteredScores" :key="index">
          Participation {{ index + 1 }}: {{ score.score }}
        </li>
      </ul>
    </div>

    <div class="top-scores">
      <h2>Meilleurs scores</h2>
      <ul>
        <li v-for="(score, index) in pastScores.slice(0, 5)" :key="index">
          Top {{ index + 1 }}: {{ score.playerName }} - {{ score.score }}
        </li>
      </ul>
    </div>

    <router-link to="/">Retour à la Home page</router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  data() {
    return {
      currentScore: this.$route.query.score,
      playerName: this.$route.query.name,
      pastScores: [],
    };
  },
  computed: {
    filteredScores() {
      let pastScoresPers = this.pastScores.filter(
        (score) => score.playerName === this.playerName
      );
      return pastScoresPers;
    },
  },
  async created() {
    let registeredScores = await quizApiService.getQuizInfo();
    this.pastScores = registeredScores.data.scores;
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .score-page {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
