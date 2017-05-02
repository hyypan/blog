<template>
    <div class="notFound"></div>
</template>
<style scoped>
.notFound{
  background:url(../../assets/404.jpg);
    background-repeat: no-repeat;
    width: 100%;
    height: 100%;
    background-position: center;
    background-size: cover;
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
