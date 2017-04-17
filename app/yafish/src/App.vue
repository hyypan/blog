<template>
  <div id="app">
    <div class="navi">header</div>
    <router-view></router-view>
    <div class="footer">footer</div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
html, body{
  background:red;
  height:100%;
  margin:0;
  padding:0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
    height:100%;

}
.navi{
    width: 100%;
    height: 15%;
    background: burlywood;
}
.footer{
    width: 100%;
    height:25%;
    background: black;
}

</style>
