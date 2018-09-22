"""
    ANOTAÇÕES
    -----------------
    canvas.Canvas
        bottomup: alterar o ponto de origem da pagina para esquerda/topo quando
        configurado para 0
        pageCompression: ativa a compressão da pagina. Imagens sao sempre
        comprimidas
        enforceColorSpace: permiti definir a propriedade de cor a ser
        usada. Exemplo: rgb, cmyk
    
    Dentro do pacote reportlab.lib.pagesizes existe a funcao landscape que
    inverte o width e height para criar o formato de lanscape
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors


def coord(x, y, unit=1):
    x, y = x * unit, y * unit
    return x, y


def select_font(canvas):
    # fonts = canvas.getAvailableFonts()
    # print(fonts)
    # index = int(input('Digite o indice da fonte: '))
    # return fonts[index]
    return 'Helvetica'


def example01():
    c = canvas.Canvas('gen/cap01/hello.pdf', pagesize=A4, bottomup=1)

    c.drawString(1.0*cm, 1.0*cm, 'Welcome to Reportlab')

    # com textObject
    text = c.beginText()
    text.setTextOrigin(0.5*cm, 12*cm)
    text.setFillColor(colors.red)
    text.textLine('Apenas um texto 01')
    text.textLine('Apenas um texto 02')
    c.drawText(text)

    # Operações com linhas
    c.setLineWidth(0.3)
    c.line(3.5*cm, 3.6*cm, 8*cm, 3.6*cm)

    # denhando shapes
    c.setStrokeColorCMYK(0.3, 0.5, 0.7, 0.7)
    c.setFillColorCMYK(0.3, 0.5, 0.7, 0.7)
    c.rect(9*cm, 3*cm, 2*cm, 2*cm, fill=1)  # (x, y, largura, altura)
    c.setFillColorCMYK(1, 1, 1, 1)
    c.circle(10*cm, 4*cm, cm, fill=1)
    c.setFillColorCMYK(0, 0, 0, 0)
    c.ellipse(9*cm, 3.5*cm, 11*cm, 4.5*cm, fill=1)
    c.setFillColorCMYK(1, 1, 1, 1)
    c.wedge(9*cm, 3.5*cm, 11*cm, 4.5*cm, 270, 90, fill=1)

    # inserindo imagens
    c.drawImage('images/dota2.jpg', 0.5*cm, 4*cm, anchor='sw',
                width=2*cm, preserveAspectRatio=True)

    c.translate(cm, cm)  # usado para alterar o ponto de origem
    c.rotate(270)  # gira a pagina

    c.setFont(select_font(c), 10)
    c.setFillColor((0.5, 0.5, 0.5))
    c.drawString(-2.5*cm, 2.5*cm, 'Welcome to Reportlab')
    c.drawRightString(-2.5*cm, 2.5*cm, 'Welcome to Reportlab')

    c.showPage()
    c.save()


if __name__ == '__main__':
    example01()
