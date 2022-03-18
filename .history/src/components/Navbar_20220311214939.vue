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
  left:0;
  right:0;
  width:100%;
  height: 80px;
  padding: 30px 10px;
  display: flex;
  justify-content: space-between;
  align-content: center;
  .logo{
    color:rgb(0, 0, 0);
    font-weight: 700;
    text-decoration: none;
    font-size:2em;
    text-transform: uppercase;
  }
  ul{
    display: flex;
    justify-content: center;
    align-items: center;
    li{
      list-style: none;
      margin-left: 20px;
      a{
          color:rgb(27, 138, 179);
          height:50px;
          line-height: 50px;
          display: inline-block;
          text-decoration: none;
          font-size: 1.2em;
          padding: 0 15px;
          letter-spacing: 1px;
          cursor: pointer;
          &:hover{
              color:aliceblue;
              background-color: rgb(7, 101, 101);
          }
        }
        a.router-link-exact-active{
            color: #e73727;
        }
      }
    }
}
</style>