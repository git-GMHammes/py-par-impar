#  '12345'.isdigit() verdadeiro para numero
#  '1234.5'.isdigit() falso para numero
#  '12345abc'.isdigit() falso para numero
#  '12345abc'.isalnum() verdadeiro para alphanumerico
def valorImput1():
    var2: str = input('\n Digite um número inteiro: ')
    if verificaDigito(var2):
        parOuImpar(var2)
    else:
        print()
        print(f'\n ERRO: Você não digitou um número inteiro')
        valorImput2()


#
def valorImput2():
    var2: str = input('\n Digite um número inteiro: ')
    if verificaDigito(var2):
        parOuImpar(var2)
    else:
        print()
        print(f'\n ERRO: Você não digitou um número inteiro')
        valorImput1()


#
def parOuImpar(var1=0):
    variavel = int(var1)
    print()
    print(f'\n Você digitou: {variavel}')
    if (variavel % 2) == 0:
        print(f'\n O Valor {variavel} é PAR')
    else:
        print(f'\n O valor {variavel} é IMPAR')
    return exit('\n Fim do programa')


#
def verificaDigito(var3):
    return var3.isdigit()


#
valorImput1()
