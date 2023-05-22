<template>
  <div class="admin-page">
    <h1>Administration</h1>
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
    <button @click="createQuestion">Create Question</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

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
  async created() {
    let listOfAllQuest = await quizApiService.getAllQuestion();
    console.log(listOfAllQuest);
    this.questions = listOfAllQuest.data;
  },
};
</script>

<style scoped>
.question-page {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.question-list {
  margin-bottom: 20px;
}

.question-item {
  cursor: pointer;
  margin: 10px 0;
}
</style>
