nome = input("Ana Clara Lanzoni")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovacao = 180

#Coleta das notas dos 3 periodos
for i in range(1, quantidade_trimestre +1):
    nota = float(input("informe a nota{i}º período:"))
soma_notas +=nota

print("-" * 30)
print(f"Estudante: {nome}")
print(f"pontuação total: {soma_notas}")

#Verifica o status de aprovação
if soma_notas >= meta_aprovacao:
    print("Status: APROVADO! FINALMENTE!")
else:
    pontos_faltantes = meta_aprovacao - soma_notas
    print("Status: TENTE OUTRA VEZ!!")
    print(f"Faltaram {pontos_faltantes} pontos para atingir o minimo de {meta_aprovacao}.")