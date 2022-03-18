<template>
  <div class="navbar">
    <nav>
            <router-link to="/" class="logo">Logo</router-link>
            <ul v-show="!mobile" class="navigation">
                <li><router-link to="/home">Home</router-link> </li>
                <li><router-link to="/about">About</router-link> </li>
                <li><router-link to="/program">Program</router-link> </li>
                <li><router-link to="/entertain">Entertain</router-link> </li>
                <li><router-link to="/creativity">Creativity</router-link> </li>
                <li><router-link to="/outdoors">Outdoors</router-link> </li>
           </ul>
    <nav></nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
