<template>
  <header>
    <ul>
      <li>python</li>
      <li>vue</li>
      <li>linux</li>
      <li>其他</li>
      <li>
        <div class="secondLine">
          <span class="inputLeft">搜索</span>
          <input class="search"/>
          <img class="inputReft" src="../../assets/search.png"></img>
        </div>
      </li>

    </ul>
  </header>
</template>
<style scoped>
header{
    position: fixed;
    height: 90px;
    width: 100%;
    float: left;
    background: #ffffff;
    z-index: 20;
    border-bottom: 1px solid hsla(0, 0%, 76%, 0.3)
    }
ul{
    display: -webkit-inline-box;
    list-style: none;
}
ul li{
    margin-left: 50px;
    font-size: 23px;
    margin-top: 37px;
}
.inputLeft{
    font-size: 10px;
    height: 26px;
    width: 25px;
    display: block;
    background: white;
    border: 1px solid rebeccapurple;
    padding-top: 14px;
    margin-top: -17px;
    margin-left: 123px;
    border-radius: no;
    border-right: none;
    border-top-left-radius: 23px;
    border-bottom-left-radius: 23px;
    padding-left: 4px;
}
.search{
    display: block;
    margin-left: 153px;
    margin-top: -42px;
    height: 38px;
    border: 1px solid rebeccapurple;
    border-bottom-right-radius: 23px;
    border-top-right-radius: 23px;
}
.inputReft{
    width: 25px;
    margin-left: 250px;
    margin-top: -33px;
    display: block;
}
</style>
<script>
    export default{
        data(){
            return{
                msg:'hello vue'
            }
        },

    }
</script>
