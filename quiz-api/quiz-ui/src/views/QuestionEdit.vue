<template>
  <div class="admin-edit">
    <img v-if="question.image" :src="question.image" alt="Question image" />

    <div class="form-group">
      <input type="file" @change="onFileChange" />
    </div>

    <div class="form-group">
      <input
        type="number"
        v-model="question.position"
        placeholder="Enter question position"
      />
    </div>

    <div class="form-group">
      <input
        type="text"
        v-model="question.title"
        placeholder="Enter question title"
      />
    </div>

    <div class="form-group">
      <textarea
        v-model="question.text"
        placeholder="Enter question text"
      ></textarea>
    </div>

    <div
      v-for="(answer, index) in question.possibleAnswers"
      :key="index"
      class="form-group"
    >
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

      if (file) {
        reader.onloadend = () => {
          this.question.image = reader.result;
          this.question.image = URL.createObjectURL(file);
        };
        reader.readAsDataURL(file);
      }
    },
    async editQuestion() {
      console.log("Create Question button clicked");
      let payload = {
        position: this.question.position,
        title: this.question.title,
        text: this.question.text,
        image: this.question.image,
        possibleAnswers: this.question.possibleAnswers,
      };
      console.log(payload);
      let log = await quizApiService.updateQuestion(this.question.id, payload);
      if (log.status == 204) {
        alert("La question a bien été enregistré");
        this.$router.push("/admin");
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
.admin-edit {
  margin-top: 320px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #fff;
  background: #32174d;
  padding: 20px;
}

.admin-edit img {
  max-height: 380px;
  height: auto;
}

.form-group {
  margin-top: 20px;
  width: 100%;
  margin-bottom: 20px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border-radius: 15px;
  border: none;
  background: #fff;
  color: #000;
}

.btn {
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

.btn:hover {
  background-color: #747b81;
}

.buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
</style>
