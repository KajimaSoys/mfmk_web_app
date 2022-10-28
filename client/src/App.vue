<template>
  <div class="app">
    <div class="main">
      <div class="common-layout">
        <el-container>

          <el-header>
            <Header/>
          </el-header>

          <el-main>
            <router-view/>
          </el-main>

          <el-footer>
            <Footer/>
          </el-footer>

        </el-container>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  components: {Footer, Header}
}
</script>


<style>
* {
  margin: 0;
  padding: 0;
}

html,
body {
  height: 100%;
  /*TODO uncomment this*/
/*  background: rgb(213,232,255);*/
/*background: linear-gradient(138deg, rgba(213,232,255,1) 0%, rgba(229,211,255,1) 37%, rgba(238,174,202,1) 100%);*/
}

.el-main {
  padding-bottom: 90px;
}

/*.--el-color-primary-dark-2 {*/
/*  color: #337ecc*/
/*}*/
:root {
  --el-color-primary: #000066;
  --el-color-primary-light-3: #f89393;
  --el-button-hover-border-color: #ffffff;
  /*--el-button-hover-color: ;*/
}

.el-button--primary:hover{
  background: rgb(204, 204, 224);
  border-color: var(--el-color-primary);
  color: #000000;
}

a {
  color: var(--el-color-primary);
}
/*.el-footer {*/
/*  position: absolute;*/
/*  left: 0;*/
/*  bottom: 0;*/
/*  width: 100%;*/
/*  height: 80px;*/
/*}*/



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
