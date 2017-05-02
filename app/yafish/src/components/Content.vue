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
            <li><img class="imgsTwo" src="../assets/python.png"/></li>
            <li><img class="imgsTwo" src="../assets/logo.png"/></li>
            <li><img class="imgsTwo" src="../assets/linux.jpg"/></li>
            <li><img class="imgsTwo" src="../assets/ansible.jpg"/></li>
            <li><img class="imgsTwo" src="../assets/docker.jpg"/></li>
            <li><img class="imgsTwo" src="../assets/django.jpg"/></li>
            <li><img class="imgsTwo" src="../assets/nginx.jpg"/></li>
            <li class="imgsTwo">更多>></li>
          </ul>
          <!--<tr class="secondtr">-->
            <!--<td><img class="imgsTwo" src="../assets/docker.jpg"/></td>-->
            <!--<td><img class="imgsTwo" src="../assets/django.jpg"/></td>-->
            <!--<td><img class="imgsTwo" src="../assets/nginx.jpg"/></td>-->
            <!--<td>更多>></td>-->
          <!--</tr>-->

        <!--</table>-->
      </div>
      <div class="articles">
        <div class="terms">
          <div class="objects" v-for="t in c">
            <div class="timeWaring">
              <span>最新更新时间</span>
              <span>{{t.time}}</span>
            </div>
            <!--<img class="imgThree" src="../assets/logo.png"/>-->
            <router-link class="objectsIterm" to="/content/articles">{{t.tittle}}</router-link>
          </div>
        </div>
        <div class="more" @click="getMore">加载更多...</div>
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
<style scoped>
    html, body{
        background:#fff;
    }
</style>
<style scoped>
.content{
        color:#211e1e;
        position: relative;
        float: left;
        width: 100%;
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
    width: 100%;

}
.titles li{
    width: 13%;
    display: -webkit-box;

}
.imgsTwo{
   width: 44px;
}
.terms{
  width: 100%;
  background: wheat;
  position: relative;
  float: left;
  margin-bottom: 100px;
}
.objects{
    margin: 10px;
    height: 76px;
    border-bottom: 1px solid silver;
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
    float: left;
    width: 74%;
    background: beige;
    margin-left: 16%;
    }
.url{
    border-bottom: 1px solid rebeccapurple;

}
.more{
    width: 80%;
    height: 18px;
    position: relative;
    float: left;
    margin-top: -92px;
    text-align: center;
}
.articles{
    background:black;
}
.timeWaring{
    font-size: 12px;
    padding: 10px;
}
@media(max-width:670px){
.imgStyle{
  display:none;
  height:100px;
  width:100%;
}
.imgsTwo{
   width: 30px;
   font-size: 10px;
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
      c:[{'tittle':'文章1','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章2','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章3','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章4','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章5','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章6','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章7','time':'2019-2-2','src':'../assets/logo.png'},
      {'tittle':'文章8','time':'2019-2-2','src':'../assets/logo.png'}],
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
          //$(this).animate({'marginTop':'-300px'})

        })


        },5000)
        //setInterObj

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
              $('.terms').append('<div class="append1"><div class="timeWarning1"><span>更新时间</span><span>'+this.c[i+allItems-1].time+'</span></div><div class="router-link" to="/content/articles">'+this.c[i+allItems-1].tittle+'</div></div>')
              $('.append1').css({'margin': '10px','border-bottom': '1px solid silver','height': '76px'})
              $('.timeWarning1').css({'font-size': '12px','padding': '10px'})
              $('.imgthree1').css({'width':'50px','border': '1px solid #575963','border-radius': '14px','height': '50px'})
              $('.router-link').css({'margin-top': '5px','display': 'block','position': 'relative','float': 'left','width': '74%','background': 'beige','margin-left': '16%'})
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
