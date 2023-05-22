<template>
  <div>
    <div>
      <label>Position:</label>
      <input v-model="position" type="text" />
    </div>
    <div>
      <label>Title:</label>
      <input v-model="title" type="text" />
    </div>
    <div>
      <label>Text:</label>
      <input v-model="text" type="text" />
    </div>
    <div v-for="(answer, index) in answers" :key="index">
      <input
        type="checkbox"
        :disabled="selectedAnswer !== null && selectedAnswer !== index"
        @change="handleCheckboxChange(index)"
      />
      <label>Answer {{ index + 1 }}:</label>
      <input v-model="answers[index]" type="text" />
    </div>
    <div>
      <label for="image">Choose an image:</label>
      <input
        type="file"
        id="image"
        accept="image/*"
        @change="handleImageChange"
      />
      <img v-if="imageData" :src="imageData" />
    </div>
    <button @click="createQuestion" :disabled="!isFormValid">
      Create Question
    </button>
    <router-link to="/admin">
      <button class="back-button">← Go Back</button>
    </router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      position: "",
      title: "",
      text: "",
      answers: ["", "", "", ""],
      selectedAnswer: null,
      imageData: null,
    };
  },
  computed: {
    isFormValid() {
      // check if all fields are filled
      return (
        this.position !== "" &&
        this.title !== "" &&
        this.text !== "" &&
        this.selectedAnswer !== null &&
        this.imageData !== null &&
        !this.answers.includes("")
      );
    },
  },
  methods: {
    handleCheckboxChange(index) {
      this.selectedAnswer = this.selectedAnswer === index ? null : index;
    },
    handleImageChange(e) {
      let file = e.target.files[0];
      let reader = new FileReader();
      reader.onloadend = () => {
        let image = new Image();
        image.onload = () => {
          let canvas = document.createElement("canvas");
          canvas.width = image.width;
          canvas.height = image.height;
          let context = canvas.getContext("2d");
          context.drawImage(image, 0, 0, image.width, image.height);
          this.imageData = canvas.toDataURL("image/jpeg");
        };
        image.src = reader.result;
      };
      reader.readAsDataURL(file);
      console.log(this.imageData);
    },
    async createQuestion() {
      console.log("Create Question button clicked");
      let payload = {
        position: this.position,
        title: this.title,
        text: this.text,
        image: this.imageData,
        possibleAnswers: this.createAnswersPayload(),
      };
      let token = participationStorageService.getToken();
      let log = await quizApiService.createQuestion(payload, token);
      if (log.status == 200) {
        alert("La question a bien été enregistré");
      } else {
        alert("ALERTE: la question ne s'est pas enregistré");
      }
    },
    createAnswersPayload() {
      let payload = [
        {
          text: this.answers[0],
          isCorrect: this.selectedAnswer == 0,
        },
        {
          text: this.answers[1],
          isCorrect: this.selectedAnswer == 1,
        },
        {
          text: this.answers[2],
          isCorrect: this.selectedAnswer == 2,
        },
        {
          text: this.answers[3],
          isCorrect: this.selectedAnswer == 3,
        },
      ];
      return payload;
    },
  },
};
</script>

<style scoped>
.back-button {
  border: none;
  background-color: transparent;
  cursor: pointer;
  font-size: 18px;
  color: green;
}
</style>
