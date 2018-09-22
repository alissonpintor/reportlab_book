"""
    TRABALHANDO COM FONTES

    ANOTAÇÕES
    -----------------
    canvas.getAvailableFonts(): Retorna as fontes existente no reportalab
"""

import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def registry_font(font):
    font_path = os.path.join('fonts', font)
    font = TTFont(font, font_path)
    pdfmetrics.registerFont(font)


def init():
    c = canvas.Canvas('gen/cap02/fonts.pdf', pagesize=A4)

    roboto_black = 'Roboto-Black.ttf'
    roboto_light = 'Roboto-Light.ttf'
    registry_font(roboto_black)
    registry_font(roboto_light)

    c.setFont(roboto_black, 10)
    c.drawString(1.5*cm, 5*cm, 'Usando Fontes no Reportlab')

    c.setFont(roboto_light, 10)
    c.drawString(1.5*cm, 4.5*cm, 'Usando Fontes no Reportlab')

    c.showPage()
    c.save()


if __name__ == '__main__':
    init()
