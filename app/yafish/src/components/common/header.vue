<template>
  <header>
    <img class="hom" src="../../assets/home.png"/>
    <img class="potr" src="../../assets/pis.jpg"/>
    <ul class="zeroUl">
      <li class=""><router-link to='/'>首页</router-link></li>
      <li class="" @click="goToHotest">最热文章</li>
      <li class="" @click="goToNewest">最新文章</li>
      <li class="" @click="goToOthers">其他</li>
    </ul>
    <ul class="firstUl">
      <li class="liPre"><router-link to='/'>首页</router-link></li>
      <li class="liPre" @click="goToHotest">最热文章</li>
      <li class="liPre" @click="goToNewest">最新文章</li>
      <li class="liPre" @click="goToOthers">其他</li>
      <li><div class="left-r"></div><input class="search" placeholder="搜索"/><div class="input-r"><img src="../../assets/search.png"></img></div></li>
      <!--<li class="lastli">-->
        <!--<div class="secondLine">-->
          <!--<span class="inputLeft"></span>-->
          <!--<input class="search" @click="inputClick" placeholder="搜索"/>-->
          <!--<div class="inputReft"><img src="../../assets/search.png"></img></div>-->
        <!--</div>-->
      <!--</li>-->

    </ul>
    <ul class="secUl">
      <li>登录</li>
      <li>注册</li>
    </ul>

  </header>
</template>
<style scoped>
.zeroUl{
    display:none;
    background: #7b7979;
    position: relative;
    top: -44px;
    font-size: 10px;
    padding: 22px;
}
.potr{
    display:none;
    width: 40px;
    position: relative;
    border-radius: 20px;
    left: 118px;
    top: 4px;
}
.input-r{
    height: 26px;
    position: relative;
    left: 143px;
    width: 18px;
    top: -51px;
    display: block;
    border: 1px solid #c1c1c1;
    border-left: none;
    border-bottom-right-radius: 13px;
    border-top-right-radius: 13px;
    background: #c1c1c1;
}
.input-r img{
    margin-left: 0px;
    width: 19px;
    position: relative;
    top: 3px;

}
.search{
    top: -23px;
    position: relative;
    left: 13px;
    height: 24px;
    border: 1px solid #c1c1c1;
}
.left-r{
    width: 14px;
    height: 26px;
    border:1px solid #c1c1c1;
    border-bottom-left-radius: 13px;
    border-top-left-radius: 13px;
    position: relative;
    top: 5px;
    background:#c1c1c1;
}
.secUl{
    position: relative;
    float: right;
    margin-right: -220px;
    top: 34px;

}
.secUl li{
     margin-left: 35px;


}


header{
    position: fixed;
    height: 90px;
    width: 100%;
    float: left;
    background: #ffffff;
    z-index: 20;
    border-bottom: 1px solid black;
    top: 0;
    }
.firstUl{
    display: -webkit-inline-box;
    list-style: none;
    width: 38%;
    color: #FF9800;
}
.firstUl li{
    font-size: 18px;
    margin-top: 20px;
}
.firstUl li:first-child{
  //visibility:hidden;
      margin-left: 102px;
}
.inputLeft{
    font-size: 10px;
    height: 26px;
    width: 25px;
    display: block;
    background: white;
    border: 1px solid #c1c1c1;
    padding-top: 14px;
    margin-top: -4px;
    margin-left: 123px;
    border-radius: no;
    border-right: none;
    border-top-left-radius: 23px;
    border-bottom-left-radius: 23px;
    padding-left: 4px;
    background: #c1c1c1;
}
.sdearch{
    display: block;
    margin-left: 153px;
    margin-top: -42px;
    height: 38px;
    border: 1px solid #c1c1c1;
    border-left:none;
    border-right: none;
    background: #c1c1c1;
    font-size: 14px;
}
.search:focus{
    //outline: -webkit-focus-ring-color auto 1px;
    outline-color: #c1c1c1;
    outline-style: none;
    outline-width: 1px;

}
.inputReft{
    height: 40px;
    margin-left: 281px;
    margin-top: -42px;
    display: block;
    border: 1px solid #c1c1c1;
    border-left: none;
    border-bottom-right-radius: 23px;
    border-top-right-radius: 23px;
    background: #c1c1c1;
}
.inputReft img{
  width:36px;
}
.liPre:hover{
  color:red;
}
.liPre{
    padding-top: 7px;
    width: 106px;
    text-align:center;

}
.home{
    width:163px;
    position: relative;
    float: left;
    margin-top: 41px;
}
.hom{
    display:none;
    width: 29px;
    position: relative;
    top: 11px;
    left: 26px;
}
@media(max-width:670px){
.zeroUl{
    display:none;
    background: #7b7979;
    position: relative;
    top: -31px;
    font-size: 10px;
    padding: 22px;
}
.hom{
    display: -webkit-box;
    width: 29px;
    position: relative;
    top: 11px;
    left: 26px;
}
.firstUl{
    display: none;
    list-style: none;
    width: 38%;
    color: #FF9800;
}
header{
    position: fixed;
    height: 50px;
    width: 100%;
    float: left;
    background: #7b7979;
    z-index: 20;
    border-bottom: 1px solid #7b7979;
    top: 0;
    }
.potr{
    display: -webkit-box;
    width: 40px;
    position: relative;
    border-radius: 20px;
    left: 140px;
    top: -23px;
}
}
/*@media(max-width:670px){
ul{
    display: none;
    list-style: none;
    width: 12%;
    padding:6px;
    background: #d2caca;
    margin-left: 83px;
    top: -5px;
    margin-left: 170px;
    margin-top: 31px;
    font-size: 10px;
    height: 105px;
}
li:first-child{
  visibility:visible;
}
.hom{
    display:block;
    width: 29px;
    position: relative;
    top: 32px;
}
.lastli{
  visibility:hidden;
}
ul li{
    margin-top: 6px;
    font-size: 11px;
}
.liPre{
    padding-top: 7px;
    text-align:center;
    width: 67px;


}
}*/
</style>
<script>
    export default{
        data(){
            return{
                msg:'hello vue'
            }
        },
        mounted:function(){
        document.getElementsByTagName('body')[0].addEventListener('mouseover',function(){
        if($(this).clientWidth>670){
            $('ul').show()
        }
        })
        document.getElementsByClassName('search')[0].addEventListener('focusout',function(){

        $('.inputReft img').animate({'margin-left':'0px'})
        $('.inputReft').animate({'width':'40px'})
        }),
        document.getElementsByClassName('hom')[0].addEventListener('click',function(){
        console.log('111',document.getElementsByClassName('zeroUl')[0].hidden)
        if(document.getElementsByClassName('zeroUl')[0].style.display=='none'||document.getElementsByClassName('zeroUl')[0].style.display==''){
           $('.zeroUl').show()
           document.getElementsByClassName('contentCenter')[0].style.top='52px'
        }else{
         $('.zeroUl').hide()
         document.getElementsByClassName('contentCenter')[0].style.top='-40px'
        }
        })
        document.getElementsByTagName('ul')[0].addEventListener('mouseleave',function(){

          if(document.getElementsByTagName('body')[0].clientWidth<670){
              $(this).hide()
            }else{
              $(this).show()
            }
        })
        },


        methods:{
        inputClick:function(){
        $('.inputReft img').animate({'margin-left':'30px'})
        $('.inputReft').animate({'width':'71px'})
        },
        goToHotest: function(){
          router.push({name:'hotest'})
        },
        goToNewest: function(){
          router.push({name:'newest'})

        },
        goToOthers: function(){
          router.push({name:'others'})

        }
        },

    }
</script>
