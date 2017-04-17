<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style scope>
html, body{
  background:red;
  height:100%;
  margin:0;
  padding:0;

}
#app {
    height:100%;
}
/*
.navi{
    width: 100%;
    height: 10%;
    //background: beige;
}
.footer{
    width: 100%;
    height:10%;
    //background: beige;
}
*/
</style>
