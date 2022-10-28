<template>
  <div class="app">
      <div class="common-layout">
        <div class="image-box">
          <img src="../src/images/main-bg.jpg">
        </div>

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
}

.el-main {
  --el-main-padding: 0px;
}

.image-box {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  z-index: -2;
}

.image-box img {
  display:block;
  width:100%;
  height:100%;
  object-fit: cover;
}

:root {
  --el-color-primary: #000066;
  --el-color-primary-light-3: #f89393;
  --el-button-hover-border-color: #ffffff;
}

.el-button--primary:hover{
  background: rgb(204, 204, 224);
  border-color: var(--el-color-primary);
  color: #000000;
}

a {
  color: var(--el-color-primary);
}
</style>
