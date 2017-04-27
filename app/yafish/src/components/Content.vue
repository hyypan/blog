<template>
<div>
  <header-components></header-components>
  <div class="content">
    <div class="contentCenter">
      <div class="banner">
        <div class="runningImg">
          <img class="imgStyle" src="../assets/logo.png"/>
          <img class="imgStyle" src="../assets/python.png"/>
          <img class="imgStyle" src="../assets/qq.jpg"/>
          <img class="imgStyle" src="../assets/search.png"/>
          <img class="imgStyle" src="../assets/wx.jpg"/>
          <img class="imgStyle" src="../assets/yinhe.jpg"/>
          <img class="imgStyle" src="../assets/bg.jpg"/>
          <img class="imgStyle" src="../assets/github.jpg"/>
          <img class="imgStyle" src="../assets/icon.png"/>
        </div>
      </div>
      <div class="titles">
        <table cellspacing="30">
          <tr>
            <td><img class="imgsTwo" src="../assets/python.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
          </tr>
          <tr>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>1</td>
          </tr>

        </table>
      </div>
      <div>
        <div class="terms">
            <div class="objects" v-for="t in c">{{t}}</div>
        </div>
        <div class="rightPart">这里是推荐链接</div>
      </div>
    </div>
  </div>
  <footer-components></footer-components>
</div>
</template>
<style>
    html, body{
        background:#fff;
    }
</style>
<style scoped>
.content{
        color:red;
        position: relative;
        float: left;
        width: 100%;
        /* margin: 90px; */
        margin-top: 90px;
}
.contentCenter{
    background: rebeccapurple;
    width: 75%;
    margin: 0 auto;
    position:relative;
}
.banner{
    width: 100%;
    background: wheat;
    height: 58%;
}
.imgStyle{
  display:none;
  height:300px;
  width:100%;
  //position:relative;
  //margin-top: -300px;
}
.titles{
    background: white;
    width: 100%;
    position:relative;
}
.titles table{
    padding: 22px;
    width: 50%;
    text-align: center;
    font-size: 25px;
}
.titles td{
    border: 1px solid black;
}
.imgsTwo{
   width: 26px;
}
.terms{
  width: 65%;
  background: wheat;
  position: relative;
  float: left;
}
.objects{
    margin: 25px;
    border-bottom: 1px solid silver;
}
.rightPart{
    position: relative;
    float: left;
    margin-left: 25px;
}
</style>
<script>
import HeaderComponents from './common/header'
import FooterComponents from './common/footer'
export default{
  data () {
    return {
      msg: '正在开发中',
      c:['文章','文章','文章','文章','文章','文章','文章','文章',]
    }
  },
    mounted: function(){
    let that=this;
    var imgs=document.getElementsByClassName('imgStyle')
        $(imgs[0]).show()
        var setInterObj=setInterval(function(){

        var randomNum=Math.floor(Math.random()*10)
        console.log(randomNum)
        $(imgs[randomNum]).animate({'marginTop':'0px'},function(){
        $(this).show().siblings().hide()
          //$(this).animate({'marginTop':'-300px'})

        })


        },5000)
        //setInterObj

    },
    components:{
    FooterComponents,HeaderComponents,
    },

    methods: {

    },
    created: function(){


    }
}
</script>
