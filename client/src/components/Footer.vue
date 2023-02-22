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
     background-color: #ffffff;
     position: absolute;
     bottom: 0;
     width: 100%;
}
 .footer {
     padding: 1.4rem;
     background-color: var(--bg-color);
     font-size: 0.8vw;
}
 .footer a{
     padding-left: 20px;
}
</style>