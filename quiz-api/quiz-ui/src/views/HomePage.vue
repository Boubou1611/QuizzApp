<template>
  <div class="homepage">
    <div class="sun"></div>
    <div class="mercury-outline">
      <div class="mercury"></div>
    </div>

    <div class="venus-outline">
      <div class="venus"></div>
    </div>

    <div class="earth-outline">
      <div class="earth">
        <div class="earth-circle">
          <div class="earth-inner"></div>
        </div>
      </div>
    </div>
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
      <h1>AstroQuiz</h1>
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
  background-color: rgba(224, 176, 255, 0.8); /* Adjust the opacity here */
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

.quiz-button:hover {
  background-color: #ceccd1; /* change color on mouse over */
}

.sun {
  height: 150px; /* Increase the height */
  width: 150px; /* Increase the width */
  background-image: url(../assets/sun.png);
  border-radius: 50%;
  background-size: cover;
  box-shadow: -8px 4px 112px #f9c05f; /* Adjust the box shadow */
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 0;
}

.mercury {
  height: 25px;
  width: 25px;
  background: radial-gradient(circle, #747b81 60%, #ceccd1 75%);
  border-radius: 50%;
  position: absolute;
  left: 43%; /* Set to 50% to start at the center */
  top: 45%; /* Set to 50% to start at the center */
  transform: translate(-50%, -50%);
  animation: orbit2 25s linear infinite;
}

.venus {
  height: 50px;
  width: 50px;
  background-image: url(../assets/venus.png);
  background-size: 100%;
  border-radius: 50%;
  position: absolute;
  box-shadow: -4px 2px 56px #c1aa81;
  left: 43%; /* Set to 50% to start at the center */
  top: 43%; /* Set to 50% to start at the center */
  transform: translate(-50%, -50%);
  animation: orbit3 50s linear infinite;
}

.earth {
  height: 60px;
  width: 60px;
  background-image: url(../assets/earth.png);
  background-size: 100%;
  border-radius: 50%;
  position: absolute;
  box-shadow: -4px 2px 56px #2855d6;
  left: 43%; /* Set to 50% to start at the center */
  top: 46%; /* Set to 50% to start at the center */
  transform: translate(-50%, -50%);
  animation: orbit4 140s linear infinite;
}

@keyframes orbit2 {
  from {
    transform: rotate(0deg) translateX(112px) rotate(0deg);
  }
  to {
    transform: rotate(360deg) translateX(112px) rotate(-360deg);
  }
}

@keyframes orbit3 {
  from {
    transform: rotate(0deg) translateX(180px) rotate(0deg);
  }
  to {
    transform: rotate(360deg) translateX(180px) rotate(-360deg);
  }
}

@keyframes orbit4 {
  from {
    transform: rotate(0deg) translateX(265px) rotate(0deg);
  }
  to {
    transform: rotate(360deg) translateX(265px) rotate(-360deg);
  }
}

@keyframes orbit5 {
  from {
    transform: rotate(0deg) translateX(40px) rotate(0deg);
  }
  to {
    transform: rotate(360deg) translateX(40px) rotate(-360deg);
  }
}

p {
  color: white;
  font-family: system-ui;
  position: absolute;
  left: -62px;
  top: -11px;
}

.mercury-outline,
.venus-outline,
.earth-outline {
  border-radius: 50%;
  border: 3px dotted #ddd9;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.mercury-outline {
  height: 230px;
  width: 230px;
}

.venus-outline {
  height: 350px;
  width: 350px;
}

.earth-outline {
  height: 530px;
  width: 530px;
}

.earth-circle {
  height: 80px;
  width: 80px;
  border: 1px dotted #fff;
  position: relative;
  left: -10px;
  top: -10px;
  border-radius: 40px;
}

.earth-inner {
  height: 10px;
  width: 10px;
  background-color: white;
  border-radius: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
  left: 45%;
  top: 45%;
  animation: orbit5 10s linear infinite;
}
</style>
