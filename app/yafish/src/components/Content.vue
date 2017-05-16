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
        <!--<table cellspacing="60" cellpadding="1">-->
          <ul class="firsttr">
            <li><img class="imgsTwo" src="../assets/python.png"/><span>python</span></li>
            <li><img class="imgsTwo" src="../assets/logo.png"/><span>vue</span></li>
            <li><img class="imgsTwo" src="../assets/linux.jpg"/><span>linux</span></li>
            <li><img class="imgsTwo" src="../assets/ansible.jpg"/><span>ansible</span></li>
            <li><img class="imgsTwo" src="../assets/docker.jpg"/><span>docker</span></li>
            <li><img class="imgsTwo" src="../assets/django.jpg"/><span>django</span></li>
            <li><img class="imgsTwo" src="../assets/nginx.jpg"/><span>nginx</span></li>
          </ul>
      </div>
      <div class="articles">
        <div class="terms">
          <div class="objects" v-for="t in c">
            <div>
              <router-link class="objectsIterm" to="/content/articles">{{t.tittle}}</router-link>
            </div>
            <div class="detail">
              <span>作者:{{t.author}}</span>
              <span>最近更新时间:{{t.time}}</span>
              <span>{{t.time}}</span>
              <span>评论{{t.comments}}条</span>
              <span>点赞次数{{t.exTimes}}</span>
            </div>
            <div>{{t.content}}</div>
          </div>
        </div>
        <div class="more" @click="getMore">加载更多...</div>
      </div>
    </div>
  </div>
  <footer-components></footer-components>
</div>
</template>
<style scoped>
    html, body{
        background:#fff;
    }
</style>
<style scoped>
.detail{
    font-size: 12px;
    padding: 10px;
}
.content{
        color:#211e1e;
        position: relative;
        float: left;
        width: 100%;
        margin-top: 90px;
}
.contentCenter{
    width: 75%;
    margin: 0 auto;
    position:relative;
    top: 53px;
}
.banner{
    width: 100%;
    height: 58%;
}
.imgStyle{
  display:none;
  height:300px;
  width:100%;
}
.titles{
    background: white;
    width: 100%;
    position:relative;
}
.titles ul{
    display: -webkit-inline-box;
    list-style: none;
    padding: 0;
    width: 95%;

}
.titles li{
    width: 13%;
    display: -webkit-box;

}
.imgsTwo{
    width: 50px;
    height: 44px;
    border: 1px solid #FF9800;
    border-radius: 12px;
}
.firsttr li span{
    position: relative;
    top: 11px;
    color: #FF9800;
    font-size: 12px;
    left: -46px;
    text-align: center;

}
.terms{
  width: 100%;
  position: relative;
  margin-bottom: 26px;
}
.objects{
    margin: 10px;
    height: 76px;
    border-bottom: 1px solid silver;
    text-align: center;
    padding-bottom: 10px;
    padding-top: 10px;
}
.rightPart{
    position: relative;
    float: left;
    width: 100%;
}
.rightPart table{
    margin-left: 30px;
}
.imgThree{
    width:50px;
    border: 1px solid #575963;
    border-radius: 14px;
}
.objectsIterm{
    margin-top: 5px;
    display: block;
    position: relative;
    width: 74%;
    background: beige;
    margin-left: 16%;
    }
.url{
    border-bottom: 1px solid rebeccapurple;

}
.more{
    width: 100%;
    position: relative;
    text-align: center;
}
.articles{
}
.timeWaring{
    font-size: 12px;
    padding: 10px;
}
@media(max-width:670px){
.imgStyle{
  display:none;
  height:190px;
  width:100%;
}
.imgsTwo{
   width: 30px;
   font-size: 10px;
}
.contentCenter{
    width: 100%;
    margin: 0 auto;
    position:relative;
    top: -40px;
}
.titles{
    display:none;
    background: white;
    width: 100%;
    position:relative;
}
}

</style>
<script>
import HeaderComponents from './common/header'
import FooterComponents from './common/footer'
export default{
  data () {
    return {
      msg: '正在开发中',
      c:[{'tittle':'文章11','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章12','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章13','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章14','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章15','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章16','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章17','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'},
      {'tittle':'文章18','time':'2019-2-2','content':'文章内容', 'exTimes':10,'comments':2, 'author': 'yafish'}],
      cc:['dfswreeeeeeeeeeeeeeeeeeerweerwrrrrrrrrrrrrrwetwe','gdg'],
      urls:[
      {'tittle':'百度新闻','url':'http://www.django-rest-framework.org'},
      {'tittle':'百度新闻','url':'www.baidu.com',},
      {'tittle':'百度新闻','url':'www.baidu.com',}]
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

        })


        },5000)
    },
    components:{
    FooterComponents,HeaderComponents,
    },

    methods: {
      getMore:function (){
      var allItems=$('.objects').length + $('.append1').length
      console.log('all',allItems)
      let that=this;
      if (allItems<=this.c.length){
            for(var i=0;i<10;i++){
              $('.terms').append('<div class="append1"><div class="tittleStyle"><a href="/content/articles">'+this.c[i+7].tittle+'</a></div><div class="allDetail"><span>'+'作者:'+this.c[i+7].author+'</span><span>'+'最近更新时间:'+this.c[i+7].time+'</span><span>'+'评论:'+this.c[i+7].comments+'</span><span>'+'点赞次数:'+this.c[i+7].exTimes+'</span></div><div class="contentArticle">'+this.c[i+7].content+'</div></div>')
              $('.append1').css({'margin': '10px','border-bottom': '1px solid silver','height': '76px','padding-bottom': '10px','padding-top':'10px'})
              $('.tittleStyle').css({'text-align': 'center'})
              $('.allDetail').css({'text-align':'center','font-size': '12px','padding': '10px'})
              $('.contentArticle').css({'text-align':'center'})
      }
      }else{
      alert(0)
      }



      }
    },
    created: function(){

    }
}
</script>
