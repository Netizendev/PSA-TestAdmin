from fpdf import FPDF

def print_to_pdf(body,letter_type,adress):
    name = body
    type_of_letter = letter_type
    def text_body(name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        # Times 12
        pdf.set_font('Times', '', 12)
        # Output justified text
        pdf.multi_cell(0, 5, txt)
        # Line break
        pdf.ln()
        # Mention in italics
        pdf.set_font('', 'I')
        pdf.cell(0, 5, '(end of excerpt)')

    class PDF(FPDF):
        def header(self):
            # Logo
            self.image('sahlpdfloggo.png', 10, 8, 33)
            # helvetica bold 15
            self.set_font('helvetica', 'B', 15)
            # Move to the right
            self.cell(80)
            # Title
            self.cell(30, 10, type_of_letter, 0, 0, 'C')
            # Line break
            self.ln(20)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # helvetica italic 8
            self.set_font('helvetica', 'I', 8)
            # Page number
            self.cell(0, 10, 'Sida ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        
    #Init class
    pdf = PDF()
    #Start print
    pdf.add_page()
    # Adress
    pdf.set_font('helvetica', 'B', 8)
    for x in adress:
        # Gå till höger
        pdf.cell(150)
        pdf.cell(30, 10, x, 0, 0, 'L')
        pdf.ln(3)
    # Line break
    pdf.ln(20)
    pdf.set_font('Times', '', 12)
    # Text på sidan
    text_body(name)
    #Output
    pdf.output('output.pdf')

adress = ['Test Testsson', 'Testvägen 1', '431 31 Testbyn']
print_to_pdf('kallelse.txt','KALLELSE',adress)