nome = 'Kauan'
idade = 16

num1 = input('Digite o primerio numero: ')
num1 = int(num1)

num2 = int(input('Digite o segundo numero: '))

# OPERADORES MATEMATICOS
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2
divi_inteira = num1 // num2
expo = num1 ** num2
modulo = num1 % num2

'''
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)
print(num1 <= 100)
'''

print(num1 <= 100 and num2 <=100 or (num1 + num2) > 100)


'''
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# ATRIBUIÇÃO DE VALORES
num1 += 1
num1 -= 1
num1 /= 1
num1 *= 1

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {divi}')
print(f'Divisão Formatada: {divi:.2f}')
print(f'Divisão Inteira: {divi_inteira}')
print(f'Exponenciação: {expo}')
print(f'Resto da Divisão: {modulo}')
print()
print(f'O numero digitado + 1 é: {num1}')
'''