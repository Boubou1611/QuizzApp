<template>
  <div class="container">
    <p class="form-label">ADMINISTRATION</p>
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
      await quizApiService
        .getPassword(this.password)
        .then((response) => {
          if (response.status === 200) {
            // Password is correct, you can now use the token
            console.log("Received token: ", response.data.token);
            this.$router.push("/admin");
          }
        })
        .catch((error) => {
          // Handle network or server errors
          if (error.response.status === 401) {
            // Incorrect password
            this.warning = "Incorrect password";
          }
          console.error("An error occurred: ", error);
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
