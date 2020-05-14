from fpdf import FPDF

def text_to_pdf(*args, **kwargs):
    name = kwargs['name']
    amount = kwargs['amount']
    method = kwargs['method']
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size = 15)

    txt = "Transaction Done successfully!!!"
    pdf.cell(200, 10, txt = name,ln = 1, align = 'C')
    pdf.cell(200, 10, txt = amount,ln = 2, align = 'C')
    pdf.cell(200, 10, txt = method,ln = 3, align = 'C')
    pdf.cell(200, 10, txt = txt,ln = 4, align = 'C')
    file_name = "/tmp/"+name+"_.pdf"
    pdf.output(file_name)
