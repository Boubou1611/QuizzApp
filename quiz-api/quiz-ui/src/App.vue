<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/admin-login">Administration</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  position: fixed;
  width: 100%; /* Makes the header span the full width of the screen */
  z-index: 1;
  background-color: #32174d;
  display: flex; /* added to make header a flex container */
  justify-content: flex-start; /* align items to the left */
  align-items: center; /* added to center the content vertically */
  height: 55px; /* you can adjust this to fit your design */
}

.content {
  margin-top: 2rem;
}

/* Rest of your styles */

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: auto; /* change to auto to allow centering */
  font-size: 12px;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    flex-wrap: wrap;
  }

  nav {
    margin-left: -1rem;
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  }

  .content {
    margin-top: 4rem;
  }
}
</style>
