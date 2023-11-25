from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='portrait', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.set_draw_color(254, 80, 80)
    pdf.line(10,  24, 200, 24)

    pdf.set_draw_color(0, 0, 0)
    for line in range(34, 290, 10):
        pdf.line(10, line, 200, line)
    # Set the footer
    pdf.ln(266)

    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for page in range(row['Pages'] - 1):
        pdf.add_page()

        # Draw black lines on page
        pdf.set_draw_color(0, 0, 0)
        for line in range(14, 290, 10):
            pdf.line(10, line, 200, line)

        # Set the footer
        pdf.ln(278)

        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output('output.pdf')
