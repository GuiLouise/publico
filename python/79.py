lista = []
while True:
    try:
        valor = int(input('Digite um valor: '))
        if valor in lista:
            print('Valor duplicado. vamos tentar de novo!')
            valor = int(input('Digite um valor: '))
        else:
            lista.append(valor)
    except ValueError:
        print('APENAS NUMEROS')
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N': 
        break
    elif continuar != 'S':
        continuar =str(input(f'"{continuar}", não é valido! Use apenas S ou N\n Quer continuar? [S/N] '))
lista.sort()
print(f'Os valores digitados foram: {lista}')