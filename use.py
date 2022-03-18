import urllib.request
import time

def preco_cafe():
    pag = urllib.request.urlopen("https://www.cafestore.com.br/cafe-barista-gourmet-em-graos-1kg_2179/p")
    texto = pag.read().decode("utf8")
    preco = texto[92727:92733]   
    novo = preco.replace(',', '.')
    novoD = float(novo)
    return(novoD)

novoPreco = input("Gostaria de ver o valor do Pão imediatamente? (Y/N)")
if novoPreco == 'Y':
    print(preco_cafe())
else:
    y = 99.00
    while y < 50.00:
        time.sleep(900)
        y = preco_cafe()
    print("comprar")

        



