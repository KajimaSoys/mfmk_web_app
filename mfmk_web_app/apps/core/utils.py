import pdfrw

def _text_form(annotation, value):
    pdfstr = pdfrw.objects.pdfstring.PdfString.encode(value)
    annotation.update(pdfrw.PdfDict(V=pdfstr, AS=pdfstr))

def _checkbox(annotation, value):
    if value:
        annotation.update(pdfrw.PdfDict(V=pdfrw.objects.pdfname.BasePdfName('/Yes'), AS=pdfrw.objects.pdfname.BasePdfName('/Yes')))
    else:
        if '/V' in annotation:
            del annotation['/V']
        if '/AS' in annotation:
            del annotation['/AS']

def _field_type(annotation):
    ft = annotation['/FT']
    ff = annotation['/Ff']

    if ft == '/Tx':
        return 'text'
    if ft == '/Ch':
        if ff and int(ff) & 1 << 17:  # test 18th bit
            return 'combo'
        else:
            return 'list'
    if ft == '/Btn':
        if ff and int(ff) & 1 << 15:  # test 16th bit
            return 'radio'
        else:
            return 'checkbox'


def _radio_button(annotation, value):
    for each in annotation['/Kids']:
        # determine the export value of each kid
        keys = each['/AP']['/N'].keys()
        if ['/Off'] in keys:
            keys.remove('/Off')
        export = keys[0]

        if f'/{value}' == export:
            val_str = pdfrw.objects.pdfname.BasePdfName(f'/{value}')
        else:
            val_str = pdfrw.objects.pdfname.BasePdfName(f'/Off')
        each.update(pdfrw.PdfDict(AS=val_str))

    annotation.update(pdfrw.PdfDict(V=pdfrw.objects.pdfname.BasePdfName(f'/{value}')))




def pdf_form_info(in_pdf):
    info = []
    for page in in_pdf.pages:
        annotations = page['/Annots']
        if annotations is None:
            continue
        for annotation in annotations:
            choices=None
            if annotation['/Subtype'] == '/Widget':
                if not annotation['/T']:
                    annotation = annotation['/Parent']
                key = annotation['/T'].to_unicode()
                ft = _field_type(annotation)
                value = annotation['/V']
                if ft =='radio':
                    # value = value[1:]
                    choices =[]
                    for each in annotation['/Kids']:
                        keys = each['/AP']['/N'].keys()
                        if not keys[0][1:] in choices:
                            choices.append(keys[0][1:])
                elif ft == 'list' or ft=='combo':
                    choices = [each[1].to_unicode() for each in annotation['/Opt']]
                    values=[]
                    for each in annotation['/Opt']:
                        if each[0] in value:
                            values.append(each[1].to_unicode())
                    value=values
                else:
                    if value:
                        value=value.to_unicode()
                out = dict(name=key, type=ft)
                if value:
                    out['value']=value
                if choices:
                    out['choices']=choices
                info.append(out)
    print(info)





def fill_form(in_pdf, data, suffix=None):
    fillers = {
               'checkbox': _checkbox,
               # 'list': _listbox,
               'text': _text_form,
               # 'combo': _combobox,
               'radio': _radio_button}
    for page in in_pdf.pages:
        annotations = page['/Annots']
        if annotations is None:
            continue
        for annotation in annotations:

            if annotation['/Subtype'] == '/Widget':
                if not annotation['/T']:
                    annotation=annotation['/Parent']
                key = annotation['/T'].to_unicode()
                if key in data:
                    ft = _field_type(annotation)
                    fillers[ft](annotation, data[key])
                    if suffix:
                        new_T=pdfrw.objects.pdfstring.PdfString.encode(key+suffix)
                        annotation.update(pdfrw.PdfDict(T=new_T))
        in_pdf.Root.AcroForm.update(
            pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    return in_pdf


def single_form_fill(in_file, data, out_file):
    pdf = pdfrw.PdfReader(in_file)
    out_pdf = fill_form(pdf, data)
    pdfrw.PdfWriter().write(out_file, out_pdf)


def convert_data(instance):
    data_dict = {
      'system' :
            {
                'heating': '0',
                'water_supply': '1',
                'pumping_station': '2',
                'firefighting': '3',
            },
        'sup_parameter':
            {
                'pressure': '0',
                'temperature': '1',
                'flow': '2',
                'level': '3',
            },
        'cabinet_parameters':
            {
                'uhl4': '0',
                'uhl2': '1',
                'uhl1': '2',
            },
        'engine_control':
            {
                'direct': '0',
                'smooth': '1',
                'frequency': '2',
                'one_freq': '3',
                'for_each': '4',
            },
        'power_inputs':
            {
            'two_power_ats': '0',
            'two_power_noats': '1',
            'one_power': '2',
            },
    }

    data = {
        'Group2': data_dict['system'][instance.system] if instance.system != '' else '',
        # 'Group3': data_dict['sup_parameter'][instance.sup_parameter] if instance.sup_parameter != '' else '',
        'CheckBox7': True if 'pressure' in instance.sup_parameter else False,
        'CheckBox8': True if 'temperature' in instance.sup_parameter else False,
        'CheckBox9': True if 'flow' in instance.sup_parameter else False,
        'CheckBox10': True if 'level' in instance.sup_parameter else False,
        'CheckBox1': instance.volume_pump,
        'CheckBox2': instance.volume_fan,
        'CheckBox3': instance.volume_smoke_exhauster,
        'CheckBox4': instance.volume_gate_valves,
        'Text8' : instance.volume_pump_mark,
        'Text9' : instance.volume_fan_mark,
        'Text10' : instance.volume_smoke_exhauster_mark,
        'Text11' : instance.volume_gate_valves_mark,
        'Group4': data_dict['cabinet_parameters'][instance.cabinet_parameters] if instance.cabinet_parameters != '' else '',
        'Group5': data_dict['engine_control'][instance.engine_control] if instance.engine_control != '' else '',
        # 'CheckBox5': instance.one_freq,
        # 'CheckBox6': instance.for_each,
        'Group7': data_dict['power_inputs'][instance.power_inputs] if instance.power_inputs != '' else '',
        'Text36': instance.add_information,
    }

    #For engine_data
    k = 11
    for i in range(4):
        for j in range(6):
            k += 1
            data[f'Text{k}'] = instance.engine_data[i][j]

    return data


def generate_pdf(instance):
    in_file = 'media/pdf_templates/template.pdf'
    out_file = f'media/questionnaire_pdf/id_{instance.id}/questionnaire_{instance.id}.pdf'

    data = convert_data(instance)

    try:
        single_form_fill(in_file, data, out_file)
    except Exception as E:
        print(f"An error occurred: {E}")
        return False
    else:
        return True