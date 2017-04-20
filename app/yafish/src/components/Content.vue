<template>
<div>
  <header-components></header-components>
  <div class="content">这里写主题内容</div>
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
        background:yellow;
        position: relative;
        float: left;
        width: 100%;
        height: 500px;
        /* margin: 90px; */
        margin-top: 90px;
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
