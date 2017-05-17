<template>
    <div>
      {{this.name}}
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
        created:function(){
          this.name=this.$route.params.name
        }

    }
</script>
