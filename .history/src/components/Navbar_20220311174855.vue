<template>
  <header>
    <nav>
        <router-link to="/" class="logo">Logo</router-link>
        <ul v-show="!mobile" class="navigation">
            <li><router-link to="/home">主頁</router-link> </li>
            <li><router-link to="/about">關於</router-link> </li>
            <li><router-link to="/picture">相簿</router-link> </li>
            <li><router-link to="/contact">聯絡我們</router-link> </li>
        </ul>
    </nav>
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
  top: 0;
  right: 0;
  nav{
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
  }

}
h3 {
  margin: 40px 0 0;
}

</style>