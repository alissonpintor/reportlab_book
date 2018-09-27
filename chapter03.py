"""
    TRABALHANDO COM PAGE LAYOUT

    ANOTAÇÕES
    -----------------
    canvas.getAvailableFonts(): Retorna as fontes existente no reportalab
"""

import os
import time

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, NextPageTemplate
from reportlab.platypus import Frame, Spacer, Image, PageTemplate, PageBreak


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

    ptext = f'''
        <font size=12>We would like to welcome you to our subscriber 
        base for {mag_name} Magazine! You will receive {issue_name} issues at 
        the excellent introductory price of ${subprice}. Please respond 
        by {limited_date} to start receiving your subscription and get 
        the following free gift: {free_gift}.</font>
    '''
    flowables.append(Paragraph(ptext, styles['Justify']))

    doc.build(flowables)


def first_page(canvas, document):
    """
        Usado em create_document() para gerar um titulo na primeira pagina
    """

    title = 'PLATYPUS Demo'
    text = 'Welcome to the first PLATYPUS Page!'
    PAGE_HEIGHT = defaultPageSize[1]
    PAGE_WIDTH = defaultPageSize[0]

    canvas.saveState()
    canvas.setFont('Roboto-Light.ttf', 18)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-1*cm, title)

    canvas.setFont('Times-Roman', 10)
    canvas.drawString(cm, 0.5*cm, text)

    canvas.restoreState()


def later_pages(canvas, document):
    """
        Usado em create_document() para gerar o numero das paginas
    """

    canvas.saveState()
    canvas.setFont('Roboto-Light.ttf', 10)
    canvas.drawString(19*cm, 0.5*cm, f'Page {document.page}')

    canvas.restoreState()


def create_document():
    """
        Aqui nos usamos os parametros onFirstPage e onLaterPages de um 
        Document para gerar conteudo na primeira pagina e nas demais
        como por exempo numero da pagina, cabeçalhos, etc.
    """

    doc = SimpleDocTemplate(
        'gen/cap03/first_later.pdf',
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1.5*cm,
        topMargin=3*cm,
        bottomMargim=1.5*cm,
        showBoundary=True
    )

    roboto_light = 'Roboto-Light.ttf'
    registry_font(roboto_light)

    styles = getSampleStyleSheet()
    flowables = []
    spacer = Spacer(1, 0.5*cm)

    for i in range(50):
        text = f'Paragraph {i}'
        parag = Paragraph(text, styles['Normal'])
        flowables.append(parag)
        flowables.append(spacer)

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)


def mixed():
    """
        Usando Flowables utilizando um objeto Canvas no lugar 
        de um SimpleDocTemplate
    """

    mycanvas = canvas.Canvas('gen/cap03/mixed_flowables.pdf', pagesize=A4)
    styles = getSampleStyleSheet()
    width, heigth = A4

    text = "Hello, I'm a Paragraph!"
    para = Paragraph(text, style=styles['Normal'])
    para.wrapOn(mycanvas, width, heigth)
    para.drawOn(mycanvas, 1*cm, 27*cm)

    para2 = Paragraph(text + ' 02', style=styles['Normal'])
    para2.wrapOn(mycanvas, width, heigth)
    para2.drawOn(mycanvas, 1*cm, 26*cm)

    free_space = str(para2.getSpaceBefore())
    para3 = Paragraph(free_space, style=styles['Normal'])
    para3.wrapOn(mycanvas, width, heigth)
    para3.drawOn(mycanvas, 1*cm, 25*cm)

    mycanvas.save()


def frame_demo():
    """
        Usando Frames como conteiner para flowables
    """

    mycanvas = canvas.Canvas('gen/cap03/frame_demo.pdf', pagesize=A4)

    styles = getSampleStyleSheet()
    normal = styles['Normal']
    heading = styles['Heading1']
    spacer = Spacer(1, 0.5*cm)

    flowables = []
    flowables.append(Paragraph('Heading #1', heading))
    for i in range(50):
        flowables.append(Paragraph(f'Paragraph #{i}', normal))
        flowables.append(spacer)

    right_flowables = []
    right_flowables.append(Paragraph('Heading #2', heading))
    right_flowables.append(Paragraph('Paragraph #2', normal))

    left_frame = Frame(1*cm, 1*cm, width=5*cm, height=25*cm, showBoundary=1)
    right_frame = Frame(7*cm, 1*cm, width=5*cm, height=25*cm, showBoundary=1)

    left_frame.addFromList(flowables, mycanvas)
    right_frame.addFromList(right_flowables, mycanvas)

    mycanvas.save()


def alternate_orientation():
    """
        Criando paginas com em formaro landscape e quebra de pagina com
        PageBreak
    """

    doc = SimpleDocTemplate(
        'gen/cap03/alternate_orientation.pdf',
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1.5*cm,
        topMargin=2.5*cm,
        bottomMargim=1.5*cm)

    styles = getSampleStyleSheet()
    normal = styles['Normal']

    # Aqui criamos um frame e um template para cada tipo de orientação
    margin = 0.5 * cm
    frame = Frame(margin, margin, doc.width, doc.height, id='frame')
    frame_landscape = Frame(margin, margin, doc.height, doc.width, id='frame')
    portrait_template = PageTemplate(
        id='portrait', frames=[frame], pagesize=A4)
    landscape_template = PageTemplate(
        id='landscape', frames=[frame_landscape], pagesize=landscape(A4))

    doc.addPageTemplates([portrait_template, landscape_template])

    story = []
    story.append(Paragraph('This is a page in portrait orientation', normal))

    # alterar a orientação da página para landscape
    story.append(NextPageTemplate('landscape'))
    story.append(PageBreak())
    story.append(Spacer(cm, 0.5*cm))
    story.append(Paragraph('This is a page in landscape orientation', normal))

    # altera a orientação de volta para retrato
    story.append(NextPageTemplate('portrait'))
    story.append(PageBreak())
    story.append(Paragraph('Now back to portrait again', normal))

    doc.build(story)


if __name__ == '__main__':
    alternate_orientation()
