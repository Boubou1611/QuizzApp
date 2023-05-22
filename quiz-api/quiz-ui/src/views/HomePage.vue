<template>
  <div class="homepage">
    <div class="score-list-container" :class="{ show: showScoreList }">
      <div class="score-list">
        <div
          v-for="scoreEntry in registeredScores.data.scores"
          :key="scoreEntry.id"
          class="score-entry"
        >
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
      </div>
    </div>

    <div class="toggle-bar" @click="toggleScoreList">Meilleures scores</div>
    <div class="content-container">
      <h1>Home page</h1>
      <RouterLink to="/new-quiz-page" class="quiz-button"
        >Démarrer le quiz !</RouterLink
      >
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      showScoreList: false, // Initially hidden
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
  methods: {
    toggleScoreList() {
      this.showScoreList = !this.showScoreList;
    },
  },
};
</script>

<style scoped>
.homepage {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  height: 100vh;
  background-color: #32174d; /* your desired color */
  padding-bottom: 3rem; /* adjust as needed */
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white; /* Set the font color to white */
}

.toggle-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50%; /* Adjust the width as desired */
  height: 1rem; /* Adjust the height as desired */
  background-color: #ffffff;
  color: #32174d;
  cursor: pointer;
  font-weight: bold;
  border-radius: 1rem; /* Rounded corners */
  margin-bottom: 1rem; /* Set the font color to white */
}

.score-list-container {
  display: flex;
  justify-content: center;
  width: 50%;
  height: 50%;
  align-items: center;
  margin-bottom: 1rem;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  border: 2px solid white; /* Add a white border */
  border-radius: 10px; /* Add border radius */
  background-color: #e0b0ff; /* Add background color inside the borders */
  overflow-y: auto; /* Make the score list container scrollable */
}

.score-list-container.show {
  max-height: 500px; /* Adjust the max-height value as needed */
}

.score-list {
  width: 50%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start; /* Align items vertically to the top */
  width: 100%; /* Adjust the width as desired */
  color: black; /* Set the font color to black */
  padding: 1rem; /* Add padding inside the score list */
}

.score-entry {
  width: calc(50% - 0.5rem); /* Adjust the column width with margin */
  text-align: center;
  margin-bottom: 1rem; /* Adjust the gap between score entries */
}

.quiz-button {
  margin-top: 1rem;
  color: white; /* Set the font color to white */
}
</style>
