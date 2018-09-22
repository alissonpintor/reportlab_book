"""
    TRABALHANDO COM PAGE LAYOUT

    ANOTAÇÕES
    -----------------
    canvas.getAvailableFonts(): Retorna as fontes existente no reportalab
"""

import os
import time

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def registry_font(font):
    font_path = os.path.join('fonts', font)
    font = TTFont(font, font_path)
    pdfmetrics.registerFont(font)


def hello():
    doc = SimpleDocTemplate(
        'gen/cap03/hello.pdf',
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1.5*cm,
        topMargin=3*cm,
        bottomMargim=1.5*cm)

    styles = getSampleStyleSheet()
    flowables = []

    text = '<b style="color: #000;">Hello</b>, Eu sou um Paragrafo'
    parag = Paragraph(text, style=styles['Normal'])
    flowables.append(parag)

    doc.build(flowables)


def form_letter():
    doc = SimpleDocTemplate(
        'gen/cap03/letter.pdf',
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1.5*cm,
        topMargin=3*cm,
        bottomMargim=1.5*cm
    )

    roboto_light = 'Roboto-Light.ttf'
    registry_font(roboto_light)

    flowables = []
    logo = 'images/dota2.jpg'
    mag_name = "Pythonista"
    issue_name = 12
    subprice = '99.00'
    limited_date = '21/09/2018'
    free_gift = 'Sorvete de Uva'
    formated_time = time.ctime()
    full_name = 'Alisson Santana Pintor'
    address_parts = ['Estrada da Guarita', 'Condominio Terra Nova, casa 416']
    
    logo = Image(logo, 3*cm, 3*cm)
    flowables.append(logo)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontName=roboto_light))
    ptext = '<font size=12 color=red>%s</font>' % formated_time
    flowables.append(Paragraph(ptext, styles['Normal']))

    flowables.append(Spacer(1, 0.5*cm))

    ptext = '<font size=12> %s </font>' % full_name
    flowables.append(Paragraph(ptext, styles["Normal"]))

    for part in address_parts:
        ptext = '<font size=12>%s:</font>' % part.strip()
        flowables.append(Paragraph(ptext, styles['Normal']))
    
    flowables.append(Spacer(1, 12))

    ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
    flowables.append(Paragraph(ptext, styles['Normal']))

    flowables.append(Spacer(1, 12))

    ptext = '''
        <font size=12>We would like to welcome you to our subscriber 
        base for {0} Magazine! You will receive {1} issues at 
        the excellent introductory price of ${2}. Please respond 
        by {3} to start receiving your subscription and get 
        the following free gift: {4}.</font>
    '''.format(mag_name, issue_name, subprice, limited_date, free_gift)
    flowables.append(Paragraph(ptext, styles['Justify']))

    doc.build(flowables)


if __name__ == '__main__':
    form_letter()
