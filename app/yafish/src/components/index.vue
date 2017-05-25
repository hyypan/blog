<template>
    <div>
      <header-components></header-components>
      <div>
        <ul class="f-ul">
          <li class="f-li" style="position:fixed;">
            <ul>
              <li class="portrail">这里放头像</li>
              <li class="cenlender">
                <div class="mon-year-box">
                  <span class="down" @click="down"><</span>
                  <span class="year"></span>
                  <span class="">年</span>
                  <span class="mon"></span>
                  <span class="">月</span>
                  <span class="day"></span>
                  <span class="">日</span>
                  <span class="up" @click="up">></span>
                </div>
                <ul class="weeks">
                  <li>一</li>
                  <li>二</li>
                  <li>三</li>
                  <li>四</li>
                  <li>五</li>
                  <li>六</li>
                  <li>日</li>
                </ul>
                <ul class="days">
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                  <li>11</li>
                </ul>
              </li>
              <li class="tags">这里放标签</li>
            </ul>
          </li>
          <li class="f2-li" style="position: relative;left: 20%;">
            <div class="running-images">
              <ul>
              <li v-model="runningImg" v-for="r in runningImg" class="run-li">
                <img :src="r" class="big-img"/>
              </li>
              </ul>
              <div class="circle" >
                <div v-for="r in runningImg" class="yuan"></div>
              </div>
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
          <li class="f-li" style="position: relative;
              margin-left: 21%;
              background: white;
              margin-top: 10px;">
            <div>这里放一些搜索</div>
            <ul>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
              <li>搜索列表</li>
            </ul>
            <div>这里预留位置1</div>
            <div>这里预留位置2</div>
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
    .days li{
        list-style: none;
        display: inline-block;
        font-size: 10px;
        margin-left:10px;
    }
    .weeks li{
        list-style: none;
        display: inline-block;
        font-size: 10px;
        margin-left:10px;
    }
    .mon-year-box{
        background: #b5b9b3;
    }
    .mon-year-box span{
        margin-left: 5px;
    }
    .tags{
        background: white;
        margin-top: 24px;
        height: 229px;
    }
    .cenlender{
        background: white;
        margin-top: 24px;
        height: 229px;

    }
    .portrail{
    background: white;
    margin-top: 1px;
    height: 111px;
    }
    .circle{
        position: absolute;
    /* margin: auto; */
        margin-left: 30%;
        top: 90%;

    }
    .yuan{
    position: relative;
    float: left;
    margin-left: 20px;
    width: 10px;
    height: 10px;
    background: white;
    border-radius: 5px;
    }
    .big-img{
        transition-duration: 1s;
       -moz-transition-duration: 1s; /* Firefox 4 */
       -webkit-transition-duration: 1s; /* Safari 和 Chrome */
       -o-transition-duration: 1s; /* Opera */
        height: 250px;
        width: 100%;
    }
    .big-img:hover{
       transform:rotate(0deg) scale(1.1);
      -ms-transform:rotate(0deg) scale(1.1); /* Internet Explorer */
      -moz-transform:rotate(0deg) scale(1.1); /* Firefox */
      -webkit-transform:rotate(0deg) scale(1.1); /* Safari 和 Chrome */
      -o-transform:rotate(0deg) scale(1.1); /* Opera */
    }
    .running-images ul{
        padding:0;
    }
    .running-images li{
        display:inline;
        width:100%;
        position:absolute;
        left:630px;
    }
    .running-images li:first-child{
        left:0;
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
        padding:0;
        margin-top:73px;
    }
    .f-li{
      width:20%;
      background:sliver;
    }
    .f-li ul{
      padding:10px;
    }
    .f2-li{
      width:652px;

    }
    .running-images{
       position: relative;
       height: 250px;
       background: #fff;
       margin: 11px;
       list-style: none;
       overflow:hidden;

    }
    .a-img{
       transition-duration: 1s;
       -moz-transition-duration: 1s; /* Firefox 4 */
       -webkit-transition-duration: 1s; /* Safari 和 Chrome */
       -o-transition-duration: 1s; /* Opera */
       width: 120px;
       height: 100px;
    }
    .a-img:hover{
      transform:rotate(5deg) scale(1.1);
      -ms-transform:rotate(5deg) scale(1.1); /* Internet Explorer */
      -moz-transform:rotate(5deg) scale(1.1); /* Firefox */
      -webkit-transform:rotate(5deg) scale(1.1); /* Safari 和 Chrome */
      -o-transform:rotate(5deg) scale(1.1); /* Opera */
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
                setInter:'',
                list:[],
                img: require('../assets/bg1.jpeg'),
                runningImg:[require('../assets/bg1.jpeg'), require('../assets/bg2.jpeg'), require('../assets/bg.jpg'),require('../assets/linux.jpg')],
                articles:[
                {'src': require('../assets/bg1.jpeg'),'title': '文章标题1', 'content': '文章内容1','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/bg2.jpeg'),'title': '文章标题2', 'content': '文章内容2','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/bg.jpg'),'title': '文章标题3', 'content': '文章内容3','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/linux.jpg'),'title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                ]
            }
        },
        components:{
            FooterComponents,HeaderComponents,
        },
        mounted:function(){
            let that=this
            var run=function(){
             if(that.list.length==3){
              $('.run-li:eq(0)').animate({'left':'-300px'},500,function(){
              $('.yuan:eq(3)').css({'background':'#1cce10'}).siblings().css({'background':'white'})
              var li=$(this)
              $(this).remove()
              that.list.push(li)
            console.log('bbb',that.list.length)
            if(that.list.length>=4){
                that.list.forEach(function(currentValue,index,array){
                    if(index==0){
                    $(currentValue).animate({'left':0},200)
                    $('.running-images ul').append(currentValue)
                    }else{
                    $(currentValue).animate({'left':'630px'},200)
                    $('.running-images ul').append(currentValue)
                    }
                })
                that.list=[]
            }
            })
             }else{
            $('.run-li:eq(0)').animate({'left':'-764px'},1000,function(){
              var li=$(this)
              $(this).remove()
              that.list.push(li)
            console.log('bbb',that.list.length)
            if(that.list.length>=4){
                that.list.forEach(function(currentValue,index,array){
                    if(index==0){
                    $(currentValue).animate({'left':0},200)
                    $('.running-images ul').append(currentValue)
                    }else{
                    $(currentValue).animate({'left':'630px'},200)
                    $('.running-images ul').append(currentValue)
                    }
                })
                that.list=[]
            }
            })
            $('.run-li:eq(1)').animate({'left':0},500)}

        }
            //that.setInter = setInterval(run,4000)
          $('.running-images').mouseenter(function(){
            console.log('clear',1)
            //clearInterval(that.setInter)
          })
          $('.running-images').mouseleave(function(){
            //that.setInter = setInterval(run,4000)
            console.log('set')
          })
          //日历计算
          var dateToday=new Date()
          console.log(dateToday.toLocaleDateString())
          $('.year').html(dateToday.getFullYear())
          $('.mon').html(Number(dateToday.getMonth())+Number(1))
          $('.day').html(dateToday.getDate())


        },
        methods:{
            up:function(){
              var mon=$('.mon').html()
              var year=$('.year').html()
              if(Number(mon)<12){
                mon=Number(mon)+1
                $('.mon').html(mon)
              }else{
                $('.mon').html(1)
                $('.year').html(Number(year)+1)
              }

            },
            down:function(){
              var mon=$('.mon').html()
              var year=$('.year').html()
              if(Number(mon)==1){
                mon=12
                $('.mon').html(mon)
                $('.year').html(Number(year)-1)

              }else{
                $('.mon').html(Number(mon)-1)
              }

            }
        }
    }
</script>
