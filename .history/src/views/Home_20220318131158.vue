<template>
  <div class='home'>
    <Navbar></Navbar>
    <section class="sec1">
      <div class="timetable">
          <p>營業時間</p>
          <ul>
            <li>週一 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週二 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週三 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週四 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週五 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週六 &nbsp;0600~0900 </li>
            <li>週日 公休</li>
          </ul>
      </div>
    </section>
    <section class="sec2"></section>
    <section class="sec3"></section>
    <section class="sec4"></section>
    <section class="sec5"></section>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
export default {
  name: 'Home',
  components:{
    Navbar
  }
}
</script>

<style lang="scss" scoped>
.home{
  margin: 0 auto 0 auto;
  background: #F5A02A;
  width: 65%;
  height: 100vh;
  .sec1{
    width:100%;
    height:55vh;
    background: url("../assets/store.jpg");
    background-size: cover;
    .timetable{
      display: inline-block;
      background: rgba(247,227,177,0.7);
      padding: 20px;
      margin: 120px;
      margin-left: 50px;
      p{
        font-weight: bolder;
      }
      li{
        font-size: 2.8vmin;
        color:#AF3314;
      }
    }
  }
}
.home_picture{
  height:80%;
  width:80%;
}
</style>
