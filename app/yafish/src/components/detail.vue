<template>
    <div>
      <span @click="goback"><</span>
      <span>{{this.name}}</span>
    </div>
</template>
<style scoped>
    body{
        background-color:#ff0000;
    }
</style>
<script>
    export default{
        data(){
            return{
                msg:'hello vue',
                name: ''
            }
        },
        components:{
        },
        methods:{
        goback(){
        window.history.go(-1)
        }
        },
        created:function(){
          this.name=this.$route.params.name
        }

    }
</script>
