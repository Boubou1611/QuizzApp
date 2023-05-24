<template>
  <div class="questions">
    <img v-if="question.image" :src="question.image" alt="Question image" />

    <h2>{{ question.title }}</h2>
    <h3>{{ question.text }}</h3>

    <div class="answer-container">
      <div
        v-for="(answer, index) in question.possibleAnswers"
        :key="index"
        class="answer-item"
      >
        <a
          @click="selectAnswer(index)"
          :class="{
            'correct-answer': answer.isCorrect,
            'incorrect-answer': !answer.isCorrect,
            selected: selectedAnswer === index,
          }"
        >
          {{ answer.text }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedAnswer: null,
    };
  },
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  methods: {
    selectAnswer(index) {
      this.selectedAnswer = index;
      setTimeout(() => {
        this.$emit("answer-selected", index);
        this.selectedAnswer = null;
      }, 300);
    },
  },
  emits: ["answer-selected"],
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.questions {
  color: white;
}

.questions img {
  height: 400px;
  margin: auto; /* center the image */
  display: block;
  border: 5px solid purple; /* change the color and thickness as per your requirement */
  border-radius: 15px;
}

.answer-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.answer-item {
  width: 48%; /* Slightly less than 50% to allow for space between items */
  box-sizing: border-box; /* To include padding and border in width calculation */
}
.questions a {
  display: block; /* This makes the anchor element take up the full width of the parent div */
  padding: 10px;
  border: 2px solid white;
  border-radius: 10px;
  margin: 10px;
  transition: background-color 0.3s ease;
  background-color: rgba(
    224,
    176,
    255,
    0.8
  ); /* Replace with the color you want */
  color: #ffffff;
}

.questions h3 {
  margin-top: 20px;
  font-size: 2.5em;
  margin-left: 20px;
}

.questions h2 {
  margin-left: 20px;
}

.questions a:hover {
  background-color: #333;
}

.questions .correct-answer.selected {
  background-color: green;
}

.questions .incorrect-answer.selected {
  background-color: red;
}
</style>
