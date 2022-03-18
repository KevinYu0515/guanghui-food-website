<template>
    <header>
      <router-link to="/" class="logo">Logo</router-link>
      <ul>
          <li><router-link to="/home">主頁</router-link> </li>
          <li><router-link to="/about">關於</router-link> </li>
          <li><router-link to="/picture">相簿</router-link> </li>
          <li><router-link to="/contact">聯絡我們</router-link> </li>
      </ul>
    </header>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
header{
  position: fixed;
  
}
</style>