<template>
  <div class="admin-page">
    <div class="question-list">
      <div
        v-for="(question, index) in sortedQuestions"
        :key="index"
        class="question-item"
        @click="handleClick(index)"
      >
        {{ question.position }} - {{ question.text }}
      </div>
    </div>
    <button @click="createQuestion" class="button">Create Question</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "admin-panel",
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    handleClick(index) {
      console.log(`Question ${index + 1} clicked`);
      this.$router.push({
        name: "admin-display",
        query: { question: JSON.stringify(this.questions[index]) },
      });
    },
    createQuestion() {
      console.log("Create Question button clicked");
      this.$router.push({
        path: "/admin-create",
      });
    },
  },
  computed: {
    sortedQuestions() {
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return this.questions.sort((a, b) => a.position - b.position);
    },
  },
  async beforeRouteEnter(to, from, next) {
    const token = participationStorageService.getToken();
    console.log(token);

    if (token) {
      console.log(token);
      next();
    } else {
      next("/admin-login");
    }
  },
  async created() {
    let listOfAllQuest = await quizApiService.getAllQuestion();
    console.log(listOfAllQuest);
    this.questions = listOfAllQuest.data;
  },
};
</script>

<style scoped>
.admin-page {
  margin-top: 70px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #fff;
  background: #32174d;
}

.question-list {
  width: 50%;
  margin-bottom: 20px;
  padding: 20px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.question-item {
  cursor: pointer;
  margin: 10px 0;
  padding: 10px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
}

.button {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5em 1em;
  color: #fff;
  border: 1px solid #fff;
  border-radius: 10px;
  background-color: rgba(224, 176, 255, 1);
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #747b81;
}
</style>
