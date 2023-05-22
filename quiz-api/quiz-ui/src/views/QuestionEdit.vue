<template>
  <div class="admin-edit">
    <img v-if="question.image" :src="question.image" alt="Question image" />

    <input type="file" @change="onFileChange" />

    <input
      type="text"
      v-model="question.title"
      placeholder="Enter question title"
    />

    <textarea
      v-model="question.text"
      placeholder="Enter question text"
    ></textarea>

    <div v-for="(answer, index) in question.possibleAnswers" :key="index">
      <input
        type="text"
        v-model="answer.text"
        placeholder="Enter answer text"
      />
      <input
        type="checkbox"
        :disabled="selectedAnswer !== null && selectedAnswer !== index"
        @change="handleCheckboxChange(index)"
      />
      This is the correct answer
    </div>

    <div class="buttons">
      <button @click="editQuestion" class="btn">
        Enregistrer les changements
      </button>
      <router-link to="/admin" class="btn"> Annuler </router-link>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  data() {
    return {
      question: JSON.parse(this.$route.query.question),
      selectedAnswer: null,
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      let reader = new FileReader();

      reader.onloadend = () => {
        this.question.imageData = reader.result;
      };

      if (file) {
        reader.readAsDataURL(file);
      }
    },
    async editQuestion() {
      console.log("Create Question button clicked");
      let payload = {
        position: this.question.position,
        title: this.question.title,
        text: this.question.text,
        image: this.question.imageData,
        possibleAnswers: this.question.possibleAnswers,
      };
      console.log(payload);
      let log = await quizApiService.updateQuestion(this.question.id, payload);
      if (log.status == 204) {
        alert("La question a bien été enregistré");
      } else {
        alert("ALERTE: la question ne s'est pas enregistré");
      }
    },
    handleCheckboxChange(index) {
      this.selectedAnswer = this.selectedAnswer === index ? null : index;
    },
  },
};
</script>

<style scoped>
.btn {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 2px solid green;
  border-radius: 15px;
  background-color: white;
  color: green;
  text-decoration: none;
  transition: background-color 0.5s, color 0.5s; /* fade effect */
}

.btn:hover {
  background-color: green;
  color: white;
}

.buttons {
  display: flex;
  justify-content: space-between;
}
</style>
