<template>
  <div class="container d-flex justify-content-center">
    <form @submit.prevent="submitForm" class="w-20">
      <div class="mb-3">
        <label for="playerName" class="form-label">Mot de passe</label>
        <input
          type="password"
          class="form-control"
          id="playerName"
          placeholder="Entrez le mot de passe"
          v-model="password"
        />
      </div>
      <div class="d-flex justify-content-center">
        <button class="btn btn-primary custom-button" @click="launchLogin">
          Soumettre
        </button>
      </div>
      <p class="form-label warning">{{ warning }}</p>
    </form>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      password: "",
      warning: "",
    };
  },
  methods: {
    async launchLogin() {
      await quizApiService.getPassword(this.password).then((response) => {
        console.log(response);
        if (response.status === 200) {
          // Password is correct, you can now use the token
          console.log(response);
          console.log("Received token: ", response.data.token);
          participationStorageService.saveToken(response.data.token);
          this.$router.push("/admin");
        } else if (response.status === 401) {
          console.error(response.data.error);
          this.warning = response.data.error;
        }
      });
    },
  },
};
</script>

<style>
.container {
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.custom-button {
  background-color: rgba(224, 176, 255, 1);
  color: #ffffff;
}

.custom-button:hover {
  background-color: #747b81;
  color: #ffffff;
}

.warning {
  color: red;
  font-weight: bold;
}
</style>
