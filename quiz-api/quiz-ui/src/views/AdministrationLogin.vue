<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <p class="form-label">Mot de passe</p>
        <input
          type="text"
          class="form-control"
          id="playerName"
          placeholder="Entrez le mot de passe"
          v-model="password"
        />
      </div>
      <button class="btn btn-primary" @click="launchLogin">Soumettre</button>
      <p class="form-label">{{ warning }}</p>
    </form>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

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
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
