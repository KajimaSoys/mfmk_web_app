<template>
  <div class="header">
    <router-link to="/" class="logo">
      <img src="logo-white.svg" alt>
    </router-link>

    <div class="header-contacts--mail">
      <div class="header-contacts__sub">
        Напишите нам
      </div>

      <div data-href="mailto:info@mfmc.ru" class="link-like">
        info@mfmc.ru
      </div>
    </div>

    <div class="header-contacts--phone">
      <div class="header-contacts__sub">
        По России бесплатно
      </div>

      <div data-href="tel:84951222262" class="link-like">
        +7 (495) 122-22-62
      </div>
    </div>

    <div class="task_link">
      <router-link to="/task-form-1">
        Опросный лист
      </router-link>
    </div>

    <div class="call_link">
      <a href="https://mfmc.ru/local/popup/callback/" target="_blank">Заказать звонок</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style>

.bg-main {
  position: absolute;
}

.el-header {
  --el-header-height: auto;
  backdrop-filter: blur(4px) brightness(80%);

}

.header {
  padding: 1.2rem;
  margin: 0.5px;
  height: 80px;
  color: #ffffff;
  display: flex;
  justify-content: flex-start;
}

.logo{
  width: 38vw;
  display: flex;
}

.header-contacts--mail {
  width: 10vw;
}

.header-contacts--phone {
  width: 25vw;
}

.header-contacts__sub {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.8vw;
  line-height: 16px;
}

.link-like {
  cursor: pointer;
  font-size: 1vw;
  line-height: 1.5;
}

.task_link {
  width: 10vw;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-right: 10px;
}

.task_link a {
  text-decoration: none;
  border: 1px solid #ffffff;
  color: #ffffff;
  padding: 7px 25px 9px;
  position: absolute;
  font-size: 0.8vw;
}

.task_link a:hover {
  background-color: #ffffff;
  color: #000000;
}

.call_link {
  display: flex;
  align-items: center;
}

.call_link a {
  text-decoration: none;
  cursor: pointer;
  border: 1px solid #ffffff;
  background-color: #ffffff;
  color: #000000;
  padding: 7px 25px 9px;
  position: absolute;
  font-size: 0.8vw;
}

.call_link a:hover{
  background-color: transparent;
  color: #ffffff;
}

</style>