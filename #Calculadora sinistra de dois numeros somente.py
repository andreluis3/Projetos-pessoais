#Calculadora 


print(" CALCULADORA MANUAL")
def calculadora():
    while True: 
        operacao = input("escolha a operação que você vai utilizar (+, -, *, /) ou 'sair' para encerrar:    " )

        if operacao == "sair": 
            print("Obrigado, até mais!")
            break

        if operacao not in ['+', '-', '*', '/'  ]:
            print("Operação inválida, tente novamente.")
            continue

        n1 = float(input("Digite o primeiro número:        "))
        n2 = float(input("Digite o segundo número   "))

        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '/':
            resultado = n1 / n2        
        else:
            print("Erro: Divisão por zero!")
            continue

        print(f"Resultado: {resultado}") 

        continuar = input("Você deseja realizar outra operação ? (sim/nao): ").lower()
        if continuar == 'nao':  
            print("Fim do programa")
            break

calculadora() 


