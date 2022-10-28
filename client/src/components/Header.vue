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
  padding: 1.5rem;
  margin: 0.5px;
  height: 100px;
  color: #ffffff;
}

.logo img {
  float: left;
  width: 11%;
}

.header-contacts--mail {
  float: left;
  margin-left: 30%;
}

.header-contacts--phone {
  float: left;
  margin-left: 5%;
}

.header-contacts__sub {
  color: rgba(255, 255, 255, 0.5);
  font-size: 16px;
  line-height: 16px;
}

.link-like {
  cursor: pointer;
  font-size: 20px;
  line-height: 1.5;
}

.task_link {
  float: left;
  margin-left: 20%;
}

.task_link a {
  text-decoration: none;
  border: 1px solid #ffffff;
  color: #ffffff;
  padding: 7px 32px 7px;
  position: absolute;
}

.task_link a:hover {
  background-color: #ffffff;
  color: #000000;
}

.call_link {
  float: left;
  margin-left: 30%;
}

.call_link a {
  text-decoration: none;
  cursor: pointer;
  border: 1px solid #ffffff;
  background-color: #ffffff;
  color: #000000;
  padding: 7px 32px 7px;
  position: absolute;
}

.call_link a:hover{
  background-color: transparent;
  color: #ffffff;
}

</style>