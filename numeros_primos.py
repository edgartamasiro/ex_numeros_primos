print('Programa que verifica se um número positivo é primo')
n = int(input('Digite o número: '))
e_primo = True
if (n % 2 == 0 and n != 2) or n <= 0 :
# verifica se o número é par, se é diferente de 2 e se é menor ou igual a 0
    e_primo = False
else:
    for i in range(n - 1, 1, -1) :
    # excetua as verificações de divisão por ele mesmo e por 1
        if n % i == 0 :
        # na primeira ocorrência de resto 0 retorna false e dá o break
            # print(i)
            e_primo = False
            break
print('{}: {}'.format(n, e_primo))

