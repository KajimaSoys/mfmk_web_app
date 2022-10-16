<template>
  <h1 class="title">Добавить новое техническое задание</h1>
  <router-link to="/">Главная</router-link>
  <form @submit.prevent="submitForm">
    <div>Основная информация</div>

    <div>
 <el-tabs tab-position="left" class="demo-tabs"> <!-- style="height: 400px" -->
    <el-tab-pane label="Система">
      Система
      <div>
        <el-radio-group v-model="task.system" size="large">
          <el-radio-button label="Отопление" name="heating"/>
          <el-radio-button label="Водоснабжение" name="water_supply"/>
          <el-radio-button label="КНС" name="pumping_station"/>
          <el-radio-button label="Пожаротушение" name="firefighting"/>
        </el-radio-group>
      </div>
    </el-tab-pane>

    <el-tab-pane label="Производители">
      Производители
      <div>
        <el-radio-group v-model="task.manufacturer" size="large">
          <el-radio-button label="DEK" name="dek"/>
          <el-radio-button label="IEK" name="iek"/>
          <el-radio-button label="EKF" name="ekf"/>
          <el-radio-button label="КЭАЗ" name="keaz"/>
        </el-radio-group>
      </div>
    </el-tab-pane>

   <el-tab-pane label="Поддерживаемый параметр">
     Поддерживаемый параметр
     <div>
       <el-radio-group v-model="task.sup_parameter" size="large">
          <el-radio-button label="Давление" name="pressure"/>
          <el-radio-button label="Температура" name="temperature"/>
          <el-radio-button label="Расход" name="flow"/>
          <el-radio-button label="Уровень" name="level"/>
        </el-radio-group>
     </div>
   </el-tab-pane>

   <el-tab-pane label="Данные о системе">
     Объем теплоносителя в системе (литр)

     <div class="system-data">
       <div>
         <el-checkbox-button v-model="task.volume_pump" @change="disabled_pump = !disabled_pump">
           Насос
         </el-checkbox-button>

        <el-input v-model="task.volume_pump_mark" :disabled="disabled_pump" placeholder="Маркировка" clearable />
       </div>

       <div>
         <el-checkbox-button v-model="task.volume_fan" @change="disabled_fan = !disabled_fan">
          Вентилятор
         </el-checkbox-button>

        <el-input v-model="task.volume_fan_mark" :disabled="disabled_fan" placeholder="Маркировка" clearable/>
       </div>

        <div>
          <el-checkbox-button v-model="task.volume_smoke_exhauster" @change="disabled_smoke = !disabled_smoke">
            Дымосос
          </el-checkbox-button>

          <el-input v-model="task.volume_smoke_exhauster_mark" :disabled="disabled_smoke" placeholder="Маркировка" clearable/>
        </div>

       <div>
         <el-checkbox-button v-model="task.volume_gate_valves" @change="disabled_gate = !disabled_gate">
          Задвижки
         </el-checkbox-button>

        <el-input v-model="task.volume_gate_valves_mark" :disabled="disabled_gate" placeholder="Маркировка" clearable/>
       </div>
      </div>

     <el-divider/>

     Данные электродвигателей

     <div class="demo-input-suffix">
       <el-row>
          <el-col :span="6">
            <span>
              Номер электродвигателя
            </span>
          </el-col>

          <el-col :span="1" v-for="index in 6" :key="index" class="engine-number">
            <span>
            {{ index }}
          </span>
          </el-col>
        </el-row>


       <el-row>
         <el-col :span="6">
          <span>
            Мощность, кВт
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[0][index]"/>
         </el-col>

       </el-row>

       <el-row>
         <el-col :span="6">
          <span>
            Напряжение, В
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[1][index]"/>
         </el-col>
       </el-row>

       <el-row>
         <el-col :span="6">
          <span>
            Номинальный ток, А
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[2][index]"/>
         </el-col>
        </el-row>

        <el-row>
          <el-col :span="6">
           <span>
            Номинальная частота вращения, об/мин
          </span>
         </el-col>
          <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[3][index]"/>
         </el-col>
        </el-row>

      </div>

<!--     <div>-->
<!--       <el-radio-group v-model="engine_data" size="large" class="radio_group">-->
<!--          <el-radio-button label="Насос" name="pump"/>-->
<!--          <el-radio-button label="Вентилятор" name="fan"/>-->
<!--          <el-radio-button label="Дымосос" name="smoke_exhauster"/>-->
<!--          <el-radio-button label="Задвижки" name="gate_valves"/>-->

<!--       </el-radio-group>-->
<!--     </div>-->
   </el-tab-pane>

   <el-tab-pane label="Параметры шкафа и окружающей среды">
    Параметры шкафа и окружающей среды
     <div>
       <el-radio-group v-model="task.cabinet_parameters" size="large">
          <el-radio-button label="УХЛ4" name="uhl4"/>
          <el-radio-button label="УХЛ2" name="uhl2"/>
          <el-radio-button label="УХЛ1" name="uhl1"/>
        </el-radio-group>
     </div>
   </el-tab-pane>

   <el-tab-pane label="Управление двигателям">
    Управление двигателям
     <div>
       <el-radio-group v-model="task.engine_control" size="large" @change="freq_checked">
          <el-radio-button label="Прямой пуск" name="direct"/>
          <el-radio-button label="Плавный пуск" name="smooth"/>
          <el-radio-button label="Частотное регулирование" ref="freq" name="frequency"/>
             <el-checkbox-group v-model="task.engine_control_freq" size="large" :disabled="disabled_freq">
                 <el-checkbox-button key="one_freq" label="one_freq">
                   Один преобразователь частоты
                 </el-checkbox-button>
                 <el-checkbox-button key="for_each" label="for_each">
                   ПЧ на каждый электродвигатель
                 </el-checkbox-button>
           </el-checkbox-group>
        </el-radio-group>

     </div>
   </el-tab-pane>

   <el-tab-pane label="Количество вводов питания">
    Количество вводов питания
     <div>
       <el-radio-group v-model="task.power_input" size="large">
          <el-radio-button label="Два ввода питания (с АВР)" name="two_power_ats"/>
          <el-radio-button label="Два ввода питания (без АВР)" name="two_power_noats"/>
          <el-radio-button label="Один ввод питания" name="one_power"/>
        </el-radio-group>
     </div>
   </el-tab-pane>


<!--   <el-tab-pane label="Управление двигателем">-->
<!--     Поддерживаемый параметр-->
<!--     <div>-->
<!--       <el-tree-->
<!--          :props="props"-->
<!--          :load="loadNode"-->
<!--          lazy-->
<!--          show-checkbox-->
<!--          @check-change="handleCheckChange"-->
<!--       />-->
<!--     </div>-->
<!--   </el-tab-pane>-->
  </el-tabs>
    </div>

  </form>

</template>

<script>
import { ref } from 'vue'
export default {
  name: "TaskView",
  data(){
    return{
      errors: [],
      disabled_pump: true,
      disabled_fan: true,
      disabled_smoke: true,
      disabled_gate: true,
      disabled_freq: true,

      choices2 : ['Прямой пуск', 'Плавный пуск', 'Частотное регулирование', 'Один преобразователь частоты', 'ПЧ на каждый электродвигатель'],
      // engine_control_choices: [
      //   {
      //     short: 'direct',
      //     full: 'Прямой пуск',
      //   },
      //   {
      //     short: 'smooth',
      //     full: 'Плавный пуск',
      //   },
      //   {
      //     short: 'frequency',
      //     full: 'Частотное регулирование',
      //   },
      //   {
      //     short: 'one_freq',
      //     full: 'Один преобразователь частоты',
      //   },
      //   {
      //     short: 'for_each',
      //     full: 'ПЧ на каждый электродвигатель',
      //   },
      // ],

      task: {
        system: '',
        manufacturer: ref(''),
        sup_parameter: '',
        volume_pump: false,
        volume_pump_mark: '',
        volume_fan: false,
        volume_fan_mark: '',
        volume_smoke_exhauster: false,
        volume_smoke_exhauster_mark: '',
        volume_gate_valves: false,
        volume_gate_valves_mark: '',
        engine_data: [[''], [''], [''], [''], [''], ['']],
        cabinet_parameters: '',
        engine_control: '',
        engine_control_freq: [''],
        power_input: '',
        add_information: '',
      }
    };
  },
  methods: {
    freq_checked: function () {
      console.log('ok')
      // let radio = this.$refs.freq.classList
      // console.log(radio)
      console.log()
      if(this.task.engine_control === "Частотное регулирование") {
        console.log('checked')
      //
        this.disabled_freq = false
      }
      else {
        this.disabled_freq = true
        console.log('non checked')
      //   // TODO FIX!!!
      }
    }
  }
}






</script>



<style>



.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-tabs--left .el-tabs__content {
  height: 100%;
}

.system-data .el-checkbox-button__inner {
  width: 120px;
}

.system-data .el-input {
  width: 60%;
}

.demo-input-suffix {
  font-size: 16px;


}

.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
  margin-right: 10px;
  margin-left: 10px;
}

.el-row .el-col:first-child {
  margin-left: 0px;
}

.engine-number{
  text-align: center;
  /*padding-left: 0px ;*/
  /*padding-right: 0px;*/
}




/*.radio_group {*/
/*  vertical-align: middle;*/
/*}*/

</style>