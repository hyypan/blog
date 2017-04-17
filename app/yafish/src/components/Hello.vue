<template>
  <div class="content">
    <div class="list">这个地方放目录</div>
    <div class="listRight">这个地方是目录显示出来的内容</div>
    <div class="listBottom">这里放另一部分内容</div>
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
    text-align: center;
    -ms-transform:rotate(-5deg); 	/* IE 9 */
    -moz-transform:rotate(-5deg); 	/* Firefox */
    -webkit-transform:rotate(-5deg); /* Safari 和 Chrome */
    -o-transform:rotate(-5deg); 	/* Opera */
    height: 400px;
    width: 20%;
    background: beige;
    border-right: 1px solid silver;
    position: relative;
    float: left;
    margin-top:6%;
    padding-top: 17px;
}
.listRight{
    -ms-transform:rotate(2deg); 	/* IE 9 */
    -moz-transform:rotate(2deg); 	/* Firefox */
    -webkit-transform:rotate(2deg); /* Safari 和 Chrome */
    -o-transform:rotate(2deg); 	/* Opera */
    background: beige;
    width: 66%;
    position: relative;
    float: left;
    margin: 10 auto;
    left: 83px;
    height: 400px;
    margin-top: 6%;
    padding:17px;
}


</style>
