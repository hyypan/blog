<template>
    <div>
      <header-components></header-components>
      <div>
        <ul class="f-ul">
          <li class="f-li">
            <ul>
              <li class="portrail">
                <div><img src="../assets/docker.jpg"/> </div>
                <div></div>
              </li>
              <li class="cenlender">
                <div class="mon-year-box">
                  <span class="down" @click="down"><</span>
                  <span class="year" v-model="year"></span>
                  <span class="">年</span>
                  <span class="mon" v-model="mon"></span>
                  <span class="">月</span>
                  <span class="day" v-model="day"></span>
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
              <li class="tags">
                <ul>
                  <li><div class="tags-d">Python(1)</div></li>
                  <li><div class="tags-d">Django(1)</div></li>
                  <li><div class="tags-d">Vue(1)</div></li>
                  <li><div class="tags-d">Webpack(1)</div></li>
                  <li><div class="tags-d">Ansible(1)</div></li>
                  <li><div class="tags-d">Docker(1)</div></li>
                  <li><div class="tags-d">Linux(1)</div></li>
                  <li><div class="tags-d">Git(1)</div></li>
                  <li><div class="tags-d">机器学习(1)</div></li>
                  <li><div class="tags-d">算法(1)</div></li>
                  <li><div class="tags-d">生活和感想(1)</div></li>
                  <li><div class="tags-d">游戏(1)</div></li>
                  <li><div class="tags-d">NBA(1)</div></li>
                  <li><div class="tags-d">PHP(1)</div></li>
                  <li><div class="tags-d">JavaScript(1)</div></li>
                  <li><div class="tags-d">Html(1)</div></li>

                </ul>
              </li>
            </ul>
          </li>
          <li class="f2-li" style="position: relative;left:-7px;">
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
              float:right;
              background: white;
              margin-top: 10px;">
            <div class="input-d"><input type="text"/></div>
            <ul class="search-ul">
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
    @media(max-width:1024px){
    .f-li{
      display:none;
    }
    }
    .search-ul{
        margin-left: 4px;
    }
    .input-d{
        margin: 40px;
    }
    .tags-d{
        background:#eeeeee;
        padding: 4px;

    }
    .up,.down{
        display: inline-block;
        width: 24px;
        background: #b5b9b3;
        text-align: center;
    }
    .up, .down:hover{
      cursor:pointer;
    }
    .days{
      width:188px;
    }
    .days li{
        list-style: none;
        display: inline-block;
        font-size: 10px;
        margin-left:12px;
        width:11px;
        margin-bottom: 17px;    }
    .days li:hover{
        text-decoration: underline;
    }
    .weeks{
        width: 200px;
    }
    .weeks li{
        list-style: none;
        display: inline-block;
        font-size: 13px;
        margin-left:10px;
    }
    .mon-year-box{
        background: white;
    }
    .mon-year-box span{
        margin-left: 3px;
    }
    .tags{
    background: white;
    margin-top: 8px;
    height: 289px;
    }
    .tags li{
        list-style: none;
        display: inline-block;
        margin: 6px;
        font-size: 12px;
    }
    .cenlender{
        background: white;
        margin-top: 24px;
        height: 229px;
        padding-top: 7px;
        padding-left: 5px;
    }
    .portrail{
    background: rgb(238, 238, 238);
    margin-top: 1px;
    height: 208px;
    }
    .portrail img{
        width: 90px;
        height: 90px;
        border: 1px solid silver;
        border-radius: 45px;
        position: relative;
        left: 69px;
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
      width:245px;
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
                year:'',
                mon:'',
                day:'',
                setInter:'',
                list:[],
                img: require('../assets/bg1.jpeg'),
                runningImg:[require('../assets/bg1.jpeg'), require('../assets/bg2.jpeg'), require('../assets/bg.jpg'),require('../assets/linux.jpg')],
                articles:[
                {'src': require('../assets/bg1.jpeg'),'title': '文章标题1', 'content': '文章内容1','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/bg2.jpeg'),'title': '文章标题2', 'content': '文章内容2','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/bg.jpg'),'title': '文章标题3', 'content': '文章内容3','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/linux.jpg'),'title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/linux.jpg'),'title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/linux.jpg'),'title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},
                {'src': require('../assets/linux.jpg'),'title': '文章标题4', 'content': '文章内容4','readTimes':'10', 'goodClick':'100', 'commends':'10','time':'2017.2.2'},

                ]
            }
        },
        components:{
            FooterComponents,HeaderComponents,
        },
        watch: {
        mon:function(val, oldVal){
         //计算对应的星期和日期
         var year=$('.year').html()
         var mon=$('.mon').html()
         var mon2=mon
         var day=$('.day').html()
         //这里是为了重置日期
         if(mon=='12'){
            mon=0
         }else{
          mon=Number(mon)-1
         }

         var date=new Date()
         date.setFullYear(year,mon,1)
         console.log('setdate',date)
         var weekDay= date.getDay()
         if(weekDay==0){
         weekDay=7
         }
         console.log('mon2',weekDay)
         //判断瑞年
         var learYear=function(inYear){
          if((Number(inYear)%400)==0){
            return true
            //alert(1)
         }else{
          if((Number(inYear)%100)==0){
            return false
          }else if(Number(inYear)%4==0){
            return true
          }else{
            return false
          }
          }
         }
         var regExp=/11|[4|6|9]/
         var maxNum=28
          if(regExp.test(mon2)){
          maxNum=30
          }else if(learYear(year) && mon2=='2'){
          maxNum=29
          }else if(mon2!='2'){
          maxNum=31
          }
          console.log('mamm', maxNum)
          for(var j=weekDay;j>0;j--){
            if(regExp.test(mon2-1)){
            $('.days li').eq(j-1).html(31-weekDay+j)
            }else if(mon2=='3' && learYear(year)){
             $('.days li').eq(j-1).html(30-weekDay+j)

            }else if(mon2=='3' && !learYear(year)){
             $('.days li').eq(j-1).html(29-weekDay+j)

            }else{
             $('.days li').eq(j-1).html(32-weekDay+j)

            }
          }
          for(var i=0;i<=35;i++){
            if(i>maxNum){
             $('.days li').eq(i+weekDay-2).html(i-maxNum)
             $('.days li').eq(i+weekDay-2).css({'color':'#bbb9b9'})
            }else{
             $('.days li').eq(weekDay-1+i).html(i+1)
             $('.days li').eq(i+weekDay-1).css({'color':'black'})
             if(i==0){
             for(var k=0;k<weekDay;k++){
              $('.days li').eq(weekDay-k-2).css({'color':'#bbb9b9'})
             }
             }
            }

          }
          }
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

            that.setInter = setInterval(run,4000)
          $('.running-images').mouseenter(function(){
            console.log('clear',1)
            clearInterval(that.setInter)
          })
          $('.running-images').mouseleave(function(){
            that.setInter = setInterval(run,4000)
            console.log('set')
          })
          //日历计算1
          var dateToday=new Date()
          console.log(dateToday.toLocaleDateString())
          $('.year').html(dateToday.getFullYear())
          $('.mon').html(Number(dateToday.getMonth())+Number(1))
          $('.day').html(dateToday.getDate())

         //计算对应的星期和日期
         var year=$('.year').html()
         var mon=$('.mon').html()
         var mon2=mon
         var day=$('.day').html()
         //这里是为了重置日期
         if(mon=='12'){
            mon=0
         }else{
          mon=Number(mon)-1
         }

         var date=new Date()
         date.setFullYear(year,mon,1)
         console.log('setdate',date)
         var weekDay= date.getDay()
         if(weekDay==0){
         weekDay=7
         }
         console.log('mon2',weekDay)
         $('.days li').eq(weekDay-1).html(1)
         $('.days li').eq(day-1).css({'text-decoration': 'underline'})
         //判断瑞年

         var learYear=function(inYear){
          if((Number(inYear)%400)==0){
            return true
         }else{
          if((Number(inYear)%100)==0){
            return false
          }else if(Number(inYear)%4==0){
            return true
          }else{
            return false
          }
          }
         }

         var regExp=/11|[4|6|9]/
         var maxNum=28
          if(regExp.test(mon2)){
          maxNum=30
          }else if(learYear(year) && mon2=='2'){
          maxNum=29
          }else if(!learYear(year) && mon2=='2'){
          maxNum=28
          }else{
          maxNum=31
          }
          for(var j=weekDay;j>0;j--){
            if(regExp.test(mon2-1)){
            $('.days li').eq(j-1).html(31-weekDay+j)

            }else if(mon2=='3' && learYear(year)){
             $('.days li').eq(j-1).html(30-weekDay+j)

            }else if(mon2=='3' && !learYear(year)){
             $('.days li').eq(j-1).html(29-weekDay+j)
            }else{
             $('.days li').eq(j-1).html(32-weekDay+j)

            }
          }
          for(var i=0;i<=35;i++){
            if(i>maxNum){
             $('.days li').eq(i+weekDay-2).html(i-maxNum)
             $('.days li').eq(i+weekDay-2).css({'color':'#bbb9b9'})

            }else{
             $('.days li').eq(weekDay-1+i).html(i+1)
             $('.days li').eq(i+weekDay-1).css({'color':'black'})
             if(i==0){
             for(var k=0;k<weekDay;k++){
              $('.days li').eq(weekDay-k-2).css({'color':'#bbb9b9'})
             }
             }
            }

          }
        },
        methods:{
            up:function(){
              var mon=$('.mon').html()
              var year=$('.year').html()
              if(Number(mon)<12){
                mon=Number(mon)+1
                $('.mon').html(mon)
                this.mon=mon
              }else{
                $('.mon').html(1)
                this.mon=1
                $('.year').html(Number(year)+1)
                this.year=Number(year)+1
              }

            },
            down:function(){
              var mon=$('.mon').html()
              var year=$('.year').html()
              if(Number(mon)==1){
                mon=12
                this.mon=12
                $('.mon').html(mon)
                $('.year').html(Number(year)-1)
                this.year=Number(year)-1

              }else{
                $('.mon').html(Number(mon)-1)
                this.mon=Number(mon)-1
              }

            }
        }
    }
</script>
