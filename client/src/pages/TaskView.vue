<template>
<!--  <h1 class="title">Добавить новое техническое задание</h1>-->
<!--  <router-link to="/">Главная</router-link>-->
  <form @submit.prevent="submitForm">
<!--    <div>Основная информация</div>-->

    <div>
 <el-tabs v-model="tab_number" tab-position="bottom" class="demo-tabs"> <!-- style="height: 400px" -->
    <el-tab-pane label="Система">
      Система
      <div>
        <el-radio-group v-model="task.system" size="large">
          <el-radio-button label="heating">Отопление</el-radio-button>
          <el-radio-button label="water_supply">Водоснабжение</el-radio-button>
          <el-radio-button label="pumping_station">КНС</el-radio-button>
          <el-radio-button label="firefighting">Пожаротушение</el-radio-button>
        </el-radio-group>
      </div>
      <el-button @click="nextTab">Далее</el-button>
    </el-tab-pane>

    <el-tab-pane label="Производители">
      Производители
      <div>
        <el-radio-group v-model="task.manufacturer" size="large">
          <el-radio-button label="dek">DEK</el-radio-button>
          <el-radio-button label="iek">IEK</el-radio-button>
          <el-radio-button label="ekf">EKF</el-radio-button>
          <el-radio-button label="keaz">КЭАЗ</el-radio-button>
        </el-radio-group>
      </div>
      <el-button @click="previousTab">Назад</el-button>
      <el-button @click="nextTab">Далее</el-button>
    </el-tab-pane>

   <el-tab-pane label="Поддерживаемый параметр">
     Поддерживаемый параметр
     <div>
       <el-radio-group v-model="task.sup_parameter" size="large">
          <el-radio-button label="pressure">Давление</el-radio-button>
          <el-radio-button label="temperature">Температура</el-radio-button>
          <el-radio-button label="flow">Расход</el-radio-button>
          <el-radio-button label="level">Уровень</el-radio-button>
        </el-radio-group>
     </div>
     <el-button @click="previousTab">Назад</el-button>
     <el-button @click="nextTab">Далее</el-button>
   </el-tab-pane>

   <el-tab-pane label="Данные о системе">
     Объем теплоносителя в системе

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
          <el-col :span="4">
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
         <el-col :span="4">
          <span>
            Мощность, кВт
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[0][index-1]"/>
         </el-col>

       </el-row>

       <el-row>
         <el-col :span="4">
          <span>
            Напряжение, В
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[1][index-1]"/>
         </el-col>
       </el-row>

       <el-row>
         <el-col :span="4">
          <span>
            Номинальный ток, А
          </span>
         </el-col>

         <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[2][index-1]"/>
         </el-col>
        </el-row>

        <el-row>
          <el-col :span="4">
           <span>
            Номинальная частота вращения, об/мин
          </span>
         </el-col>
          <el-col :span="1" v-for="index in 6" :key="index">
           <el-input v-model="task.engine_data[3][index-1]"/>
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
     <el-button @click="previousTab">Назад</el-button>
     <el-button @click="nextTab">Далее</el-button>
<!--     <el-button @click="sendData">Отправить</el-button>-->
   </el-tab-pane>

   <el-tab-pane label="Параметры шкафа и окружающей среды">
    Параметры шкафа и окружающей среды
     <div class="cabinet_parameters">
       <el-radio-group v-model="task.cabinet_parameters" size="large">
          <el-radio-button label="uhl4">УХЛ4 (T окружающего воздуха не более +40 °С и не ниже 0 °С, средняя за 24 ч – не более 35 °С)</el-radio-button>
          <el-radio-button label="uhl2">УХЛ2 (-40 °С; +40 °С под навесом от воздействия осадков и солнечных лучей)</el-radio-button>
          <el-radio-button label="uhl1">УХЛ1 (-40 °С; +40 °С на открытом воздухе)</el-radio-button>
        </el-radio-group>
     </div>

     <el-divider/>

     Размер шкафа
     <div class="demo-input-suffix">
       <el-row>
          <el-col :span="3">
            <span>
              Ширина шкафа, мм
            </span>
          </el-col>

          <el-col :span="5">
           <el-input v-model="task.cabinet_width" clearable/>
         </el-col>
        </el-row>

       <el-row>
          <el-col :span="3">
            <span>
              Высота шкафа, мм
            </span>
          </el-col>

          <el-col :span="5">
           <el-input v-model="task.cabinet_height" clearable/>
         </el-col>
        </el-row>

       <el-row>
          <el-col :span="3">
            <span>
              Глубина шкафа, мм
            </span>
          </el-col>

          <el-col :span="5">
           <el-input v-model="task.cabinet_depth" clearable/>
         </el-col>
        </el-row>
     </div>
     <el-button @click="previousTab">Назад</el-button>
     <el-button @click="nextTab">Далее</el-button>
   </el-tab-pane>

   <el-tab-pane label="Управление двигателям">
    Управление двигателям
     <div>
       <el-radio-group v-model="task.engine_control" size="large" @change="freq_checked">
          <el-radio-button label="direct">Прямой пуск</el-radio-button>
          <el-radio-button label="smooth">Плавный пуск</el-radio-button>
          <el-radio-button label="frequency" ref="freq">Частотное регулирование</el-radio-button>

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
     <el-button @click="previousTab">Назад</el-button>
     <el-button @click="nextTab">Далее</el-button>
   </el-tab-pane>

   <el-tab-pane label="Количество вводов питания">
    Количество вводов питания
     <div>
       <el-radio-group v-model="task.power_inputs" size="large">
          <el-radio-button label="two_power_ats">Два ввода питания (с АВР)</el-radio-button>
          <el-radio-button label="two_power_noats">Два ввода питания (без АВР)</el-radio-button>
          <el-radio-button label="one_power">Один ввод питания</el-radio-button>
        </el-radio-group>
     </div>
     <el-button @click="previousTab">Назад</el-button>
     <el-button @click="nextTab">Далее</el-button>
   </el-tab-pane>

   <el-tab-pane label="Дополнительная информация">
    Дополнительная информация
     <div class="additional">
       <el-input
        v-model="task.add_information"
        :rows="4"
        type="textarea"
        placeholder="Введите комментарий.."
        clearable
       />
     </div>
     <el-button @click="previousTab">Назад</el-button>
      <el-button @click="sendData">Отправить</el-button>
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
import { ref } from 'vue';
import axios from "axios";

export default {
  name: "TaskView",
  data(){
    return{
      tab_number: '0',
      errors: [],
      disabled_pump: true,
      disabled_fan: true,
      disabled_smoke: true,
      disabled_gate: true,
      disabled_freq: true,

      // choices2 : ['Прямой пуск', 'Плавный пуск', 'Частотное регулирование', 'Один преобразователь частоты', 'ПЧ на каждый электродвигатель'],
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
        manufacturer: '',
        sup_parameter: '',
        volume_pump: false,
        volume_pump_mark: '',
        volume_fan: false,
        volume_fan_mark: '',
        volume_smoke_exhauster: false,
        volume_smoke_exhauster_mark: '',
        volume_gate_valves: false,
        volume_gate_valves_mark: '',
        engine_data: [
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
        ],
        cabinet_parameters: '',
        cabinet_width: '',
        cabinet_height: '',
        cabinet_depth: '',
        engine_control: '',
        engine_control_freq: [''],
        one_freq: false,
        for_each: false,
        power_inputs: '',
        add_information: '',
      }
    };
  },
  methods: {
    freq_checked: function () {
      if(this.task.engine_control === "frequency") {
        this.disabled_freq = false
      }
      else {
        this.disabled_freq = true
      }
    },

    nextTab: function () {
      this.tab_number = (parseInt(this.tab_number) + 1).toString()
    },

    previousTab: function () {
      this.tab_number = (parseInt(this.tab_number) - 1).toString()
    },

    async sendData() {
      // console.log(this.task)
      if (this.task.engine_control === "frequency") {
        if (this.task.engine_control_freq.includes('one_freq')) {
          this.task.one_freq = true
        } else {
          this.task.one_freq = false
        }

        if (this.task.engine_control_freq.includes('for_each')) {
          this.task.for_each = true
        } else {
          this.task.for_each = false
        }
      } else {
        this.task.one_freq = false
        this.task.for_each = false
      }

      const data = {
        'system': this.task.system,
        'manufacturer': this.task.manufacturer,
        'sup_parameter': this.task.sup_parameter,
        'volume_pump': this.task.volume_pump,
        'volume_pump_mark': this.task.volume_fan_mark,
        'volume_fan': this.task.volume_fan,
        'volume_fan_mark': this.task.volume_pump_mark,
        'volume_smoke_exhauster': this.task.volume_smoke_exhauster,
        'volume_smoke_exhauster_mark': this.task.volume_smoke_exhauster_mark,
        'volume_gate_valves': this.task.volume_gate_valves,
        'volume_gate_valves_mark': this.task.volume_gate_valves_mark,
        'engine_data': this.task.engine_data,
        'cabinet_parameters': this.task.cabinet_parameters,
        'cabinet_width': this.task.cabinet_width,
        'cabinet_height': this.task.cabinet_height,
        'cabinet_depth': this.task.cabinet_depth,
        'engine_control': this.task.engine_control,
        'test': this.task.engine_control_freq,
        'one_freq': this.task.one_freq,
        'for_each': this. task.for_each,
        'power_inputs': this.task.power_inputs,
        'add_information': this.task.add_information,
      }
      console.log(data)
      // TODO delete log

      await axios
        .post('/questionnare/', data)
        .then(response => {
          console.log('success')
        })
        .catch(error => {
          console.log(error)
        })

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
.el-tabs--bottom .el-tabs__header.is-bottom {
  position: absolute;
  /*left: 0;*/
  width: 98%;
  bottom: 5rem;
  padding: 2rem;
  /*width: 100%;*/
}
/*.el-tabs--bottom .el-tabs__item.is-bottom:nth-child(2){*/
/*  padding-left: 0;*/
/*}*/


.el-tabs__item {
  /*padding-left: 45px;*/
  padding-right: 85px;
}
/*.el-tabs--bottom .el-tabs__content {*/
/*  height: 100%;*/
/*}*/

.system-data .el-checkbox-button__inner {
  width: 120px;
}

.system-data .el-input {
  width: 60%;
}

.demo-input-suffix {
  font-size: 16px;


}

.cabinet_parameters .el-radio-group {
  align-items: flex-start;
  flex-direction: column;
}

.cabinet_parameters .el-radio-button__inner {
  border-left: var(--el-border) !important;
  border-right: var(--el-border) !important;
  border-radius: 4px !important;
}

.cabinet_parameters .el-radio-button__original-radio:checked+.el-radio-button__inner {
  box-shadow: 0 0 0 0;
  border-radius: 4px !important;

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

.additional .el-textarea__inner {
  width: 30%;
}


/*.radio_group {*/
/*  vertical-align: middle;*/
/*}*/

</style>