<template>
  <header>
    <!--<div><img src="../../assets/yanglogo.png"/> </div>-->
    <img class="hom" src="../../assets/home.png"/>
    <ul>
      <li class="liPre"><router-link to='/'>首页</router-link></li>
      <li class="liPre" @click="goToHotest">最热文章</li>
      <li class="liPre" @click="goToNewest">最新文章</li>
      <li class="liPre" @click="goToOthers">其他</li>
      <li class="lastli">
        <div class="secondLine">
          <span class="inputLeft"></span>
          <input class="search" @click="inputClick" placeholder="搜索"/>
          <div class="inputReft"><img src="../../assets/search.png"></img></div>
        </div>
      </li>

    </ul>
  </header>
</template>
<style scoped>
header{
    position: fixed;
    height: 90px;
    width: 100%;
    float: left;
    background: #ffffff;
    z-index: 20;
    border-bottom: 1px solid #ece0ce;
    top: 0;
    }
ul{
    display: -webkit-inline-box;
    list-style: none;
    width: 38%;
    color: #FF9800;
}
ul li{
    font-size: 18px;
    margin-top: 20px;
}
li:first-child{
  visibility:hidden;
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
.search{
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
  background:#c1c1c1;
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
    top: 32px;
}
@media(min-width:670px){
ul{
    display: -webkit-inline-box;
    list-style: none;
    width: 38%;
    color: #FF9800;
}
}
@media(max-width:670px){
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
}
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
        alert(1)
            $('ul').show()
        }
        })
        document.getElementsByClassName('search')[0].addEventListener('focusout',function(){

        $('.inputReft img').animate({'margin-left':'0px'})
        $('.inputReft').animate({'width':'40px'})
        }),
        document.getElementsByClassName('hom')[0].addEventListener('mouseover',function(){
        $('ul').show()
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
