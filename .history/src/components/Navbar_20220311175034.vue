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
  display: flex;
  width:100%;
  height:80px;
  justify-content: space-between;
  align-items: center;
  padding: 0px 60px 0 50px;
  background-color:azure;
  box-shadow: 0 5px 30px rgba(0,0,0,0.05);
  z-index: 1000;
  transition: 0.5s ease all;
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
</style>