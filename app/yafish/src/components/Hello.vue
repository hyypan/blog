<template>
  <div class="content">
    <div class="vatar">
      <div class="face">
        <img class="img" src="../assets/pis.jpg"/>
        <h1>YaphetS</h1>
        <p>嗨！这里收集了关于linux,Python，vue,webpack相关的东西，停留2分钟，受益一生</p>
        <p>联系我:</p>
        <ul>
          <li><img class="first-img" src="../assets/wx.jpg"/> </li>
          <li><img src="../assets/qq.jpg"/> </li>
          <li><a href="https://github.com/hyypan"><img src="../assets/github.jpg"/> </a></li>
        </ul>
        <a v-link="content"><p class="enter">点击进入</p></a>
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.content{
    //font-family: 'Avenir', Helvetica, Arial, sans-serif;
    //-webkit-font-smoothing: antialiased;
    //-moz-osx-font-smoothing: grayscale;
    height:100%;
    //background-image: url('../assets/bg.jpg');
    background-image:url('https://onevcat.com//assets/images/background-cover.jpg');
    background-repeat: no-repeat;
}
.vatar{
    //background: #484141;
    width: 30%;
    height: 60%;
    margin: 0 auto;
    position: relative;
    top: 15%;
}
.face{
    width: 119%;
    height: 102%;
}
.img{
    display: block;
    width: 120px;
    height: 120px;
    border-radius: 60px;
    margin: 0 auto;
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
.enter{
    width:98%;
    height: 30px;
    border: 1px solid white;
    margin: 0 auto;
    border-radius: 8px;
    font-size: 19px;
    padding-top: 7px;
}
@media screen and (max-width: 600px) {
ul img{
    width: 30px;
    height: 30px;
    margin-right: 20px;
    border-radius: 15px;
}
.face p{
    font-size: 10px;
}
}
</style>
