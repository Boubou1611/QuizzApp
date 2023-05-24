<template>
  <div class="your-score">
    <div class="score-page">
      <h1>Votre score est de {{ currentScore }}</h1>
    </div>

    <div class="past-rankings">
      <h2>Votre classement par rapport aux participations passées :</h2>
      <div class="scrollable-list">
        <ul>
          <li
            v-for="(score, index) in filteredScores"
            :key="index"
            class="list-item"
          >
            Participation {{ index + 1 }}: {{ score.score }}
          </li>
        </ul>
      </div>
    </div>

    <div class="top-scores">
      <h2>Meilleurs scores :</h2>
      <div class="scrollable-list">
        <ul>
          <li
            v-for="(score, index) in pastScores.slice(0, 5)"
            :key="index"
            class="list-item"
          >
            Top {{ index + 1 }}: {{ score.playerName }} - {{ score.score }}
          </li>
        </ul>
      </div>
    </div>

    <router-link to="/" class="button">Retour à la Home page</router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      currentScore: participationStorageService.getPlayerScore(),
      playerName: participationStorageService.getPlayerName(),
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
.your-score {
  margin-top: 70px;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}

.scrollable-list {
  height: 200px;
  overflow-y: scroll;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.list-item {
  border-bottom: 1px solid white;
  padding: 10px 0;
}

.button {
  display: inline-block; /* allows for width and height to be set */
  margin-top: 1rem;
  color: white; /* Set the font color to white */
  padding: 0.5em 1em; /* adds some padding around the text */
  border: 1px solid white; /* white border */
  border-radius: 10px; /* rounded border */
  background-color: #747b81; /* initial background color */
  text-decoration: none; /* remove underline from link */
  transition: background-color 0.3s ease; /* transition effect for color change */
}

.button:hover {
  background-color: #ceccd1; /* change color on mouse over */
}
</style>
