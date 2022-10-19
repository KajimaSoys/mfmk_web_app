from PyPDF2 import PdfReader, PdfWriter
import pdfrw

INVOICE_TEMPLATE_PATH = '../../../tests/template2.pdf'
INVOICE_OUTPUT_PATH = '../../../tests/temp.pdf'

ANNOT_KEY = '/Annots'           # key for all annotations within a page
ANNOT_FIELD_KEY = '/T'          # Name of field. i.e. given ID of field
ANNOT_FORM_type = '/FT'         # Form type (e.g. text/button)
ANNOT_FORM_button = '/Btn'      # ID for buttons, i.e. a checkbox
ANNOT_FORM_text = '/Tx'         # ID for textbox
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# def temp(input_pdf_path, output_pdf_file, data_dict):
#     template_pdf = pdfrw.PdfReader(input_pdf_path)


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for Page in template_pdf.pages:
        if Page[ANNOT_KEY]:
            for annotation in Page[ANNOT_KEY]:

                if annotation[ANNOT_FIELD_KEY] and annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY :
                    key = annotation[ANNOT_FIELD_KEY][1:-1] # Remove parentheses
                    key2 = annotation
                    # print(key2)

                    if key in data_dict.keys():
                        if annotation[ANNOT_FORM_type] == ANNOT_FORM_button:
                            # button field i.e. a checkbox
                            print(annotation[ANNOT_FORM_type])
                            annotation.update( pdfrw.PdfDict( V=pdfrw.PdfName(data_dict[key]) , AS=pdfrw.PdfName(data_dict[key]) ))
                        elif annotation[ANNOT_FORM_type] == ANNOT_FORM_text:
                            # regular text field
                            annotation.update( pdfrw.PdfDict( V=data_dict[key], AP=data_dict[key]) )
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
    print(key2)

data_dict = {
    # 'item_1_amount': '123',
    'Choice1': 'Yes',
    'Text8': 'Дела блять'}
    # 'CheckBox2': 'Off'  }


if __name__ == '__main__':
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)







def generate_pdf(instance):
    reader = PdfReader("media/pdf_templates/template.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[1], {
            # "Text1": instance.system
            "Group1" : {
                '/V': '/0'
            }
        }
    )

    with open(f"{instance.path}/pdf_file.pdf", "wb") as output_stream:
        writer.write(output_stream)


    return True

def main():
    reader = PdfReader("../../../media/pdf_templates/template3.pdf")
    writer = PdfWriter()

    print(reader.numPages)
    page2 = reader.pages[1]
    print(page2.extractText())
    fields = reader.get_fields()
    print(fields)

    writer.add_page(page2)
    #
    writer.update_page_form_field_values(
        writer.pages[0], {
            # "Text1": instance.system
            "Group5" : {'/V':'/0'}}
    )
    fields = reader.get_fields()
    print(fields)
    #
    with open(f"../../../tests/temp3.pdf", "wb") as output_stream:
        writer.write(output_stream)


