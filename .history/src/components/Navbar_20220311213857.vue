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
  width: 100%;
  height: 80px;
  justify-content: space-between;
  align-items: center;
  padding: 0px 60px 0 50px;
  background:none;
  flex-direction: row;

      .logo{
          color:midnightblue;
          font-weight: 700;
          font-size: 2em;
          text-decoration: none;
          text-transform: uppercase;
          margin: 5px 8px 0 0;
          transition: 0.5s ease all;
      }

      nav ul  {
          position: relative;
          display: flex;
          flex-direction: row;

          li {
              List-style:none;

              a{
                  color:#F7E3B1;
                  height:50px;
                  font-weight: bold;
                  line-height: 50px;
                  display: inline-block;
                  text-decoration: none;
                  font-size: 1.2em;
                  padding: 0 15px;
                  letter-spacing: 1px;
                  cursor: pointer;
                  &:hover{
                      color:aliceblue;
                  }
              }
              a.router-link-exact-active{
                color: aliceblue;
                text-decoration: underline;
              }
          }
      }

      .navigation{
          display:flex;
          align-items: center;
          flex:1;
          justify-content: right;
        }
    }
</style>