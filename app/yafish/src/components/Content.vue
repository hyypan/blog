<template>
<div>
  <header-components></header-components>
  <div class="content">
    <div class="contentCenter">
      <div class="banner">
        <div class="runningImg">
          <img class="imgStyle" src="../assets/logo.png"/>
          <img class="imgStyle" src="../assets/Python.jpg"/>
          <img class="imgStyle" src="../assets/django.jpg"/>
          <img class="imgStyle" src="../assets/search.png"/>
          <img class="imgStyle" src="../assets/wx.jpg"/>
          <img class="imgStyle" src="../assets/yinhe.jpg"/>
          <img class="imgStyle" src="../assets/bg.jpg"/>
          <img class="imgStyle" src="../assets/github.jpg"/>
          <img class="imgStyle" src="../assets/linux.jpg"/>
        </div>
      </div>
      <div class="titles">
        <table cellspacing="30">
          <tr>
            <td><img class="imgsTwo" src="../assets/python.png"/>python</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>vue</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>linux</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>ansible</td>
          </tr>
          <tr>
            <td><img class="imgsTwo" src="../assets/logo.png"/>docker</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>Django</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>nginx</td>
            <td><img class="imgsTwo" src="../assets/logo.png"/>其他</td>
          </tr>

        </table>
      </div>
      <div>
        <div class="terms">
          <div class="objects" v-for="t in c">
            <div>
              <span>最新更新时间</span>
              <span>{{t.time}}</span>
            </div>
            <img class="imgThree" src="../assets/logo.png"/>
            <p class="objectsIterm">{{t.tittle}}</p></div>
        </div>
        <div class="rightPart">
          <table>
            <th>推荐链接</th>
            <tr class="url" v-for="u in urls"><a :href="u.url">{{u.tittle}}</a></tr>
          </table>
        </div>
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
    width: 85%;
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
  width: 80%;
  background: wheat;
  position: relative;
  float: left;
  margin-bottom: 100px;
}
.objects{
    margin: 54px;
    border-bottom: 1px solid silver;
}
.rightPart{
    position: relative;
    float: left;
    margin-left: 25px;
}
.rightPart table{
    margin-left: 30px;
}
.imgThree{
    width:50px;
    width: 50px;
    border: 1px solid #575963;
    border-radius: 14px;
}
.objectsIterm{
    margin-top: 5px;
    display: block;
    position: relative;
    float: left;
    width: 74%;
    background: beige;
}
.url{
    border-bottom: 1px solid rebeccapurple;

}
</style>
<script>
import HeaderComponents from './common/header'
import FooterComponents from './common/footer'
export default{
  data () {
    return {
      msg: '正在开发中',
      c:[{'tittle':'文章1fdfkfkjsflkjfjseiorkfjsdjk,lfjsldfjklsdjflksdjflsdjflsdkfsjd','time':'2019-2-2'},{'tittle':'文章2','time':'2019-2-2'},{'tittle':'文章3','time':'2019-2-2'},{'tittle':'文章4','time':'2019-2-2'},{'tittle':'文章5','time':'2019-2-2'},{'tittle':'文章6','time':'2019-2-2'},{'tittle':'文章7','time':'2019-2-2'},{'tittle':'文章8','time':'2019-2-2'}],
      cc:['dfswreeeeeeeeeeeeeeeeeeerweerwrrrrrrrrrrrrrwetwe','gdg'],
      urls:[{'tittle':'百度新闻','url':'http://www.django-rest-framework.org'},{'tittle':'百度新闻','url':'www.baidu.com',},{'tittle':'百度新闻','url':'www.baidu.com',}]
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
