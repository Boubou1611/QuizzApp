<template>
  <div class="admin-edit">
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
    <div v-for="(answer, index) in answers" :key="index" class="form-group">
      <input
        type="checkbox"
        :disabled="selectedAnswer !== null && selectedAnswer !== index"
        @change="handleCheckboxChange(index)"
      />
      <label>Réponse {{ index + 1 }}:</label>
      <input v-model="answers[index]" type="text" />
    </div>
    <div>
      <div class="image-container">
        <img v-if="imageData" :src="imageData" class="image-preview" />
      </div>
      <input
        type="file"
        id="image"
        accept="image/*"
        @change="handleImageChange"
      />
    </div>
    <button @click="createQuestion" :disabled="!isFormValid">
      Create Question
    </button>
    <router-link to="/admin">
      <button class="back-button">← Annuler</button>
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
        this.$router.push("/admin");
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
.admin-edit {
  margin-top: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #32174d;
  color: #fff;
  padding: 20px;
}

.admin-edit label {
  color: #fff;
}

.admin-edit input[type="text"],
.admin-edit input[type="file"] {
  border-radius: 15px;
  padding: 10px;
  margin: 10px 0;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

.admin-edit img {
  max-height: 380px;
  height: auto;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 300px; /* adjust as needed */
  height: 300px; /* adjust as needed */
  border-radius: 50%;
  overflow: hidden; /* this will make the image fit into the rounded box */
  margin: 10px auto; /* center the box */
  background-color: #fff; /* or any color you like */
  border: 2px solid #fff; /* or any color you like */
}

.image-preview {
  width: 100%;
  height: 100%;
  object-fit: cover; /* this will make the image cover the whole area of the box */
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.back-button {
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

.back-button:hover {
  background-color: #747b81;
}

button {
  border: 2px solid #fff;
  background-color: rgba(0, 0, 0, 0);
  color: #fff;
  padding: 10px 20px;
  border-radius: 15px;
  margin-top: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
