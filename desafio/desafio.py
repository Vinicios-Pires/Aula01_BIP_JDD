# Desafio: Calcular o bônus de um funcionário

CONSTANT_BONUS = 1000

username = input("Digite seu nome: ")

salary = float(input("Digite seu salário: "))

bonus = float(input("Digite o bônus: ")) / 100

bonus_value = CONSTANT_BONUS + salary * bonus

print(f"Olá {username}, seu salário é {salary} e seu bônus é {bonus_value}.")
