<template>
    <div class="header">
      <div class="arrow" @click="leftAside">></div>
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
@media(max-width:1024px){
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
            $('.f-li').show()
            }else{
            $('.f-li').hide()
            }
          }
        }
    }
</script>
