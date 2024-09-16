import os
os.system

# Função para calcular a média de uma lista de números
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Inicialização das variáveis
numeros = []
pares = []   
impares = []
positivos = []
negativos = []

# Leitura de 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    
    # Verificar se o número é par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    # Verificar se o número é positivo ou negativo
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)

# Calcular maiores e menores números
maior_numero = max(numeros)
menor_numero = min(numeros)

# Calcular médias
media_pares = calcular_media(pares)
media_impares = calcular_media(impares)
media_total = calcular_media(numeros)

# Mostrar os resultados
print(f"\nQuantidade de números pares: {len(pares)}")
print(f"Quantidade de números ímpares: {len(impares)}")
print(f"Quantidade de números positivos: {len(positivos)}")
print(f"Quantidade de números negativos: {len(negativos)}")
print(f"Quantidade total de números inseridos: {len(numeros)}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_total:.2f}")

# Mostrar os números na ordem inversa
print("Números na ordem inversa:")
for num in reversed(numeros):
    print(num)
