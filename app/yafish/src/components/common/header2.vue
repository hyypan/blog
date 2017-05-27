<template>
    <div class="header">
      <div class="arrow" @click="leftAside">></div>
      <div class="arrow-t" @click="rightAside"><</div>

    </div>
</template>
<style scoped>
  .header{
    position: fixed;
    height: 75px;
    background: white;
    width: 100%;
    z-index: 10;
    text-align:center;
  }
  .arrow{
    width: 69px;
    background: rebeccapurple;
    height: 18px;
    font-size: 21px;
    font-weight: 800;
    position: relative;
    left: 0;
    top: 31px;
    display:none;
  }
   .arrow-t{
    position: relative;
    display:none;
    float: right;
    top: 21px;
    right: 14px;
    font-size: 21px;
  }
@media(max-width:1024px){
   .arrow-t{
    position: relative;
    display:block;
    float: right;
    top: 21px;
    right: 14px;
    font-size: 21px;
  }
  .arrow{
    width: 69px;
    background: rebeccapurple;
    height: 18px;
    font-size: 21px;
    font-weight: 800;
    position: relative;
    left: 0;
    top: 31px;
    display:block;
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
        components:{
        },
        methods:{
          leftAside:function(){
            var obj=$('.f-li').css('display')
            console.log('obj',obj)
            if(obj=='none'){
            $('.f-li').show(500)
            }else{
            $('.f-li').hide(500)
            }
          },
            rightAside:function(){
            var obj=$('.f3-li').css('display')
            console.log('obj',obj)
            if(obj=='none'){
            $('.f3-li').show()
            $('.f2-li').css({'width':'40%'})
            $('.icons').css({'display':'none'})

            }else{
            $('.f3-li').hide(function(){
            $('.icons').css({'display':'block'})

            })
            $('.f2-li').css({'width':'100%'})

            }
          }
        }
    }
</script>
