<template>
  <el-tabs v-model="tab_number" tab-position="bottom" class="demo-tabs" stretch>
    <el-tab-pane label="Информация о системе">

      <div class="system">
        <el-form
          label-width="auto"
          label-position="top"
          require-asterisk-position="right"
          status-icon
          size="large"
          ref="system_ref"
          :model="task"
          :rules="rules"
        >
          <el-form-item label="Система" prop="system">
            <el-radio-group v-model="task.system" size="large">
              <el-radio-button label="heating">Отопление</el-radio-button>
              <el-radio-button label="water_supply">Водоснабжение</el-radio-button>
              <el-radio-button label="pumping_station">КНС</el-radio-button>
              <el-radio-button label="firefighting">Пожаротушение</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <el-divider/>

          <el-form-item label="Производители" prop="manufacturer">
            <el-radio-group v-model="task.manufacturer" size="large">
              <el-radio-button label="dek">DEK</el-radio-button>
              <el-radio-button label="iek">IEK</el-radio-button>
              <el-radio-button label="ekf">EKF</el-radio-button>
              <el-radio-button label="keaz">КЭАЗ</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <el-divider/>

          <el-form-item label="Поддерживаемый параметр" prop="sup_parameter">
            <el-checkbox-group v-model="task.sup_parameter" size="large">
              <el-checkbox-button v-for="parameter in sup_paramater_choices" :key="parameter.key" :label="parameter.key">
                {{ parameter.value }}
              </el-checkbox-button>
            </el-checkbox-group>
          </el-form-item>

          <el-divider/>

          <el-form-item label="Объем теплоносителя в системе">
            <div class="system_data">
              <div class="system_data_element">
                <el-checkbox-button v-model="task.volume_pump" @change="disabled_pump = !disabled_pump">
                  Насос
                </el-checkbox-button>

                <el-input v-model="task.volume_pump_mark" :disabled="disabled_pump" placeholder="Маркировка" clearable />
              </div>

              <div class="system_data_element">
                <el-checkbox-button v-model="task.volume_fan" @change="disabled_fan = !disabled_fan">
                  Вентилятор
                </el-checkbox-button>

                <el-input v-model="task.volume_fan_mark" :disabled="disabled_fan" placeholder="Маркировка" clearable/>
              </div>

              <div class="system_data_element">
                <el-checkbox-button v-model="task.volume_smoke_exhauster" @change="disabled_smoke = !disabled_smoke">
                  Дымосос
                </el-checkbox-button>

                <el-input v-model="task.volume_smoke_exhauster_mark" :disabled="disabled_smoke" placeholder="Маркировка" clearable/>
              </div>

              <div class="system_data_element">
                <el-checkbox-button v-model="task.volume_gate_valves" @change="disabled_gate = !disabled_gate">
                  Задвижки
                </el-checkbox-button>

                <el-input v-model="task.volume_gate_valves_mark" :disabled="disabled_gate" placeholder="Маркировка" clearable/>
              </div>
            </div>
          </el-form-item>

          <el-divider/>

          <el-form-item label="Данные электродвигателей" prop="engine_data">
            <div class="demo-input-suffix">
              <el-row>
                <el-col :span="5">
                  <span>
                    Номер электродвигателя
                  </span>
                </el-col>

                <el-col :span="2" v-for="index in 6" :key="index" class="engine-number">
                  <span>
                    {{ index }}
                  </span>
                </el-col>
              </el-row>

              <el-row>
                <el-col :span="5">
                  <span>
                    Мощность, кВт
                  </span>
                </el-col>

                <el-col :span="2" v-for="index in 6" :key="index">
                  <template v-if="index==1">
                    <el-form-item class="zero_margin"
                                  :prop="'engine_data.0.0'"
                                  :rules="{required: true, trigger: 'blur',}" :show-message=show_message>
                      <el-input v-model="task.engine_data[0][index-1]"/>
                    </el-form-item>
                  </template>
                  <template v-else>
                    <el-input v-model="task.engine_data[0][index-1]"/>
                  </template>
                </el-col>
              </el-row>

              <el-row>
                <el-col :span="5">
                  <span>
                    Напряжение, В
                  </span>
                </el-col>

                <el-col :span="2" v-for="index in 6" :key="index">
                  <el-input v-model="task.engine_data[1][index-1]"/>
                </el-col>
              </el-row>

              <el-row>
                <el-col :span="5">
                  <span>
                    Номинальный ток, А
                  </span>
                </el-col>

                 <el-col :span="2" v-for="index in 6" :key="index">
                   <el-input v-model="task.engine_data[2][index-1]"/>
                 </el-col>
              </el-row>

              <el-row>
                <el-col :span="5">
                  <span>
                    Номинальная частота вращения, об/мин
                  </span>
                </el-col>
                  <el-col :span="2" v-for="index in 6" :key="index">
                    <el-input v-model="task.engine_data[3][index-1]"/>
                  </el-col>
              </el-row>
            </div>
          </el-form-item>

          <el-divider/>

          <div class="cabinet_parameters">
            <el-form-item class="big_text" label="Параметры шкафа и окружающей среды">
              <el-radio-group v-model="task.cabinet_parameters" size="large">
                <el-radio-button label="uhl4">УХЛ4 (T окружающего воздуха не более +40 °С и не ниже 0 °С, средняя за 24 ч – не более 35 °С)</el-radio-button>
                <el-radio-button label="uhl2">УХЛ2 (-40 °С; +40 °С под навесом от воздействия осадков и солнечных лучей)</el-radio-button>
                <el-radio-button label="uhl1">УХЛ1 (-40 °С; +40 °С на открытом воздухе)</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <el-divider/>

            <el-form-item class="big_text" label="Размер шкафа"/>

            <el-form-item label="Ширина шкафа, мм">
              <el-input class="w-25" type="text" v-model="task.cabinet_width" clearable/>
            </el-form-item>

            <el-form-item label="Высота шкафа, мм">
              <el-input class="w-25" type="text" v-model="task.cabinet_height" clearable/>
            </el-form-item>

            <el-form-item label="Гулбина шкафа, мм">
              <el-input class="w-25" type="text" v-model="task.cabinet_depth" clearable/>
            </el-form-item>
          </div>

          <el-divider/>

          <el-form-item label="Управление двигателям" prop="engine_control">
            <el-radio-group v-model="task.engine_control" size="large">
              <el-radio-button label="direct">Прямой пуск</el-radio-button>
              <el-radio-button label="smooth">Плавный пуск</el-radio-button>
              <el-radio-button label="frequency">Частотное регулирование</el-radio-button>
              <el-radio-button label="one_freq">Один преобразователь частоты</el-radio-button>
              <el-radio-button label="for_each">ПЧ на каждый электродвигатель</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <el-divider/>

          <el-form-item label="Количество вводов питания" prop="power_inputs">
            <el-radio-group v-model="task.power_inputs" size="large">
              <el-radio-button label="two_power_ats">Два ввода питания (с АВР)</el-radio-button>
              <el-radio-button label="two_power_noats">Два ввода питания (без АВР)</el-radio-button>
              <el-radio-button label="one_power">Один ввод питания</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <div class="next-button">
            <el-form-item>
              <el-button type="primary" @click="nextTabValidate($refs.system_ref)">Далее</el-button> <!-- , 'additional' -->
            </el-form-item>
          </div>

        </el-form>
      </div>
    </el-tab-pane>


    <el-tab-pane label="Контактная информация">
      <div class="main_info">
        <el-form
          label-width="auto"
          label-position="top"
          require-asterisk-position="right"
          status-icon
          size="large"
          ref="main_ref"
          :model="task"
          :rules="rules"
        >
          <div class="contacts">
            Контактные данные

            <el-form-item label="Организация" prop="entity">
              <el-input class="w-75" type="text" v-model="task.entity" clearable/>
            </el-form-item>

            <el-form-item label="ФИО" prop="name">
              <el-input class="w-75" type="text" v-model="task.name" clearable/>
            </el-form-item>

            <el-form-item label="Должность" prop="post">
              <el-input class="w-75" type="text" v-model="task.post" clearable/>
            </el-form-item>

            <el-form-item label="Email" prop="mail">
              <el-input class="w-75" type="email" v-model="task.mail" clearable/>
            </el-form-item>

            <el-form-item label="Контактный телефон" prop="number">
              <el-input class="w-75" type="text" v-model="task.number" clearable/>
            </el-form-item>

            <el-form-item label="Город" prop="city">
              <el-input class="w-75" type="text" v-model="task.city" clearable/>
            </el-form-item>
          </div>
          <div class="source_info">
            Основные даныне

            <el-form-item label="Название и расположение объекта" prop="object_info">
              <el-input
                class="w-50"
                v-model="task.object_info"
                :rows="4"
                type="textarea"
                clearable
              />
            </el-form-item>

            Как вы о нас узнали?

            <el-form-item prop="source">
              <el-radio-group v-model="task.source" size="large">
                <el-radio-button label="ad">Реклама Яндекс / Google</el-radio-button>
                <el-radio-button label="search">Поиск Яндекс / Google</el-radio-button>
                <el-radio-button label="social">Социальные сети</el-radio-button>
                <el-radio-button label="friends">Рекомендации коллег, друзей</el-radio-button>
                <el-radio-button label="work">Уже знали о нас, работали с нами</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="Другое" prop="source_another">
              <el-input
                class="w-50"
                v-model="task.source_another"
                :rows="4"
                type="textarea"
                clearable
              />
            </el-form-item>


            <el-divider/>

            <div class="additional">
              <el-form-item label="Дополнительная информация" prop="add_information">
                <el-input
                  v-model="task.add_information"
                  :rows="4"
                  type="textarea"
                  placeholder="Введите комментарий.."
                  clearable
                />
              </el-form-item>
            </div>

          </div>

          <div class="next-button">
          <el-form-item>
            <el-button @click="previousTab">Назад</el-button>
            <el-button type="primary" @click="sendData">Отправить</el-button>
          </el-form-item>
          </div>

        </el-form>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import { ref } from 'vue';
import axios from "axios";
import { ElMessage, ElMessageBox } from 'element-plus'
import {saveAs} from 'file-saver'
import FormInstance from 'element-plus'

export default {
  name: "TaskView",
  data(){
    return{
      rules: {
        entity: {
          required: true,
          message: "Поле обязательно для заполнения",
          trigger: "blur",
        },
        name: {
          required: true,
          message: "Поле обязательно для заполнения",
          trigger: "blur",
        },
        post: {
          required: true,
          message: "Поле обязательно для заполнения",
          trigger: "blur",
        },
        mail: {
          required: true,
          message: "Поле обязательно для заполнения",
          trigger: "blur",
        },
        number: {
          required: true,
          message: "Поле обязательно для заполнения",
          trigger: "blur",
        },
        system: {
          required: true,
          message: "Выберите один из вариантов",
          trigger: "change",
        },
        manufacturer: {
          required: true,
          message: "Выберите один из вариантов",
          trigger: "change",
        },
        engine_power: {
          required: true,
          trigger: "blur",
        },
        engine_control: {
          required: true,
          message: "Выберите один из вариантов",
          trigger: "change",
        }
      },


      tab_number: '0',


      disabled_pump: true,
      disabled_fan: true,
      disabled_smoke: true,
      disabled_gate: true,
      disabled_freq: true,
      show_message: false,

      sup_paramater_choices: [
        {
          key: 'pressure',
          value: 'Давление'
        },
        {
          key: 'temperature',
          value: 'Температура'
        },
        {
          key: 'flow',
          value: 'Расход'
        },
        {
          key: 'level',
          value: 'Уровень'
        },
      ],

      download_link: '',

      task: {
        entity: '',
        name: '',
        post: '',
        mail: '',
        number: '',
        city: '',
        object_info: '',
        source: '',
        source_another: '',

        system: '',
        manufacturer: '',
        sup_parameter: [],
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
        engine_control_freq: '',
        power_inputs: '',
        add_information: '',
      },
    };
  },
  methods: {
    onSubmit(){},
    nextTabValidate(ref) { //, element
      console.log(this.$refs)
      ref.validate((valid=any) => {
        if(valid) {
          // this.disabled_tabs[element] = false
          this.tab_number = (parseInt(this.tab_number) + 1).toString()
        } else {
          console.log("error submit!");
          return false
        }
      })
    },


    nextTab: function () {
      this.tab_number = (parseInt(this.tab_number) + 1).toString()
    },

    previousTab: function () {
      this.tab_number = (parseInt(this.tab_number) - 1).toString()
    },

    async check_validate(ref){
      let bool = false
      await this.$refs[ref].validate((valid=any) => {
          if (valid) { bool = true }
        })
      return bool
    },

    async sendData() {
      let errors = false
      for (let ref in this.$refs) {
        let res = await this.check_validate(ref)
        if (res){
          console.log(ref + ' валидно')
        } else {
          console.log(ref + ' не валидно')
          let form_tabs_ref = {
            main_ref: '0',
            system_ref: '1',
            manufacturer_ref: '2',
            sup_parameter_ref: '3',
            engine_data_ref: '4',
            cabinet_parameters_ref: '5',
            engine_control_ref: '6',
            power_inputs_ref: '7',
            add_information_ref: '8',
          }
          this.tab_number = form_tabs_ref[ref]
          errors = true
          break
          }
      }

      if (!errors) {
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

        var sup_param_serialized = []

        for (let item in this.task.sup_parameter){
          sup_param_serialized.push(this.task.sup_parameter[item])
        }

        const data = {
          'client': {
            'entity_name': this.task.entity,
            'name': this.task.name,
            'post': this.task.post,
            'email': this.task.mail,
            'number': this.task.number,
            'city': this.task.city,
          },
          'main_data': this.task.object_info,
          'source': this.task.source,
          'source_another': this.task.source_another,
          'system': this.task.system,
          'manufacturer': this.task.manufacturer,
          // 'sup_parameter': this.task.sup_parameter.values(),
          'sup_parameter': sup_param_serialized,
          'volume_pump': this.task.volume_pump,
          'volume_pump_mark': this.task.volume_pump_mark,
          'volume_fan': this.task.volume_fan,
          'volume_fan_mark': this.task.volume_fan_mark,
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
        // console.log(data)

        await axios
          .post('/questionnaire/', data)
          .then(response => {
            console.log('Success')
            this.get_path(response.data.id)
          })
          .catch(error => {
            console.log(error)
          })

          ElMessageBox.confirm(
            'Спасибо, Ваша заявка принята! Желаете загрузить опросный лист?',
            'Успешно',
            {
              confirmButtonText: 'Скачать',
              cancelButtonText: 'Отмена',
              type: 'success',
            })

          .then(() => {
            return axios({
              url: this.download_link,
              method: 'GET',
              responseType: 'blob',

            }).then(response => {
              console.log(response)
              saveAs(new Blob([response.data]), 'questionnaire.pdf')
            })
          })
      }
    },

    async get_path(id) {
      await axios
      .get(`/questionnaire/${id}/`)
      .then(response => {
        this.download_link = '/' + response.data.path + '/questionnaire_' + id + '.pdf'
        console.log(this.download_link)
      })
      .catch(error => {
        console.log(error)
      })
    },
  }
}
</script>


<style>
:root {
  --el-font-size-base: 0.8vw;
}

.demo-tabs {
  padding: 20px;
  background-color: #ffffff;
  /*height: 950px;*/
}

.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.contacts {
  float: left;
  width: 30%;
}

.source_info {
  margin-left: 30%;
}

.system .el-form-item__label,
.manufacturer .el-form-item__label,
.sup_parameter .el-form-item__label,
.system_data .el-form-item__label,
.cabinet_parameters .big_text .el-form-item__label,
.engine_control .el-form-item__label,
.power_inputs .el-form-item__label,
.additional .el-form-item__label {
  padding-top: 12px;
  font-size: 1.5vw;
  font-weight: 600;
  color: #6b778c;
}

.el-radio-button__inner{
  min-width: 130px;
}

.el-radio-group {
  margin-top: 20px;
}

.el-checkbox-group {
  margin-top: 20px;
}

.el-tabs--bottom .el-tabs__header.is-bottom {
  position: fixed;
  width: 98%;
  bottom: 0rem;
  padding: 1rem 2rem 1rem 2rem;
  background-image: linear-gradient(to bottom, rgba(255,0,0,0), rgb(255 255 255) 70%);
}

/*.system_data:deep(.el-checkbox-button__inner) {*/
/*  width: 100px;*/
/*}*/

/*.system_data .el-input {*/
/*  width: 40%;*/
/*}*/

/*.system_data:deep(.el-form-item__content) {*/
/*  margin-top: 30px;*/
/*  display: block;*/
/*  flex-direction: column;*/
/*  align-items: flex-start;*/
/*}*/

/*.system_data .zero_margin .el-form-item__content {*/
/*  margin-top: 0px;*/
/*}*/

/*.system_data_element {*/
/*  width: 40%;*/
/*}*/

.system_data {
  display: flex;
  flex-direction: column;
}

.system_data_element{
  display: flex;
  margin-bottom: 10px;
  align-items: flex-end;
}

.system_data_element > label {
  margin-bottom: 0!important;
}

.system_data_element > .el-input.el-input--large.is-disabled.el-input--suffix, .system_data_element > .el-input.el-input--large.el-input--suffix {
  font-size: var(--el-font-size-base);
  width: 390px!important;
  height: 38px!important;
  min-height: 38px!important;
}

span.el-checkbox-button__inner {
  min-width: 130px;
  width: 130px;
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

.cabinet_parameters .el-form-item label {
  font-size: 14px;
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
  /*padding-right: 65px;*/
}

.el-col-2 {
    max-width: 7.333333%;
    flex: 0 0 7.333333%;
}

.additional .el-textarea__inner {
  width: 50%;
}

.next-button {
    margin-top: 2rem;
    margin-bottom: 3rem;
}

.main_info .el-divider.el-divider--horizontal {
  width: 50%;
}

</style>