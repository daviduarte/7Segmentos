import re

letras_excluidas = "[gkmvwxz]"

with open('palavras.txt', encoding="utf8") as arquivao:
    palavras = arquivao.readlines()
    idioma = [palavra.rstrip('\n') for palavra in palavras]

palavra_mais_longa = ""
for palavra in idioma:

    if len(palavra) <= len(palavra_mais_longa):
        continue
    
    regex = re.findall(letras_excluidas, palavra)
    if len(regex) > 0:
        continue
        


    palavra_mais_longa = palavra




print(palavra_mais_longa)