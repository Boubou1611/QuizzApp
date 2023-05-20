<script>
import QuestionDisplay from "./QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  components: {
    QuestionDisplay,
  },
  data() {
    return {
      currentQuestion: {
        id: 0,
        position: 0,
        title: "",
        text: "",
        image: "",
        possibleAnswers: "",
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
    };
  },
  async created() {
    // Charger les informations nécessaires pour afficher la première question
    // On suppose qu'il y a une fonction async `fetchQuestion` qui récupère les questions par HTTP
    let quizInfo = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = quizInfo.data.size;
    let question = await quizApiService.getQuestByPosition(
      this.currentQuestionPosition
    ); // suppose que l'index commence à 0
    this.currentQuestion = question.data;
    console.log(this.currentQuestion);
    console.log(this.totalNumberOfQuestion);
  },
  methods: {
    async loadQuestionByPosition(position) {
      // Mettre à jour currentQuestion avec les données de la question à l'indice `position`
      let newQuestion = await quizApiService.getQuestByPosition(position);
      this.currentQuestion = Object.assign({}, newQuestion.data);
    },
    async answerClickedHandler(index) {
      // Vérifier si la réponse est correcte
      // Si la réponse est correcte et s'il reste des questions, aller à la question suivante
      // Si la réponse est incorrecte, terminer le quiz
      // const isAnswerCorrect = this.checkAnswer(
      //   this.currentQuestion.possibleAnswers,
      //   index
      // );
      participationStorageService.addToParticipationScore(index + 1);
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition <= this.totalNumberOfQuestion) {
        await this.loadQuestionByPosition(this.currentQuestionPosition);
      } else {
        this.endQuiz();
      }
      console.log(this.currentQuestion);
    },
    async endQuiz() {
      let payload = {
        playerName: participationStorageService.getPlayerName(),
        answers: participationStorageService.getParticipationScore(),
      };
      quizApiService.addParticipation(payload);
      let yourScore = await quizApiService.getQuizInfo();
      let scoresData = yourScore.data.scores;

      let playerObj = scoresData.find(
        (player) => player.playerName === payload.playerName
      );

      this.$router.push({
        name: "PersonnalScore",
        query: { score: playerObj.score, name: playerObj.playerName },
      });
    },
    checkAnswer(possibleAnswers, index) {
      // Parcourir la liste possibleAnswers
      for (let i = 0; i < possibleAnswers.length; i++) {
        if (possibleAnswers[i].isCorrect === true) {
          if (i === index) {
            return true;
          }
        }
      }
      return false;
    },
  },
};
</script>

<template>
  <div>
    <h1>
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}
    </h1>
    <QuestionDisplay
      :question="currentQuestion"
      @answer-selected="answerClickedHandler"
    />
  </div>
</template>

<style scoped>
/* Ajoutez ici le style que vous souhaitez pour le composant */
</style>
