<template>
  <div
    class="container d-flex justify-content-center align-items-center vh-100"
  >
    <form @submit.prevent="submitForm" class="w-20">
      <div class="mb-3">
        <label for="playerName" class="form-label">Nom du joueur</label>
        <input
          type="text"
          class="form-control"
          id="playerName"
          placeholder="Entrez votre pseudo"
          v-model="username"
        />
      </div>
      <div class="d-flex justify-content-center">
        <button class="btn btn-primary custom-button" @click="launchNewQuiz">
          Continuer
        </button>
      </div>
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
      participationStorageService.removePlayerName();
      participationStorageService.removePlayerScore();
      participationStorageService.savePlayerName(this.username);
      participationStorageService.saveParticipationScore();
      console.log(`Launching new quiz for player: ${this.username}`);
      this.$router.push("/questions");
    },
  },
  mounted() {
    this.$nextTick(function () {
      // Code that will run only after the entire view has been rendered
      this.$el.classList.add(
        "d-flex",
        "justify-content-center",
        "align-items-center"
      );
    });
  },
};
</script>

<style>
.form-label {
  color: white;
}

.custom-button {
  background-color: #654321; /* Replace with the color you want when mouse is over */
  color: #000000; /* Replace with the color you want when mouse is over */
}

.custom-button:hover {
  background-color: rgba(
    224,
    176,
    255,
    0.8
  ); /* Replace with the color you want */
  color: #ffffff; /* Replace with the color you want */
}
</style>
