'''
Created on 14 de dez. de 2025

@author: Marcus Vinicius Belo Matos de Aguiar
'''
# Programa para realizar operações (conversão, soma, subtração, multiplicação e divisão) com números complexos

import math

# Função Para Converter de retangular para polar
def RetParaPolar(z):
    if type(z) == tuple:                # verifica se o número enviado já está em formato polar, caso verdadeiro retorna ao usuário apenas a mensagem, caso contrário realiza a conversão
        print("O numero ja esta no formato polar")
    else:
        try:
            a = z.real                      # a recebe a parte real de z
            b = z.imag                      # b a parte imaginária
            p = math.sqrt(a*a + b*b)        # calculo do modulo
            theta = math.atan(b/a)          # calculo do angulo
            theta = theta*180/math.pi       # converte o angulo de radiano para graus
            zConvertido = (p,theta)         # confecção do novo numero complexo convertido, agora em formato de tupla
            return zConvertido
        except ZeroDivisionError:
            print("Erro! A parte real do segundo numero nao pode ser nula")
            return None

#Função para Converter de polar para retangular
def PolarParaRet(z):
    if type(z) == tuple:                # verifica novamente se o formato do numero é polar
        p = z[0]                        # p recebe o primeiro elemento da tupla, ou seja, o módulo
        theta = z[1]                    # theta recebe o segunda elemento, o ângulo
        theta= theta*math.pi/180        # converte o angulo de graus para radianos
        a = p*math.cos(theta)           # calculo da parte real
        b = p*math.sin(theta)           # calculo da parte imaginária
        zConvertido = complex(a,b)      # construção do novo número complexo após conversão
        return zConvertido
    else:
        print("O numero ja esta em formato retangular")

# Função Para somar dois numeros complexos
def SomaComplexa(z1,z2):
    a1 = z1.real                        # a recebe a parte real
    a2 = z2.real
    b1 = z1.imag                        # e b a parte imaginaria
    b2 = z2.imag
    aSoma = a1 + a2                     # soma as partes reais
    bSoma = b1 + b2                     # soma as partes imaginarias
    zSoma = complex(aSoma, bSoma)       # constroi o numero complexo resultado da soma dos dois anteriores, em formato retangular
    return zSoma

# Função Para subtrair dois numeros complexos
def SubComplexa(z1,z2):
    a1 = z1.real                        # a recebe a parte real
    a2 = z2.real
    b1 = z1.imag                        # e b a parte imaginaria
    b2 = z2.imag
    aSub = a1 - a2                      # subtrai as partes reais
    bSub = b1 - b2                      # subtrai as partes imaginarias
    zSub = complex(aSub, bSub)          # constroi o numero complexo resultado da subtração dos dois anteriores, em formato retangular
    return zSub

# Função Para multiplicar dois numeros complexos
def MultComplexa(z1,z2):
    z1 = RetParaPolar(z1)               # converte o primeiro numero para o formato polar
    z2 = RetParaPolar(z2)               # converte o segundo numero para o formato polar
    p1 = z1[0]                          # p recebe o modulo, primeiro elemento da tupla
    p2 = z2[0]
    theta1 = z1[1]                      # theta recebe o angulo, segundo elemento da tupla
    theta2 = z2[1]
    pMult = p1*p2                       # multiplica os modulos
    thetaMult = theta1 + theta2         # soma os angulos
    zMult = (pMult, thetaMult)          # constroi o novo numero complexo, em formato tupla
    zMult = PolarParaRet(zMult)         # converte para retangular
    return zMult
    
# Função Para dividir dois numeros complexos
def DivComplexa(z1,z2):
    z1 = RetParaPolar(z1)               # converte o primeiro numero para o formato polar
    z2 = RetParaPolar(z2)               # converte o segundo numero para o formato polar
    p1 = z1[0]                          # p recebe o modulo, primeiro elemento da tupla
    p2 = z2[0]
    theta1 = z1[1]                      # theta recebe o angulo, segundo elemento da tupla
    theta2 = z2[1]
    try:
        pDiv = p1/p2                    # divide os modulos, caso p2 for nulo vai para exception
        thetaDiv = theta1 - theta2      # subtrai os angulos
        zDiv = (pDiv, thetaDiv)         # constroi o novo numero complexo, em formato tupla
        zDiv = PolarParaRet(zDiv)       # converte para retangular
        return zDiv
    except ZeroDivisionError:
        print("Erro: Impossível dividir por 0")
        return None

# Inicio do Programa: construindo um menu rudimentar no console para auxiliar o usuário
print("Programa para trabalhar com numeros complexos. \n Selecione a opçao desejada:")
print("1 - Realizar conversao de retangular para polar")
print("2 - Realizar a conversao de polar para retangular ")
print("3 - Somar dois numeros complexos")
print("4 - Subtrair dois numeros complexos")
print("5 - Multiplicar dois numeros complexos")
print("6 - Dividir dois numeros complexos")

# Alerta o usuario caso ele digite uma opão menor que 1 ou maior que 6, ou seja, valores inteiros fora do intervalo do menu anterior, e trata caso ele digite um valor não inteiro
while True:
    try:
        opcao_str = input("Digite sua opçao: ")
        opcao = int(opcao_str)
        if 1 <= opcao <= 6:
           # Implementação do menu utilizando estrutura do tipo switch-case
           match opcao:
               case 1:                             # Converter de retangular para polar
                   try:                            # Trata as entradas indesejadas, isto é, entradas diferentes do padrão a + bi
                       numero = input("Digite o número em formato retangular")
                       numero = numero.replace(" ", "").replace("i", "j")
                       numero = complex(numero)
                       numeroPolar = RetParaPolar(numero)
                       print(f"O numero, em formato polar, possui modulo = {numeroPolar[0]} e angulo = {numeroPolar[1]} graus")
                   except ValueError:
                        print("Formato inválido! Digite no formato 'a+bi' ou 'a+bj'")
               case 2:                             # Converter de polar para retangular
                    num = []
                    num.append(float(input("Digite o modulo do seu numero complexo polar: ")))
                    num.append(float(input("Digite o angulo (em graus) do seu numero complexo polar: ")))
                    numero = tuple(num)
                    numeroRet = PolarParaRet(numero)
                    print("O numero, em formato retangular, é: ", + numeroRet)
               case 3:                             # Soma
                    try:                            # Trata as entradas indesejadas, isto é, entradas diferentes do padrão a + bi
                        numero1 = input("Digite o primeiro número em formato retangular")
                        numero1 = numero1.replace(" ", "").replace("i", "j")
                        numero1 = complex(numero1)
                        numero2 = input("Digite o segundo número em formato retangular")
                        numero2 = numero2.replace(" ", "").replace("i", "j")
                        numero2 = complex(numero2)
                        soma = SomaComplexa(numero1,numero2)
                        print("O resultado da soma é: ", + soma)
                    except ValueError:
                        print("Formato inválido! Digite no formato 'a+bi' ou 'a+bj'")    
               case 4:                             # Subtração
                   try:                            # Trata as entradas indesejadas, isto é, entradas diferentes do padrão a + bi
                       numero1 = input("Digite o primeiro número em formato retangular")
                       numero1 = numero1.replace(" ", "").replace("i", "j")
                       numero1 = complex(numero1)
                       numero2 = input("Digite o segundo número em formato retangular")
                       numero2 = numero2.replace(" ", "").replace("i", "j")
                       numero2 = complex(numero2)
                       subtract = SubComplexa(numero1,numero2)
                       print("O resultado da subtração é: ", + subtract)
                   except ValueError:
                        print("Formato inválido! Digite no formato 'a+bi' ou 'a+bj'")    
               case 5:                             # Multiplicação
                    try:                            # Trata as entradas indesejadas, isto é, entradas diferentes do padrão a + bi
                        numero1 = input("Digite o primeiro número em formato retangular")
                        numero1 = numero1.replace(" ", "").replace("i", "j")
                        numero1 = complex(numero1)
                        numero2 = input("Digite o segundo número em formato retangular")
                        numero2 = numero2.replace(" ", "").replace("i", "j")
                        numero2 = complex(numero2)
                        multiplic = MultComplexa(numero1,numero2)
                        print("O resultado da multiplicaçao é: ", + multiplic)
                    except ValueError:
                        print("Formato inválido! Digite no formato 'a+bi' ou 'a+bj'")    
               case 6:                             # Divisão
                    try:                            # Trata as entradas indesejadas, isto é, entradas diferentes do padrão a + bi
                        numero1 = input("Digite o primeiro número em formato retangular")
                        numero1 = numero1.replace(" ", "").replace("i", "j")
                        numero1 = complex(numero1)
                        numero2 = input("Digite o segundo número em formato retangular")
                        numero2 = numero2.replace(" ", "").replace("i", "j")
                        numero2 = complex(numero2)
                        divisao = DivComplexa(numero1,numero2)
                        print("O resultado da divisao é: ", + divisao)
                    except ValueError:
                        print("Formato inválido! Digite no formato 'a+bi' ou 'a+bj'")
        else:
            print("Opção inválida. Escolha entre 1 e 6.")
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido.")