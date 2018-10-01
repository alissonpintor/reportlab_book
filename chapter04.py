"""
    TRABALHANDO COM STYLES

    ANOTAÇÕES
    -----------------
    Todos os markups Xml suportados pelo Paragraph estão na pagina 68-69 do livro

    Style Normal:
        name = Normal parent = None alignment = 0 allowOrphans = 0 allowWidows = 1 
        backColor = None borderColor = None borderPadding = 0 borderRadius = None 
        borderWidth = 0 bulletAnchor = start bulletFontName = Helvetica 
        bulletFontSize = 10 bulletIndent = 0 endDots = None firstLineIndent = 0 
        fontName = Helvetica fontSize = 10 justifyBreaks = 0 justifyLastLine = 0 
        leading = 12 leftIndent = 0 rightIndent = 0 spaceAfter = 0 spaceBefore = 0 
        spaceShrinkage = 0.05 splitLongWords = 1 textColor = Color(0,0,0,1) 
        textTransform = None underlineProportion = 0.0 wordWrap = None
"""

import os

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def registry_font(font):
    font_path = os.path.join('fonts', font)
    font = TTFont(font, font_path)
    pdfmetrics.registerFont(font)


class MyStyle(ParagraphStyle):
    """
        Como criar meu proprio style usando classe
    """

    def __init__(self, name):
        self.name = name
        self.__dict__.update(self.defaults)  # cria as propriedades usando as defaults
        self.leading = 14


def my_style():
    """
        Como criar meu proprio style com função
    """

    style = ParagraphStyle
    style.name = 'MyStyle'
    style.fontSize = 16
    style.leading = 12

    return style


def paragraph_markup():
    """
        Usando markups xml para stilizar o paragrafo
    """

    doc = SimpleDocTemplate('gen/cap04/paragraph_markup.pdf', pagesize=A4)
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    spacer = Spacer(cm, 0.5*cm)
    flowables = []

    text = "<para align=center>Hello, I'm a paragraph</para>"
    para = Paragraph(text, style=normal)
    flowables.append(para)

    flowables.append(spacer)

    text = """
    <para align=justify> Fusce molestie libero eu metus facilisis, vitae 
    efficitur ligula suscipit. Ut sit amet mauris vitae velit volutpat porta. 
    Etiam id bibendum odio. Proin congue molestie lorem. Nam non viverra sapien. 
    Vestibulum mattis tellus ut enim iaculis, vitae posuere massa laoreet. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames 
    ac turpis egestas. Sed pulvinar purus nulla, lacinia efficitur mauris 
    pulvinar non. </para> 
    """
    para2 = Paragraph(text, style=normal)
    flowables.append(para2)

    doc.build(flowables)


def intra_tags():
    """
        Usando tags internas <b>, <i>, <u>, <a href>, <a name> <srike>, <br/>
    """

    doc = SimpleDocTemplate('gen/cap04/intra_tags.pdf', pagesize=A4)
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    normal.spaceBefore = 10
    normal.spaceAfter = 15
    spacer = Spacer(cm, 0.5*cm)
    flowables = []

    text = """
    This <b>text</b> is important, not <strong>strong</strong>.<br/><br/> 
    A book title should be in <i>italics</i><br/><br/> 
    You can also <u>underline</u> your text.<br/><br/>
    Bad text should be <strike>struck-through</strike>!<br/><br/> 
    You can link to <a href="https://www.google.com" color="blue">Google</a> like this.
    """
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = """
    This <b>text</b> is important, not <strong>strong</strong>.<br/><br/> 
    """
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = """
    This <b>text</b> is important, not <strong>strong</strong>.<br/><br/> 
    """
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = """
    This <b>text</b> is important, not <strong>strong</strong>.<br/><br/> 
    """
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = """
    This <b>text</b> is important, not <strong>strong</strong>.<br/><br/> 
    """
    para = Paragraph(text, style=normal)
    flowables.append(para)

    doc.build(flowables)


def paragraph_fonts():
    """
        Alterando as fontes dos paragrafos
    """

    doc = SimpleDocTemplate('gen/cap04/paragraph_fonts.pdf', pagesize=A4)
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    normal.spaceAfter = 15
    spacer = Spacer(cm, 0.5*cm)
    flowables = []

    roboto_light = 'Roboto-Light.ttf'
    registry_font(roboto_light)

    text = "<font face=courier size=14 color=red>Welcome to Reportlab! (courier)</font>"
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = "<font face=times-roman size=14 color=#777215>Welcome to Reportlab! (times-roman)</font>"
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = f"<font face={roboto_light} size=14 fg=blue>Welcome to Reportlab! ({roboto_light})</font>"
    para = Paragraph(text, style=normal)
    flowables.append(para)

    text = f"""
    Here is a picture: <img src="images/dota2.jpg" width="20" height="20"/> in the middle of our text
    """ 
    para = Paragraph(text, style=normal)
    flowables.append(para)

    doc.build(flowables)


if __name__ == '__main__':
    # p = MyStyle('Teste')
    # print(p.name)
    # print(p.leading)
    paragraph_fonts()