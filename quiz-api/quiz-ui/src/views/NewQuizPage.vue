<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <p class="form-label">Nom du joueur</p>
        <input
          type="text"
          class="form-control"
          id="playerName"
          placeholder="Entrez votre pseudo"
          v-model="username"
        />
      </div>
      <button class="btn btn-primary" @click="launchNewQuiz">Soumettre</button>
    </form>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      username: "",
    };
  },
  methods: {
    launchNewQuiz() {
      // Ici, vous pouvez mettre la logique pour stocker le nom du joueur et rediriger vers la première question du quiz
      participationStorageService.savePlayerName(this.username);
      participationStorageService.saveParticipationScore();
      alert(`Le nom du joueur est : ${this.username}`);
      console.log(`Launching new quiz for player: ${this.username}`);
      this.$router.push("/questions");
      // Stockage et redirection à implémenter
    },
  },
};
</script>
