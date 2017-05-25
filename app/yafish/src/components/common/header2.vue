<template>
    <div class="header">这里是header</div>
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

</style>
<script>
    export default{
        data(){
            return{
                msg:'hello vue'
            }
        },
        components:{
        }
    }
</script>
