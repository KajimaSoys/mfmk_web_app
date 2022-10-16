<template>
<!--  <nav>-->
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link>-->
<!--  </nav>-->
<!--  <router-view/>-->
  <div class="app"> <!--  :style="myStyle"-->
    <div class="main">
      <div class="common-layout">
        <el-container>
          <el-header>Header</el-header>
          <el-main>
            <router-view/>
          </el-main>

          <el-footer>Footer</el-footer>
        </el-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // data (){
  //   return{
  //     myStyle:{
  //       backgroundColor:"#16a085"
  //
  //     }
  //   }
  // }
}
</script>


<style>
.common-layout .el-header, .common-layout .el-footer {
    background-color: var(--el-color-primary-light-7);
    color: var(--el-text-color-primary);
    text-align: center;
}

/*.common-layout .el-footer{*/
/*    height:50px;*/
/*}*/
* {
  margin: 0;
  padding: 0;
}
html,
body {
  height: 100%;
}
.el-header {
  position: relative;
  min-height: 100%;
}
.el-main {
  padding-bottom: 90px;
}
.el-footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 80px;
}



/*#app {*/
/*  font-family: Avenir, Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*}*/

/*nav {*/
/*  padding: 30px;*/
/*}*/

/*nav a {*/
/*  font-weight: bold;*/
/*  color: #2c3e50;*/
/*}*/

/*nav a.router-link-exact-active {*/
/*  color: #42b983;*/
/*}*/
</style>
