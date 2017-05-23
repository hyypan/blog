<template>
    <div>
      <header-components></header-components>
      <div>
        <ul class="f-ul">
          <li class="f-li">
            <ul>
              <li>1</li>
              <li>12</li>
              <li>13</li>
              <li>14</li>
              <li>15</li>
            </ul>
          </li>
          <li class="f2-li">
            <div class="running-images" >
              <ul>
              <li v-model="runningImg" v-for="r in runningImg">
                <img :src="r"/>
              </li>
              </ul>
            </div>
            <ul class="t-ul">
              <li v-model="articles" v-for="a in articles" class="article-li">
                <img class="a-img" :src="a.src"/>
                <div class="t-article">
                  <p>{{a.title}}</p>
                  <p>{{a.content}}</p>
                  <div>
                    <ul class="four-ul">
                      <li><img src="../assets/clock.png"/><span>{{a.time}}</span></li>
                      <li><img src="../assets/eyes.png"/><span>{{a.readTimes}}</span></li>
                      <li><img src="../assets/commds.png"/><span>{{a.commends}}</span></li>
                      <li><img src="../assets/good.png"/><span>{{a.goodClick}}</span></li>

                    </ul>
                  </div>
                </div>
              </li>
            </ul>
          </li>
          <li class="f-li">
            <div>这里放一些搜索</div>
            <ul>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
            </ul>
            <div>这里放日历</div>
            <div>这里放标签</div>
          </li>
        </ul>
      </div>
      <footer-components></footer-components>
    </div>
</template>
<style scoped>
    body{
        background-color:#ff0000;
    }
    .four-ul{
        list-style: none;
        display: -webkit-inline-box;
    }
    .four-ul li:first-child{
        margin-left:0;
    }
    .four-ul li{
        margin-left: 40px;
    }
    .four-ul img{
        width:16px;
    }
    .four-ul span{
        font-size:10px;
    }
    .article-li{
        height: 100px;
        padding: 8px;
        background: white;
        margin: 15px;
    }
    .t-article{
        position: relative;
        top: -109px;
        left: 124px;
        width: 76%;
    }
    .f-ul{
        display: -webkit-inline-box;
        width: 100%;
        background: #eee;
        margin: 0;
    }
    .f-li{
      width:15%;
      background:sliver;
    }
    .f2-li{
      width:60%;

    }
    .running-images{
       position: relative;
       height: 250px;
       background: #fff;
      /* padding: 23px; */
       margin: 11px;
       list-style: none;
    }
    .a-img{
       width: 120px;
       height: 100px;
    }
    .t-ul{
      padding-left:0;
    }
    li{
      list-style:none;
    }
</style>

<script>
import HeaderComponents from './common/header2'
import FooterComponents from './common/footer'
    export default{
        data(){
            return{
                runningImg:['../assets/bg1.jpeg', '../assets/bg2.jpeg', '../assets/bg2.jpeg'],
                articles:[
                {'src': '../assets/bg1.jpeg','title': '文章标题1', 'content': '文章内容1','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': '../assets/bg2.jpeg','title': '文章标题2', 'content': '文章内容2','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': '../assets/bg.jpg','title': '文章标题3', 'content': '文章内容3','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': '../assets/linux.jpg','title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                ]
            }
        },
        components:{
            FooterComponents,HeaderComponents,
        }
    }
</script>
