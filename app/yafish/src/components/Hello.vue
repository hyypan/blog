<template>
  <div class="hello">
    <div class="navi">
      <div class="navi-img"><img src="../assets/python.png"/><h1>python</h1></div>
    </div>
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
<style>
html, body{
        background:red;
    }
</style>
<style scoped>
.navi{
    width: 100%;
    height: 68px;
    background: white;
    position: fixed;
    margin-top: 4px;
    border-bottom: 1px solid rgba(51, 48, 48, 0.11);
}
.navi-img img{
    width: 90px;
    position: relative;
    float: left;
    margin-top: -19px;
    margin-left: 24px;
}
</style>
