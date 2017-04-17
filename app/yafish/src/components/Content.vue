<template>
<div class="div">{{msg}}</div>
</template>
<style>
    html, body{
        background:#fff;
    }
</style>
<style scoped>
    .div{
        color:red;
        background:yellow;
    }
</style>
<script>
export default{
  data () {
    return {
      msg: '正在开发中'
    }
  }
}
</script>
