from fpdf import FPDF

##A = Typ av brev. Provsvar (PS), Kallelse (KA), 10 årsbrev (10)
##B = namn och adress till person i format lista [] ex. [Test Testsson, Testvägen 1, 432 Testbyn]
##C = Dynamiskt datum. För provsvar vilket datum provet togs. För kallelse, vilket datum patienten är kallad. För 10 års brev, vilket datum patinenten är avskriven.
def print_to_pdf(a,b,c):    
    def text_body(body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        # Times 12
        pdf.set_font('Times', '', 12)
        # Output justified text
        pdf.multi_cell(0, 5, txt)
        # Line break
        pdf.ln()

    class PDF(FPDF):
        def header(self):
            # Logo
            self.image('1322.png', 10, 8, 33)
            # helvetica bold 15
            self.set_font('helvetica', 'B', 15)
            # Move to the right
            self.cell(80)
            # Title
            self.cell(30, 10, letter_title, 0, 0, 'C')
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
    ##Kolla typ av brev
    if a.lower() == 'ka':
        body = 'kallelse.txt'
        letter_title = 'kallelse'.upper()
    if a.lower() == 'ps':
        body = 'provsvar.txt'
        letter_title = 'provsvar'.upper()
    if a.lower() == '10':
        body = '10year.txt'
        letter_title = 'provtagning upphör'.upper()
    #Init class
    pdf = PDF()
    #Start print
    pdf.add_page()
    # Adress
    pdf.set_font('helvetica', 'B', 8)
    for x in b:
        # Gå till höger
        pdf.cell(140)
        pdf.cell(30, 10, x, 0, 0, 'L')
        pdf.ln(3)
    # Datum
    pdf.ln(3)
    pdf.cell(30, 10, 'Datum för ' + letter_title.lower(), 0, 0, 'L')
    pdf.cell(30, 10, c, 0, 0, 'L')
    pdf.ln(3)
    # Line break
    pdf.ln(20)
    pdf.set_font('Times', '', 12)
    # Text på sidan
    text_body(body)
    #Output
    pdf.output(letter_title.lower()+'_'+b[0].lower()+'_'+c+'.pdf')

##Testa genom följande kommandon
adress = ['Test Testsson', 'Testvägen 1', '432 Testbyn']
print_to_pdf('ka', adress, '2021-04-08')