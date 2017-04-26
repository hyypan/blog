<template>
<div>
  <header-components></header-components>
  <div class="content">
    <div class="contentCenter">
      <div class="banner">banner</div>
      <div>words</div>
    </div>
  </div>
  <footer-components></footer-components>
</div>
</template>
<style>
    html, body{
        background:#fff;
    }
</style>
<style scoped>
.content{
        color:red;
        position: relative;
        float: left;
        width: 100%;
        height: 500px;
        /* margin: 90px; */
        margin-top: 90px;
}
.contentCenter{
    background: rebeccapurple;
    width: 75%;
    margin: 0 auto;
    height: 100%;
}
.banner{
    width: 100%;
    background: wheat;
    height: 34%;
}

</style>
<script>
import HeaderComponents from './common/header'
import FooterComponents from './common/footer'
export default{
  data () {
    return {
      msg: '正在开发中'
    }
  },
    mounted: function(){

    },
    components:{
    FooterComponents,HeaderComponents,
    },

    methods: {

    },
    created: function(){

    }
}
</script>
