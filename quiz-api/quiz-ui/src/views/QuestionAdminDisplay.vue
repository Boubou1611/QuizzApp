<template>
  <div class="admin-display">
    <img v-if="question.image" :src="question.image" alt="Question image" />

    <h2>{{ question.title }}</h2>
    <h3>{{ question.text }}</h3>

    <div v-for="(answer, index) in jsonifyAnswers" :key="index">
      <a @click="$emit('answer-selected', index)">{{ answer.text }}</a>
    </div>

    <div class="buttons">
      <router-link to="/admin-edit" class="btn" @click="editQuestion">
        Editer
      </router-link>

      <button class="btn" @click="deleteQuestion">Supprimer</button>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      question: JSON.parse(this.$route.query.question),
    };
  },
  computed: {
    jsonifyAnswers() {
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return (this.question.possibleAnswers = JSON.parse(
        this.question.possibleAnswers
      ));
    },
  },
  methods: {
    editQuestion() {
      this.$router.push({
        name: "admin-edit",
        query: { question: JSON.stringify(this.question) },
      });
    },
    async deleteQuestion() {
      let token = participationStorageService.getToken();
      console.log(token);
      await quizApiService.deleteQuestion(this.question.id, token);
      this.$router.push({
        path: "/admin",
      });
    },
  },
  // props: {
  //   question: {
  //     type: Object,
  //     required: true,
  //   },
  // },
};
</script>

<style scoped>
.admin-display {
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #fff;
  background: #32174d;
}

.admin-display img {
  max-height: 380px;
  height: auto;
}

.admin-display h2,
.admin-display h3 {
  text-align: center;
}

.admin-display a {
  color: #fff;
  text-decoration: none;
}

.btn {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 2px solid #fff;
  border-radius: 15px;
  background-color: rgba(224, 176, 255, 0.8);
  color: #fff;
  text-decoration: none;
  transition: background-color 0.5s, color 0.5s;
}

.btn:hover {
  background-color: #747b81;
  color: #fff;
}

.buttons {
  display: flex;
  justify-content: space-between;
  width: 50%;
}
</style>
