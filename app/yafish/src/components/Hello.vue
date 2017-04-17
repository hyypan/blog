<template>
  <div class="content">
    <div class="list">这个地方放目录</div>
    <div class="listRight">这个地方是目录显示出来的内容</div>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created: function () {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.content{
    height:80%;
}
.list{
    height: 100%;
    width: 20%;
    background: beige;
    border-right: 1px solid silver;
    position: relative;
    float: left;
    margin-top:6%;
}
.listRight{
    background: beige;
    width: 76%;
    position: relative;
    float: left;
    margin: 10 auto;
    top: 10px;
    left: 10px;
    height: 95%;
    margin-top:6%;
}


</style>
