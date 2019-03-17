#! /usr/bin/python3
import sys
import os
import time


# função que divide palavras com quebras de linha do array palavras_arquivo_lido
def retirarQuebrasDeLinhaDaPalavra(palavra):
    array_palavra = palavra.split()

    return array_palavra

#print(os.getcwd())
#/home/eduardo/Imagens/programa_inserir_imagens
#nome_doc = 'doc1.txt'


while len(sys.argv) != 1:

#    if len(sys.argv) == 1:
    print("Parametro incorreto, digite somente 1 nome de documento !!! \n")
    break


print('\n'*2)
print('='*60)
print('Bem vindo ao programa de inserir imagens em documento')
print('='*60)
print('\n')


#nomeUsuario = input("Digite o seu nome de usuário do sistema: ")

nomeUsuario = 'eduardo'

#lista de extesão de arquivos de imagem
lista_extensao = ['jpeg', 'png']

#extensao = input('Digite a extensão dos arquivos: ')

#while extensao not in lista_extensao:
#   extensao = input('Valor inválido, digite a extensão do arquivo corretamente: ')


# pede para inserir o nome do arquivo que será lido para posteriormente criar o arquivo html
nome_arquivo_lido = input('Digite o nome do arquivo a ser lido: ')
print()


# abre o arquivo nome_arquivo_lido em modo leitura
doc_arquivo_lido = open(nome_arquivo_lido, 'r')
# o texto está pronto para ser passado para o arquivo html
palavras_arquivo_lido = []
# cada palavra está sendo criada para adicionar ao array palavras_arquivo_lido
palavra_arquivo_provisorio = ''


for linha in doc_arquivo_lido:
    for caractere in linha:
        # se caractere for diferente de vazio, ou seja, se há caractere...
        if caractere != ' ':
            # se caractere de quebra de linha contiver na variável caractere...
            if '\n' in caractere:
                # atribui o caractere de quebra de linha na variável letras_quebra_de_linha.
                letras_quebra_de_linha = ''
                letras_quebra_de_linha += letras_quebra_de_linha.join(caractere)

                # if letras_quebra_de_linha for igual a caractere de quebra de linha...
                if letras_quebra_de_linha == '\n':
                    # adiciona o caractere de quebra de linha no array_letras_quebra_de_linha.
                    array_letras_quebra_de_linha = []
                    array_letras_quebra_de_linha.append(letras_quebra_de_linha)

                    # se o comprimento do array_letras_quebra_de_linha (que contem o
                    # caractere de quebra de linha) for igual a 1, vc adiciona em
                    # palavra_arquivo_provisorio o(s) proprio(s) caracter(es) mais o caractere de espaço.
                    #OBS: palavra_arquivo_provisorio armazena cada caractere que
                    # não for o caractere de quebra de linha (\n)
                    if len(array_letras_quebra_de_linha) == 1:
                        palavra_arquivo_provisorio += palavra_arquivo_provisorio.join(' ')

                    if len(array_letras_quebra_de_linha) > 1:
                        array_letras_quebra_de_linha.clear()

            else:
                # adicione o caractere em palavra_arquivo_provisorio
                palavra_arquivo_provisorio += palavra_arquivo_provisorio.join(caractere)


        # se caractere for igual a vazio
        elif caractere == ' ':
            # adicione os caracteres de palavra_arquivo_provisorio no array palavras_arquivo_lido
            palavras_arquivo_lido.append(palavra_arquivo_provisorio)
            # e deixe a string vazia em palavra_arquivo_provisorio
            palavra_arquivo_provisorio = ''

# adiciona a última palavra em palavra_arquivo_provisorio
palavras_arquivo_lido.append(palavra_arquivo_provisorio)
# zera a string em palavra_arquivo_provisorio
palavra_arquivo_provisorio = ''


# pergunta se deseja verificar cada palavra
result = input('Deseja visualizar a execução do programa palavra por palavra? [s ou n], se sim pode demorar vários minutos ou até horas [s ou n]: ')


while result not in 'sn':
    print('valor inválido, Digite s ou n !!!')
    result = input('Deseja visualizar a execução do programa palavra por palavra?, se sim pode demorar vários minutos ou até horas [s ou n]: ')


if result == 's':
    for palavra in palavras_arquivo_lido:

        # exibe a palavra que está sendo percorrida no momento e dá uma pausa de 5 segundos...
        print('palavra com espaço: {}'.format(palavra))
        time.sleep(5)

        # se a palavra em palavras_arquivo_lido contiver espaços...
        if ' ' in palavra:

            # exibe a palavra que está sendo percorrida no momento
            #print('palavra com espaço: {}'.format(palavra))
            #print()

            # armazena o numero do index da palavra percorrida no momento,
            # no array palavras_arquivo_lido armazenando o numero de index na variável index_palavra.
            index_palavra = palavras_arquivo_lido.index(palavra)

            # exibe o valor de index da palavra no momento e espera 2 segundos...
            print()
            print('valor de index_palavra: {}'.format(index_palavra))
            print()
            time.sleep(2)

            # armazena o index da palavra na variável index...
            index = index_palavra
            # e usa esse index para armazenar a palavra percorrida no momento em palavra_com_espaco.
            palavra_com_espaco = palavras_arquivo_lido[index]

            # função que retorna um array contendo as palavras faitadas,
            # armazenando-as na variável palavras_fatiadas
            palavras_fatiadas = retirarQuebrasDeLinhaDaPalavra(palavra_com_espaco)

            # inverte as palavras para ficar na ordem correta no array palavras_arquivo_lido
            palavras_fatiadas.reverse()

            # exibe as palavras fatiadas no array palavras_fatiadas e espera 2 segundos...
            print('palavras_fatiadas: {}'.format(palavras_fatiadas))
            print('------------')
            print()
            time.sleep(2)

            # exibe a quantidade em numero das palavras fatiadas no array palavras_fatiadas e espera 2 segundos...
            print('len de palavras_fatiadas: {}'.format(len(palavras_fatiadas)))
            print()
            time.sleep(2)

            # loop for usado para inserir cada indice de palavras_fatiadas em palavras_arquivo_lido.
            for j in range(0, len(palavras_fatiadas)):
                print('valor de j: {}'.format(j))
                print('--------------')

                palavras_arquivo_lido.insert(index, palavras_fatiadas[j])

            # criamos a variável remove_palavra_com_espaco...
            remove_palavra_com_espaco = 0
            # ao fatiarmos a palavra com espaço, esta mesma palavra ( a palvra com espaço ) ainda
            # continua no array palavras_arquivo_lido, para isso utilizamos a
            # variável remove_palavra_com_espaco inserindo o
            # seu indice de array em palavras_arquivo_lido remove-la logo abaixo...
            remove_palavra_com_espaco = int(index) + len(palavras_fatiadas)

            # pegamos a palavra com espaço em palavras_arquivo_lido...
            a = palavras_arquivo_lido[remove_palavra_com_espaco]

            # removemos a palavra com espaço de palavras_arquivo_lido...
            palavras_arquivo_lido.remove(a)

            # exibimos no terminal a palavra removida
            print('palavra a ser removida removida: {}'.format(a))
            print()

    # exibimos o array palavras_arquivo_lido
    print(palavras_arquivo_lido)

# fechamos o documento doc_arquivo_lido
doc_arquivo_lido.close()



if result == 'n':

    for palavra in palavras_arquivo_lido:

        # exibe a palavra que está sendo percorrida no momento
        print('palavra com espaço: {}'.format(palavra))

        # se a palavra em palavras_arquivo_lido contiver espaços...
        if ' ' in palavra:

            # armazena o numero do index da palavra percorrida no momento,
            # no array palavras_arquivo_lido armazenando o numero de index na variável index_palavra.
            index_palavra = palavras_arquivo_lido.index(palavra)

            print()
            print('valor de index_palavra: {}'.format(index_palavra))
            print()

            # adiciona o numero de index ao array array_index_palavra
            #array_index_palavra.append(index_palavra)
            #print('valor de array_index_palavra: {}'.format(array_index_palavra))


            # armazena o index da palavra na variável index...
            index = index_palavra
            # e usa esse index para armazenar a palavra percorrida no momento em palavra_com_espaco.
            palavra_com_espaco = palavras_arquivo_lido[index]

            # função que retorna um array contendo as palavras faitadas,
            # armazenando-as na variável palavras_fatiadas
            palavras_fatiadas = retirarQuebrasDeLinhaDaPalavra(palavra_com_espaco)

            # inverte as palavras para ficar na ordem correta no array palavras_arquivo_lido
            palavras_fatiadas.reverse()

            # exibe as palavras fatiadas no array palavras_fatiadas
            print('palavras_fatiadas: {}'.format(palavras_fatiadas))
            print('------------')
            print()

            # exibe a quantidade em numero das palavras fatiadas no array palavras_fatiadas
            print('len de palavras_fatiadas: {}'.format(len(palavras_fatiadas)))
            print()

            # loop for usado para inserir cada indice de palavras_fatiadas em palavras_arquivo_lido.
            for j in range(0, len(palavras_fatiadas)):
                print('valor de j: {}'.format(j))
                print('--------------')

                palavras_arquivo_lido.insert(index, palavras_fatiadas[j])

            # criamos a variável remove_palavra_com_espaco...
            remove_palavra_com_espaco = 0
            # ao fatiarmos a palavra com espaço, esta mesma palavra ( a palvra com espaço ) ainda
            # continua no array palavras_arquivo_lido, para isso utilizamos a
            # variável remove_palavra_com_espaco inserindo o
            # seu indice de array em palavras_arquivo_lido remove-la logo abaixo...
            remove_palavra_com_espaco = int(index) + len(palavras_fatiadas)

            # pegamos a palavra com espaço em palavras_arquivo_lido...
            a = palavras_arquivo_lido[remove_palavra_com_espaco]

            # removemos a palavra com espaço de palavras_arquivo_lido...
            palavras_arquivo_lido.remove(a)

            # exibimos no terminal a palavra removida
            print('palavra a ser removida removida: {}'.format(a))
            print()

    # exibimos o array palavras_arquivo_lido
    print(palavras_arquivo_lido)

# fechamos o documento doc_arquivo_lido
doc_arquivo_lido.close()
print()


# usado para inserir um título no novo arquivo criado
titulo_texto = input('Digite o nome do Título do documento: ')
# abre o arquivo em titulo_texto em modo escrita.
arq_html = open(titulo_texto, 'w')
print()

# comfirma se é esse nome de título que vc realmente quer...
resp = input('O título do texto é "{}", Deseja alterá-lo [s ou n] :'.format(titulo_texto)).lower()

# enquanto o valor de resp for 's'
while resp == 's':
    titulo_texto = input('Digite o nome do Título do documento: ')
    resp = input('O título do texto é {}, Deseja alterá-lo [s ou n] :'.format(titulo_texto)).lower()
    print()

# se o valor de resp é 'n'
if resp == 'n':
    #print('\n O arquivo {0} foi criado agora e o código padrão inicial foi inserido !!! \n'.format(titulo_texto))

    # escreve o código html no arquivo
    arq_html.write(
    """
<html>
<head>
    <meta charset="utf-8" >
    <title>{0}</title>
</head>
<body>
    <p>""".format(titulo_texto))

    #fecha o arquivo
    arq_html.close()

# abre o arquivo e exibe as linhas
#arq_html = open(titulo_texto, 'r')
#for linha in arq_html:
#    print(linha)
#arq_html.close()

# até o ccódigo acima, ele insere e exibe o código inicial html: head, titile, body, etc...


##############################################
    #Estou trabalhando nesse código abaixo
###############################################

# inserir a quantidade de imagens que serão inseridas para inserir a LARGURA e ALTURA
# equivalentes a quantidade de imagens inseridas, nas perguntas posteriores mais a baixo...
quant_img = input('Digite a quantidade de imagens a ser inserida no documento :')
resp = input('Tem certeza que digitou a quantidade correta de imagens? [s ou n] :')

while resp == 'n':
    quant_img = input('Digite a quantidade de imagens a ser inserida no documento :')
    resp = input('Tem certeza que digitou a quantidade correta de imagens? [s ou n] :')
    print()

if resp == ' ' or quant_img == ' ':
    quant_img = input('Valor inválido !!!, Digite a quantidade de imagens a ser inserida no documento :')
    resp = input('Tem certeza que digitou a quantidade correta de imagens? [s ou n] :')
    print()


# insere a largura das imagens em um array
array_largura_img = []

# insere a altura das imagens em um array
array_altura_img = []

# enquanto a quantidade de imagens em array_largura_img e em array_altura_img for menor que
# a quantidade em quant_img
while (len(array_largura_img) and len(array_altura_img)) < int(quant_img):
    # insere a largura das imagens em um array
    print()
    larg = input('Digite o número da largura da imagem (somente o número) : ')
    resp = input('Tem certeza que digitou o valor correto da LARGURA da imagem? [s ou n] : ')
    if resp == 's':
        array_largura_img.append(larg)
        print()
        print('largura do array_largura_img : {}'.format(array_largura_img))
        print()

    if resp == 'n':
        while resp == 'n':
            larg = input('Digite o número largura da imagem (somente o número) : ')
            resp = input('Tem certeza que digitou o valor correto da LARGURA da imagem? [s ou n] : ')
            if resp == 's':
                array_largura_img.append(larg)
                print()
                print('largura do array_largura_img : {}'.format(array_largura_img))

    while resp == ' ' or larg == ' ':
        larg = input('valor inválido!!!, Digite o número largura da imagem (somente o número) : ')
        resp = input('Tem certeza que digitou o valor correto da LARGURA da imagem? [s ou n] : ')
        if resp == 's':
            array_largura_img.append(larg)




    # insere a largura das imagens em um array
    alt = input('Digite o número altura da imagem (somente o número) : ')
    resp = input('Tem certeza que digitou o valor correto da ALTURA da imagem? [s ou n] : ')
    if resp == 's':
        array_altura_img.append(alt)
        print()
        print('altura do array_altura_img : {}'.format(array_altura_img))
        print()


    if resp == 'n':
        while resp == 'n':
            alt = input('Digite o número altura da imagem (somente o número) : ')
            resp = input('Tem certeza que digitou o valor correto da ALTURA da imagem? [s ou n] : ')
            if resp == 's':
                array_altura_img.append(alt)
                print()
                print('altura do array_altura_img : {}'.format(array_altura_img))



    while resp == ' ' or alt == ' ':
        alt = input('valor inválido!!!, Digite o número altura da imagem (somente o número) : ')
        resp = input('Tem certeza que digitou o valor correto da ALTURA da imagem? [s ou n] :')
        if resp == 's':
            array_altura_img.append(alt)


print()
print()
print('largura do array_largura_img : {}'.format(array_largura_img))
print()


print()
print('altura do array_altura_img : {}'.format(array_altura_img))
print()






###############################################
    #Estou trabalhando nesse código acima
#################################################




# insere todas as palavras que contêm img de palavras_arquivo_lido
array_palavras_img = []
# o novo arquivo criado sendo utilizado para adicionar mais conteúdo nele
arq_html = open(titulo_texto, 'a')
# armazena a quantidade (em número) de vezes que aparece a palavra 'img' em palavras_arquivo_lido.
quant_palavra_img = 0

i = 0
for palavra in palavras_arquivo_lido:

    print('palavra: {}'.format(palavra))
    #time.sleep(4)
    # pega o numero de indice da palavra em palavras_arquivo_lido
    index = palavras_arquivo_lido.index(palavra)

    print('index: {}'.format(index))
    print('++++++++++++++++++++++++')
    #time.sleep(4)

    # se o indice de palavras_arquivo_lido for igual a zero...
    if index == 0:
        #print('palavra do if de palavras_arquivo_lido: {}'.format(palavra))
        #print('######################')
        #time.sleep(3)
        arq_html.write(""" {}""".format(palavra))

    elif index > 0:
        print('palavra do elif de palavras_arquivo_lido: {}'.format(palavra))

        if 'img' in palavra:

            # faz a contagem de cada palavra 'img' acessada em palavras_arquivo_lido.
            quant_palavra_img += 1

            # verifica se a quantidade de palavras img em palavras_arquivo_lido é menor ou
            # igual a quantidade de imagens na pasta 'img' em programa_inserir_imagens.
            if  quant_palavra_img <= int(quant_img):

                # retorna todo o caminho a esquerda da ultima barra a direita, ou seja, a
                # última barra a direita (nesse exemplo na string) é a barra atrás de pasta01,
                # então, todo o caminho definido na string a partir dessa barra atrás do pasta01 , será retornada.
                #dirname = os.path.dirname('/home/'+nomeUsuario+'/programa_inserir_imagens/')
                # retorna apenas a última pasta do caminho, no exemplo, a pasta 'pasta01'.
                #basename = os.path.basename('/home/'+nomeUsuario+'/programa_inserir_imagens/')
                # caminho até as imagens que serão inseridas no arquivo html
                #caminho_img = os.path.join(dirname, basename)

                #caminho_img = '/home/'+nomeUsuario+'/Imagens/programa_inserir_imagens/img'

                # pega todo o caminho desde a raiz do sistema até a pasta 'img' em programa_inserir_imagens
                caminho_img = os.path.abspath('img')


                if 'img' in palavras_arquivo_lido[index] and index == (len(palavras_arquivo_lido)-1):
                    arq_html.write(""" \n\n <img src="{0}/{1}{2}"  width="{3}" heigth="{4}" alt="" /> \n\n""".format( caminho_img, palavra, '.png', array_largura_img[i], array_altura_img[i]))

                elif 'img' in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" \n\n <img src="{0}/{1}{2}"  width="{3}" heigth="{4}" alt="" /> <br/> <br/> \n""".format( caminho_img, palavra, '.png', array_largura_img[i], array_altura_img[i]))
                    # deleta a palavra que contêm img do array palavras_arquivo_lido
                    del palavra
                    # variável i usada para percorrer cada item dos arrays array_largura_img e array_altura_img.
                    i += 1

                elif 'img' not in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" \n\n <img src="{0}/{1}{2}"  width="{3}" heigth="{4}" alt=""  /> \n\n <p>""".format( caminho_img, palavra, '.png', array_largura_img[i], array_altura_img[i]))
                    # deleta a palavra que contêm img do array palavras_arquivo_lido.
                    del palavra
                    # variável i usada para percorrer cada item dos arrays array_largura_img e array_altura_img.
                    i += 1


            elif quant_palavra_img > int(quant_img):

                if 'img' in palavras_arquivo_lido[index] and index == (len(palavras_arquivo_lido)-1):
                    arq_html.write(""" \n\n <img src=""  width="" heigth="" alt=""/> \n\n""")

                elif 'img' in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" \n\n <img src=""  width="" heigth="" alt=""/> <br/> <br/> \n""")
                    i += 1

                elif 'img' not in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" \n\n <img src=""  width="" heigth="" alt=""/> \n\n <p>""")
                    i += 1

        elif palavra.endswith('.'):
            # se o index for menor que o array palavras_arquivo_lido, para poder fazer a checagem
            # da palavra posterior a palavra atual.
            if index < (len(palavras_arquivo_lido)-1):

                if  palavra.endswith('.') and 'img' in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0}</p>""".format(palavra))

                elif palavra.endswith('.') and 'img' not in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0}</p> \n <p> """.format(palavra))

                elif palavra.endswith('.'):
                    arq_html.write(""" {0}</p> \n """.format(palavra))


            elif index == (len(palavras_arquivo_lido)-1):

                if  palavra.endswith('.'):
                    arq_html.write(""" {0}</p> """.format(palavra))


                print('*************************')
                print('a array palavras_arquivo_lido NÃO POSSUI uma palavra a mais')
                print()


        elif palavra.endswith(':'):
            # se o index for menor que o array palavras_arquivo_lido, para poder fazer a checagem
            # da palavra posterior a palavra atual.
            if index < (len(palavras_arquivo_lido)-1):

                if  palavra.endswith(':')  and 'img' in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0}</p> \n """.format(palavra))

                elif palavra.endswith(':') and 'img' not in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0} """.format(palavra))


            #else:
            #    print('*************************')
            #    print('a array palavras_arquivo_lido NÃO POSSUI uma palavra a mais')
            #    print()


        elif palavra.endswith(','):

            # se o index for menor que o array palavras_arquivo_lido, para poder fazer a checagem
            # da palavra posterior a palavra atual.
            if index < (len(palavras_arquivo_lido)-1):

                if  palavra.endswith(',') and 'img' in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0}</p> \n """.format(palavra))

                elif palavra.endswith(',') and 'img' not in palavras_arquivo_lido[index+1]:
                    arq_html.write(""" {0} """.format(palavra))


            #else:
            #    print('*************************')
            #    print('a array palavras_arquivo_lido NÃO POSSUI uma palavra a mais')
            #    print()


        else:
            # senão escreva a palavra sem ponto no documento
            arq_html.write(""" {0} """.format(palavra).rstrip())
            print('PPPPPPPPPPPPPPPPPPPPPPPPP')
            print()

#    else:
#        arq_html.write(""" {0} """.format(palavra))




arq_html.write(""" \n\n </body> \n </html>""")

arq_html.close()






'''
# esse código funciona, naão mexer !!!!

        #if 'img' in palavra:
        #    arq_html.write("""<p>""")

        # se a palavra encontrada terminar com o caractere de ponto '.'
        if palavra.endswith('.'):

            if palavra.endswith('.') and 'img' in palavras_arquivo_lido[index+1]:
                arq_html.write(""" {0}{1}""".format(palavra, '</p>'))

            elif palavra.endswith('.'):
                arq_html.write(""" {0}{1}\n{2}""".format(palavra, '</p>', '<p>'))

        elif 'img' in palavra:

            #arq_html.write(""" <img src="{}.{}" alt=""> <p>""".format(palavra, 'png'))

            #arq_html.write(""" </p> <img src="{}.{}" alt=""> <p> """.format(palavra, 'png'))


        else:
            # senão escreva a palavra sem ponto no documento
            arq_html.write(""" {0} """.format(palavra).rstrip())
            print('PPPPPPPPPPPPPPPPPPPPPPPPP')
            print()

'''
'''
    if ' ' not in palavra:
        #arq_html.write("""{} """.format(palavra))
        arq_html.write(""" {} """.format(palavra))

    if '\n\n' in palavra: #or '\n' in palavra:
        # escreve as palavras em palavras_arquivo_lido no documento arq_html
        arq_html.write("""{0}{1}{2}""".format('</p>', '<p>', palavra))
'''


#arq_html.close()




















'''
    #abre o arquivo em modo escrita
    doc = open(nome_doc, 'w')

    # usado para inserir um título no arquivo
    titulo_texto = input('Digite o nome do Título do documento: ')

    # comfirma se é esse nome de título que vc realmente quer...
    resp = input('O título do texto é {}, Deseja alterá-lo: [s ou n]'.format(titulo_texto)).lower()

    # enquanto o valor de resp for 's'
    while resp == 's':
        titulo_texto = input('Digite o nome do Título do documento: ')
        resp = input('O título do texto é {}, Deseja alterá-lo: [s ou n]'.format(titulo_texto)).lower()

    # se o valor de resp é 'n'
    if resp == 'n':
        print('\n O arquivo {0} foi criado agora e o código padão inicial foi inserido !!! \n'.format(nome_doc))

        # escreve o código html no arquivo
        doc.write(
        """
        <html encode="utf-8">
            <head>
                <title>{0}</title>
            </head>
            <body>
        """.format(titulo_texto))

        #fecha o arquivo
        doc.close()

    # abre o arquivo e exibe as linhas
    doc = open(nome_doc, 'r')
    for linha in doc:
    print(linha)
    doc.close()

'''



'''
    for palavra in palavras_arquivo_lido:
        i = 0
        if palavra == lista_imagens[i]:
            arq_html = open('arquivo.html', 'w')
            arq_html.write('<img href="/home/Imagens/'+lista_imagens[i]+'>')
            arq_html.close()
        i+=1



    # variável do caminho até a pasta Imagens do sistema
    caminho_dirname = '/home/'+nomeUsuario+'Imagens/'

    # caminho até o arquivo da variável nome_doc
    caminho = os.path.join(os.path.dirname(caminho_dirname), 'programa_inserir_imagens')

    if nome_doc in caminho:
        resp = input('já existe um arquivo de nome "{}", \n Deseja adicionar dados no arquivo já existente? [s ou n]? '.format(nome_doc))

        while resp != 'sn':
            resp = input('Resposta errada !!!, deseja adicionar dados no arquivo? [s ou n]? ')
            if resp == 's':
                pass
            else:
                pass

    #se o arquivo não existe...
    elif nome_doc not in caminho:

        #abre o arquivo em modo escrita
        doc = open(nome_doc, 'w')
        # usado para inserir um título no arquivo
        titulo_texto = input('Digite o nome do Título do documento: ')
        # comfirma se é esse nome de título que vc realmente quer...
        resp = input('O título do texto é {}, Deseja alterá-lo: [s ou n]'.format(titulo_texto)).lower()
        # enquanto o valor de resp for 's'
        while resp == 's':
            titulo_texto = input('Digite o nome do Título do documento: ')
            resp = input('O título do texto é {}, Deseja alterá-lo: [s ou n]'.format(titulo_texto)).lower()
        # se o valor de resp é 'n'
        if resp == 'n':
            print('\n O arquivo {0} foi criado agora e o código padão inicial foi inserido !!! \n'.format(nome_doc))

            # escreve o código html no arquivo
            doc.write(
            """
            <html encode="utf-8">
                <head>
                    <title>{0}</title>
                </head>
                <body>
            """.format(titulo_texto))

            #fecha o arquivo
            doc.close()

    # abre o arquivo e exibe as linhas
    doc = open(nome_doc, 'r')
    for linha in doc:
        print(linha)
    doc.close()
'''

'''
resp = input('já existe um arquivo de nome "{}", Deseja adicionar dados no arquivo? [s ou n]? '.format(nome_doc))

print('Final')

# se o arquivo contiver dados dentro dele...
if nome_doc in caminho:
    print('Final')

    print('já existe um arquivo de nome {} !!!'.format(nome_doc))


    resp = input('Deseja adicionar dados no arquivo? [s ou n]? ')

    while resp not in 'sn'.lower():
        resp = input('Resposta errada !!!, deseja adicionar dados no arquivo? [s ou n]? ')

    if resp == 's':
        #
        doc = open(nome_doc, 'w')









resp = input('Deseja adicionar mais dados no arquivo? [s ou n]? ')

while resp not in 'sn'.lower():
    resp = input('você digitou errado !!!, deseja adicionar mais dados no arquivo? [s ou n]? ')

    if resp == 's'.lower():
        texto_digitado = doc.write(input('Digite o código html aqui inserindo as aspas triplas """ """ : '))
        print(doc.readlines())

        resp = input('Deseja inserir o mesmo texto no arquivo? [s ou n]')

        while resp not in 'sn'.lower():
            resp = input('você digitou errado !!!, deseja adicionar mais do mesmo texto no arquivo? [s ou n]? ')

        if resp == 's'.lower():
            vezes = input('Digite o número de vezes, por exemplo: 2, 5, 20  :')

            num = 0
            while vezes > num:
                lista_palavras = []
                lista_palavras.append(texto_digitado)



                doc.write(texto_digitado)




                lista_palavra = []
                palavra = 'href=""'
                palavra_encontrada = ''
                num = 0
                for caractere in doc:

                    #if caractere == palavra[num]:
                    #    lista_palavra.append(caractere)
                    #    palavra_encontrada = palavra_encontrada.join(caractere)
                    #    num += 1

                        if palavra == palavra_encontrada:
                            #vê se o médodo replace é para string e v c você consegue trocar as palavras...
                            pass

                    else:
                        palavra_encontrada = ''
                        lista_palavra.clear()

                        caractere = 'img' + str(vezes) + '.png' + '\n'
                    print(doc.readline())
                print(doc.readlines())

            num+=1




        doc.readlines()
        doc.close()

    elif resp == 'n':
        pass

'''
'''

    # procura pelo caractere '>' e separando as linhas com uma quebra de linha.
    #for caractere in doc:
    #    if caractere == '>':
    #        caractere = caractere + '\n'
    #    print(doc.readlines())
'''
