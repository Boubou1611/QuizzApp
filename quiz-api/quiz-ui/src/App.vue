<script setup>
import { ref } from "vue";
import { RouterLink, RouterView, useRouter } from "vue-router";
import participationStorageService from "@/services/ParticipationStorageService";

const router = useRouter();
const showDeconnexion = ref(false);

const adminClick = () => {
  showDeconnexion.value = true;
};

const logout = () => {
  participationStorageService.removeToken();
  showDeconnexion.value = false;
  router.push("/");
};

const goHome = () => {
  showDeconnexion.value = false;
};
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <img src="./assets/logo.png" alt="logo" class="logo-img" />
        <RouterLink to="/" class="header-title" @click="goHome"
          >Home</RouterLink
        >
        <RouterLink to="/admin" @click="adminClick" class="admin-link"
          >Administration</RouterLink
        >
        <button v-if="showDeconnexion" @click="logout" class="deconnexion-link">
          Deconnexion
        </button>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  position: fixed;
  width: 100%;
  z-index: 1;
  background-color: #8871d1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 55px;
  padding: 0 20px;
}

.logo-img {
  max-height: 50px;
  margin-right: 10px;
}

.header-title,
.admin-link {
  font-weight: bold;
  color: white;
}

.header-title {
  margin-right: 20px; /* Adjust this value as needed */
}

nav {
  display: flex;
  align-items: center;
}

@media (min-width: 1024px) {
  /* Your media queries */
}

.deconnexion-link {
  font-weight: bold;
  color: red;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  text-decoration: underline;
  margin-left: 20px; /* Adjust this value as needed */
}
</style>
