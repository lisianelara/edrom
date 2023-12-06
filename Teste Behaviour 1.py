def main():
    xponto = 2
    yponto = 3
    larguraretangulo = 40
    alturaretangulo = 20
    centrox = larguraretangulo / 2
    centroy = alturaretangulo / 2
    posicaoresultante = determinar_posicao(xponto, yponto,larguraretangulo,alturaretangulo,centrox,centroy)

    print(f"A posição do ponto é: {posicaoresultante}")

def determinar_posicao(x, y, largura, altura,centrox,centroy):
    # Verifica a posição em relação ao eixo X
    #A escolha da divisão por 4 foi por critério individual e
    #pode ser ajustada de acordo com os requisitos do programa e a
    #forma desejada para determinar a posição "centralizada".
    #O objetivo é aumentar o denominador para considerar uma área maior como "centralizada" ou
    #diminuí-lo para considerar uma área menor, permitindo adaptar a função às necessidades específicas do seu caso.
   
    if x< ((centrox - largura) / 4):
        posicaox = "esquerda"
    elif x > ((centrox - largura) / 4):
        posicaox = "direita"
    else:
        posicaox = "centralizado"

    # Verifica a posição em relação ao eixo y
    if y < (centroy - altura / 4):
        posicaoy = "baixo"
    elif y > (centroy - altura / 4):
        posicaoy = "p/cima"
    else:
        posicaoy = "centralizado"

    # Combina as posições em ambas as direções
    if posicaox == "centralizado" and posicaoy == "centralizado":
        posicao = "centralizado"
    else:
        posicao = f"{posicaoy} {posicaox}"

    return posicao

main()