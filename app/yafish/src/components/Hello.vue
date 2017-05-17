<template>
  <div class="content">
    <div class="vatar">
      <div class="face">
        <img class="img" src="../assets/pis.jpg"/>
        <h1>YaphetS</h1>
        <p>聪明在于勤奋，天才在于积累</p>
        <p class="relation">联系方式:</p>
        <ul>
          <li><img class="first-img" src="../assets/wx.jpg"/> </li>
          <li><img src="../assets/qq.jpg"/> </li>
          <li><a href="https://github.com/hyypan"><img src="../assets/github.jpg"/> </a></li>
        </ul>
        <router-link to="/content" tag="div"><p class="enter2">点击进入</p></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created: function () {

  }
}
</script>

<style scoped>

.content{
    height:100%;
    background-image:url('../assets/bg1.jpeg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
.vatar{
    //background: #484141;
    margin: 0 auto;
    position: relative;
    top: 15%;
    color: white;
}
.face{
    width: 394px;
    height: 489px;
    //background: yellow;
    margin: 0 auto;
}
.img{
    display: block;
    width: 120px;
    height: 120px;
    border-radius: 60px;
    margin: 0 auto;
}
.relation{
    position:relative;
    top:20px;
    font-size:10px;
}
.face h1{
    text-align: center;
    padding-bottom: 13px;
    border-bottom: 1px solid sienna;
}
.face p{
    text-align: center;
}

.face ul{
    display: -webkit-inline-box;
    list-style: none;
}
ul{
    width: 100%;
    padding-bottom: 13px;
    padding-left: 0px;
    border-bottom: 1px solid sienna;
}
.first-img{

}
.face a{
    text-decoration: none;
}

ul img{
    width: 100px;
    height: 100px;
    margin-right: 48px;
    border-radius: 50px;
}
.enter2{
    font-size: 19px;
    position: relative;
    top: -14px;
}
.enter{
    width: 200px;
    height: 30px;
    border: 1px solid white;
    margin: 0 auto;
    border-radius: 8px;
    font-size: 19px;
    padding-top: 10px;
    /* letter-spacing: 38px; */
    letter-spacing: 26px;
    /* margin-left: 0; */
    padding-left: 40px;
}
@media screen and (max-width: 600px) {
ul img{
    width: 50px;
    height: 50px;
    margin-right: -11px;
    border-radius: 15px;
}
ul li{
    margin-left: 42px;
}

.face{
    width: 300px;
    height: 422px;
}
.enter{
    width: 119px;
    height: 18px;
    font-size: 15px;import
    padding-top: 3px;
    letter-spacing: 11px;
   padding-left: 11px;
}
.enter2{
    font-size: 19px;
    position: relative;
    top: -14px;
}
}
</style>
