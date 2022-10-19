<template>
  <div class="footer">
    © 2022 Компания МФМК
    <a href="https://mfmc.ru/agreement/">Политика обработки данных</a>
  </div>


</template>

<script>
export default {
  name: "Footer"
}
</script>

<style>

.el-footer {
  border: 1px solid #dcdfe6;
  --el-footer-height: auto;

  /*text-align: center;*/
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}

.footer {
  padding: 1.5rem;

  background-color: var(--bg-color);
}

.footer a{
  padding-left: 20px;
}
/*.common-layout .el-footer {*/
/*    background-color: var(--el-color-primary-light-7);*/
/*    color: var(--el-text-color-primary);*/

/*  text-align: center;*/
/*  position: absolute;*/
/*  left: 0;*/
/*  bottom: 0;*/
/*  width: 100%;*/
/*  height: 80px;*/
/*}*/
</style>