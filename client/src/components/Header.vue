<template>
  <div class="header">
    <router-link to="/">Главная</router-link>

    <el-divider direction="vertical" />

    <router-link to="/task-form-1">Составить тех. задание</router-link>

    <el-divider direction="vertical" />

    <router-link to="/about">О системе</router-link>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style>

.el-header {
  border: 1px solid #dcdfe6;
  /*border-radius: var(--el-border-radius-base);*/
  --el-header-height: auto;
}

.header {
  padding: 1.5rem;
  margin: 0.5px;
  background-color: var(--bg-color);
  /*background-color: var(--el-color-primary-light-7);*/
  /*color: var(--el-text-color-primary);*/
  /*text-align: center;*/
}

</style>