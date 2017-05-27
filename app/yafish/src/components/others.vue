<template>
    <div>
        <div>这是其他文章
          <div class="a" >111</div>
          <div @click="a">222</div>
        </div>
    </div>
</template>
<style scoped>
  .a{
          transition-duration: 1s;
       -moz-transition-duration: 1s; /* Firefox 4 */
       -webkit-transition-duration: 1s; /* Safari 和 Chrome */
       -o-transition-duration: 1s; /* Opera */
      width: 200px;
    height: 100px;
    background: rebeccapurple;
  }
  @media(max-width:1024px){
  .a{
   display:none;

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
        a:function(){
                  $('.a').css({'width':'0px'})
        $('.a').show(function(){
          $('.a').css({'width':'200px'})
        })
        }



        }
    }
</script>
