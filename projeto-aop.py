# VALIDAR NOTAS
def validar_nota(nota, min_value, max_value):
    while True:
        if nota < min_value or nota > max_value:
            print(f"Valor Inválido, digitar entre {min_value} e {max_value}.")
            nota = float(input("Digite novamente: "))
        else:
            break
    return nota

# SOMANDO NOTAS DO MÓDULO
def calc_soma_modulo(aop1, aop2, aop3, prova_regular):
    return abs(aop1) + abs(aop2) + abs(aop3) + abs(prova_regular)

# SOMANDO MÉDIA DO MÓDULO
def calc_media_modulo(aop1, aop2, aop3, prova_regular, prova_recuperacao=None):
    if prova_recuperacao is not None:
        return (abs(aop1) + abs(aop2) + abs(aop3) + abs(prova_regular) + abs(prova_recuperacao)) / 2
    else:
        return (abs(aop1) + abs(aop2) + abs(aop3) + abs(prova_regular)) / 2

# LISTA STATUS DOS ALUNO
status_alunos = []

# APROVADOS E REPROVADOS
aprovados = 0
reprovados = 0

# RANGE NOTAS DOS ALUNOS
for i in range(100):
    print(f"Aluno {i + 1}:")
    aop1 = validar_nota(float(input("Nota na AOP1 (0 a 1): ")), 0, 1)
    aop2 = validar_nota(float(input("Nota na AOP2 (0 a 2): ")), 0, 2)
    aop3 = validar_nota(float(input("Nota na AOP3 (0 a 1): ")), 0, 1)
    prova_regular = validar_nota(float(input("Nota da Prova Regular (0 a 6): ")), 0, 6)

    soma_modulo = calc_soma_modulo(aop1, aop2, aop3, prova_regular)

    if soma_modulo >= 7:
        status_alunos.append("Aprovado")
        aprovados += 1
    else:
        prova_recuperacao = validar_nota(float(input("Nota da Prova de Recuperação (0 a 10): ")), 0, 10)
        media_modulo = calc_media_modulo(aop1, aop2, aop3, prova_regular, prova_recuperacao)
        if media_modulo >= 5:
            status_alunos.append("Aprovado")
            aprovados += 1
        else:
            status_alunos.append("Reprovado")
            reprovados += 1

# PORCETAGEM DE APROVADOS E REPROVADOS
total_alunos = len(status_alunos)
porcentagem_aprovados = (aprovados / total_alunos) * 100
porcentagem_reprovados = (reprovados / total_alunos) * 100

# RESULTADO STATUS DOS ALUNOS
print("\nStatus dos Alunos:")
for i, status in enumerate(status_alunos, start=1):
    print(f"Aluno {i}: {status}")

print("\nEstatísticas:")
print(f"Porcentagem de Alunos Aprovados: {porcentagem_aprovados}%")
print(f"Porcentagem de Alunos Reprovados: {porcentagem_reprovados}%")