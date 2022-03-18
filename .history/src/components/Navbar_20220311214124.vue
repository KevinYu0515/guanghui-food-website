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
  top:0;
  right:0;
  width:100%;
  height: 80px;
  padding: 30px 100px;
  display: flex;
  justify-content: ;
}
</style>