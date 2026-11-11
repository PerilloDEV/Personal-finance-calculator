
import random

while True:
    print("Olá sou sua calculadora de gastos!💰 ")
    print("Estou aqui para facilitar sua organização financeira.📚")
    print("Vamos descobrir quanto dinheiro sobra no final?")

    print()
    nome = str(input("Qual seu nome? "))
    salario = float(input("Digite seu salário: "))
    despesa = float(input("Digite seu gasto mensal de despesas fixas (Ex: Água, luz, aluguel, Internet etc...): "))
    alimento = float(input("Digite seu gasto mensal com alimentação (Ex: Supermercado, restaurantes etc...): "))
    lazer = float(input("Digite o valor mensal destinado ao lazer (Ex: Passeios, entretenimento cinema etc...): "))
    pessoais = float(input("Digite seus gastos pessoais (Ex: Roupas, calçados, eletrônicos etc...): "))

    soma = 0

    soma = despesa + alimento + lazer + pessoais
    restante = salario - soma
    porcentagem = restante / salario * 100

    print()
    print(f"Total despesas: R$ {soma:.2f}")

    if restante < 0:
        print("Ops! Seus gastos ultrapassaram seu salário!😭 ")
    elif restante == 0:
        print("Você utilizou todo o seu salário. Não sobrou dinheiro!☹️")
    else:
        print(f"Seu saldo restante é: R$ {restante:.2f}")

    print()
    if porcentagem >= 30:
        print(f"Parabéns {nome}! Você conseguiu economizar mais de 30% do seu salário!🥳🎉 ")
    elif porcentagem >= 10:
        print("Você está no caminho certo!🚀 ")
    else:
        print("Vamos achar uma maneira de sobrar!🚨")

    print()
    print("Agora, vamos organizar seu salário com base nos dados que você me passou: ")

    porcD = despesa / salario * 100
    porcA = alimento / salario * 100
    porcL = lazer / salario * 100
    porcP = pessoais / salario * 100
    porcR = 100 - porcD - porcA - porcL - porcP

    if porcD <= 30:
        corD = "\033[92m"
    else:
        corD = "\033[91m"

    if porcA <= 20:
        corA = "\033[92m"
    else:
        corA = "\033[91m"

    if porcL <= 10:
        corL = "\033[92m"
    else:
        corL = "\033[91m"

    if porcP <= 10:
        corP = "\033[92m"
    else:
        corP = "\033[91m"

    if porcR >= 30:
        corR = "\033[92m"
    else:
        corR = "\033[91m"

    print("--------------------------------------------------")
    print("CATEGORIA         VALOR           %         IDEAL ")
    print("--------------------------------------------------")
    print(f"SALÁRIO:         {salario:}         100%        100% ")
    print(f"DESPESA:         {despesa}           {corD}{porcD:.0f}%\033[0m        30.0%     ")
    print(f"ALIMENTO:        {alimento}           {corA}{porcA:.0f}%\033[0m        20.0%     ")
    print(f"LAZER:           {lazer}           {corL}{porcL:.0f}%\033[0m        10.0%    ")
    print(f"PESSOAIS:        {pessoais}           {corP}{porcP:.0f}%\033[0m        10.0%   ")
    print(f"RESTANTE:        {restante}           {corR}{porcR:.0f}%\033[0m        30.0%    ")
    print("--------------------------------------------------")

    print()
    if porcD <= 30 and porcA <= 20 and porcL <= 10 and porcP <= 10:
        print("Seus gastos estão dentro das porcentagens recomendadas! ")
        print("Continue assim! Você está no caminho certo para uma vida financeira saudável.")
    else:
        print("Tem gastos que ultrapassam o limite recomendado. ")
        print("Não desanime! Reveja suas prioridades e identifique onde")
        print("é possível economizar. Pequenas mudanças fazem a diferença!")

    print()

    print("MENSAGEM MOTIVACIONAL:")
    print("A riqueza não está apenas em quanto você ganha, mas na disciplina de guardar uma parte daquilo que conquista.")
    print()

    resposta = input("Deseja realizar uma nova análise? ").strip().lower()

    if resposta == "sim":
        print("Vamos começar uma nova análise!")

    elif resposta == "nao" or resposta == "não":
        print("Muito obrigado por utilizar a calculadora!")
        break

    else:
        print("Resposta inválida! Vamos encerrar a calculadora.")
        break
