<template>
  <div class="main">
    <div class="common-layout">
      <el-container>
        <el-header>Header</el-header>
        <el-main><router-link to="/task-form-1">Составить техническое задание</router-link></el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </div>
  </div>


<!--  <div>-->
<!--    <router-link to="/task-form-1">Составить техническое задание</router-link>-->
<!--  </div>-->
</template>

<script>
export default {
  name: 'Main'
}
</script>

<style scoped>

</style>

