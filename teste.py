# Questão 1: Cálculo do valor da variável SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print("Questão 1: SOMA =", SOMA)

# Questão 2: Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b or num == 0

fibonacci_test_number = 21  # número para testar
if is_fibonacci(fibonacci_test_number):
    print(f"Questão 2: O número {fibonacci_test_number} pertence à sequência de Fibonacci.")
else:
    print(f"Questão 2: O número {fibonacci_test_number} não pertence à sequência de Fibonacci.")

# Questão 3: Faturamento diário de uma distribuidora
faturamento_diario = [2000, 2500, 1800, 0, 2700, 3000, 0, 3500, 3800, 4000, 0, 0, 4200, 2300, 2200]

# Remover dias sem faturamento
faturamento_valido = [dia for dia in faturamento_diario if dia > 0]

# Menor e maior valor de faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Cálculo da média mensal
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Dias com faturamento superior à média
dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_faturamento)

print(f"Questão 3: Menor faturamento = {menor_faturamento}")
print(f"Questão 3: Maior faturamento = {maior_faturamento}")
print(f"Questão 3: Dias com faturamento acima da média = {dias_acima_da_media}")

# Questão 4: Percentual de representação do faturamento mensal por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}

print("Questão 4: Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# Questão 5: Inverter uma string sem usar funções prontas
def inverter_string(string):
    resultado = ""
    for char in string:
        resultado = char + resultado
    return resultado

string_original = "Distribuidora"
string_invertida = inverter_string(string_original)
print(f"Questão 5: String invertida = {string_invertida}")