<template>
  <header>
    <div class="mid">
      <img class="hom" src="../../assets/home.png"/>
      <img class="potr" src="../../assets/pis.jpg"/>
    </div>
    <div class="zeroUl" >
      <ul class="zzul">
        <li>
          <ul class="ul-a">
            <li class=""><router-link to='/'>首页</router-link></li>
            <li class="" @click="goToHotest">最热文章</li>
            <li class="" @click="goToNewest">最新文章</li>
            <li class="" @click="goToOthers">其他</li>
          </ul>
        </li>
        <li>
          <ul class="ul-a">
            <li><img class="imgsTw" src="../../assets/python.png"/><span>python</span></li>
            <li><img class="imgsTw" src="../../assets/logo.png"/><span>vue</span></li>
            <li><img class="imgsTw" src="../../assets/linux.jpg"/><span>linux</span></li>
             <li><img class="imgsTw" src="../../assets/ansible.jpg"/><span>ansible</span></li>
          </ul>
        </li>
        <li>
          <ul class="ul-a">
            <li><img class="imgsTw" src="../../assets/docker.jpg"/><span>docker</span></li>
            <li><img class="imgsTw" src="../../assets/django.jpg"/><span>django</span></li>
            <li><img class="imgsTw" src="../../assets/nginx.jpg"/><span>nginx</span></li>
          </ul>
        </li>



      </ul>
    </div>




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
.zzul{
    list-style:none;
    padding: 0;
    height: 69px;
    display: -webkit-box;
    margin-left: -32px;
    margin-top: 0;
}
.zzul li{
    list-style:none;
}
.threeUl{
   position: relative;
    top: -68px;
    left: 89px;
    list-style:none;
}
.fourUl{
    position: relative;
    top: -136px;
    list-style:none;
    left: 181px;
}
li{
    margin: 5px;
}

.imgsTw{
    width: 10px;
    height: 10px;
}
.zeroUl{
    display:none;
    //background: #7b7979;
    background:#7b7979;
    position: relative;
    list-style:none;
    top: -44px;
    font-size: 10px;
    padding: 22px;
}
.mid{
    width: 80%;
    margin: 0 auto;
    display:none;
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
    border-bottom: 1px solid rgba(193, 193, 193, 0.5);
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
.mid{
    display:block;
    width: 80%;
    margin: 0 auto;
}
.zeroUl{
    display:none;
    //background: #7b7979;
    position: relative;
    top: -23px;
    font-size: 10px;
    padding: 22px;
    height: 61px;
    list-style:none;
}
.hom{
    display: -webkit-box;
    width: 29px;
    position: relative;
    top: 11px;
    left: 0;
}
.firstUl{
    display: none;
    list-style: none;
    width: 38%;
    color: #FF9800;
}
header{
    position: fixed;
    height: 55px;
    width: 100%;
    float: left;
    //background-image:url('https://onevcat.com//assets/images/background-cover.jpg');
    //background-repeat: no-repeat;
    //background-position: center;
   // background-size: cover;
    z-index: 20;
    background:#7b7979;
    border-bottom: 1px solid rgba(193, 193, 193, 0.5);
    top: 0;
    }
.potr{
    display: -webkit-box;
    width: 40px;
    position: relative;
    border-radius: 20px;
    top: -23px;
    left: 44%;
}
}

</style>
<script>
    export default{
        data(){
            return{
                msg:'hello vue',
                arr:[1,2]
            }
        },
        mounted:function(){
         console.log(this.arr)
        console.log($('.ul-a li'))
       Array.from($('.ul-a li')).forEach(function(value,index,array){
        $(value).click(function(value){
          name = $(value)[0].target.innerHTML
          router.push({name:'Detail', params:{'name':name}})

        })
        })
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
