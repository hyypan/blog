<template>
  <header>
    <ul>
      <li>python</li>
      <li>vue</li>
      <li>linux</li>
      <li>其他</li>
      <li>
        <div class="secondLine">
          <span class="inputLeft">搜索</span>
          <input class="search" @click="inputClick"/>
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
    border-bottom: 1px solid hsla(0, 0%, 76%, 0.3)
    }
ul{
    display: -webkit-inline-box;
    list-style: none;
}
ul li{
    margin-left: 50px;
    font-size: 23px;
    margin-top: 20px;
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
}
.search{
    display: block;
    margin-left: 153px;
    margin-top: -42px;
    height: 38px;
    border: 1px solid #c1c1c1;
    border-left:none;
    border-right: none;
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
}
.inputReft img{
  width:36px;
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
        document.getElementsByClassName('search')[0].addEventListener('focusout',function(){

        $('.inputReft img').animate({'margin-left':'0px'})
        $('.inputReft').animate({'width':'40px'})
        })

        },


        methods:{
        inputClick:function(){
        //document.getElementsByClassName('inputReft')[0].style.width='71px';
        $('.inputReft img').animate({'margin-left':'30px'})
        $('.inputReft').animate({'width':'71px'})
        },
        blur:function(){
        alert(1)
        }
        }

    }
</script>
