<template>
  <div class="questions">
    <img v-if="question.image" :src="question.image" alt="Question image" />

    <h2>{{ question.title }}</h2>
    <h3>{{ question.text }}</h3>

    <div v-for="(answer, index) in question.possibleAnswers" :key="index">
      <a @click="$emit('answer-selected', index)">{{ answer.text }}</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  emits: ["answer-selected"],
};
</script>

<style scoped>
/* Ajoutez ici le style que vous souhaitez pour le composant */
</style>
