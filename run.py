import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors


FILENAME = 'gen/exemplo.pdf'
PAGEWIDTH, PAGEHEIGHT = A4
TOPRANGE = PAGEHEIGHT - (3.5*cm)
BOTTOMRANGE = 2.0*cm
IMAGES = ['images/10002.jpg', 'images/10007.jpg', 'images/10008.jpg',
          'images/10009.jpg', 'images/10010.jpg']


def add_cabecalho(c):
    c.setFillColor(colors.cadetblue)
    c.rect(0, PAGEHEIGHT - (2.5 * cm), PAGEWIDTH, PAGEHEIGHT, fill=1, stroke=0)
    c.setFillColor(colors.black)


def add_rodape(c):
    c.setFillColor(colors.cadetblue)
    c.rect(0, 0, PAGEWIDTH, 1.5 * cm, fill=1, stroke=0)
    c.setFillColor(colors.black)


def add_item(c, x, y):
    c.drawString(x, y, 'Joelho Soldável 90º')
    y -= 5.5*cm

    c.drawImage(random.choice(IMAGES), x, y, width=5*cm, height=5*cm)
    y -= 0.7*cm

    c.setFillColor(colors.cadetblue)
    c.rect(x, y, 5*cm, 0.5*cm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.drawString(x + 0.15 * cm, y + 0.10 * cm, 'Cod.')
    c.drawString(x + 1.3 * cm, y + 0.10 * cm, 'Descrição')
    c.drawString(x + 3.8 * cm, y + 0.10 * cm, 'Emb.')
    y -= 0.5*cm

    c.setFontSize(9)
    c.setFillColor(colors.black)
    c.drawString(x + 0.15 * cm, y + 0.10 * cm, '13504')
    c.drawString(x + 1.3 * cm, y + 0.10 * cm, '25mm')
    c.drawString(x + 3.8 * cm, y + 0.10 * cm, 'pct c/50')

    c.setFontSize(10)

    return x, y


def add_multi_item(c, x, y):
    c.drawString(x, y, 'Joelho Soldável 90º')
    y -= 5.5*cm

    c.drawImage(random.choice(IMAGES), x, y, width=5*cm, height=5*cm)
    y -= 0.7*cm

    c.setFillColor(colors.cadetblue)
    c.rect(x, y, 5*cm, 0.5*cm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.drawString(x + 0.15 * cm, y + 0.10 * cm, 'Cod.')
    c.drawString(x + 1.3 * cm, y + 0.10 * cm, 'Descrição')
    c.drawString(x + 3.8 * cm, y + 0.10 * cm, 'Emb.')
    y -= 0.5*cm

    items = [
        ('13455', '20mm', 'pct c/25'),
        ('13504', '25mm', 'pct c/25'),
        ('15611', '32mm', 'pct c/20'),
        ('15433', '40mm', 'pct c/12'),
        ('17433', '50mm', 'pct c/6'),
        ('17122', '60mm', 'pct c/6')
    ]

    for item in items:
        c.setFontSize(9)
        c.setFillColor(colors.black)
        c.drawString(x + 0.15 * cm, y + 0.10 * cm, item[0])
        c.drawString(x + 1.3 * cm, y + 0.10 * cm, item[1])
        c.drawString(x + 3.8 * cm, y + 0.10 * cm, item[2])
        c.line(x, y, x + 5 * cm, y)
        y -= 0.5*cm

    c.setFontSize(10)

    return x, y


def init():
    c = canvas.Canvas(FILENAME, pagesize=A4)
    x = 1.5*cm
    y = TOPRANGE

    c.setFont('Helvetica', 10)
    add_cabecalho(c)
    add_rodape(c)

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)

    x += 6 * cm
    y = TOPRANGE

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)

    x += 6 * cm
    y = TOPRANGE

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_multi_item(c, x, y)

    c.showPage()
    x = 1.5*cm
    y = TOPRANGE

    add_cabecalho(c)
    add_rodape(c)

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)

    x += 6 * cm
    y = TOPRANGE

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)

    x += 6 * cm
    y = TOPRANGE

    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_item(c, x, y)
    y -= 1 * cm
    x, y = add_multi_item(c, x, y)

    c.showPage()
    c.save()


if __name__ == '__main__':
    init()
