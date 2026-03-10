# # # # numero = int(input("Digite um número: "))
# # # # i = 1
# # # # while i <= numero:
# # # #     print(i)
# # # #     i = i + 2
    
# # # i = 1

# # # while i <= 50:
# # #     print(i)
# # #     i = i + 1

# # # i= 52
# # # while i<= 100:
# # #     print(i)
# # #     i = i + 2
# # # número=float(input("Digite uma tabuada"))

# # numero=int(input("Digite um numero de 0 a 10: "))

# # while numero < 0 or numero > 10:
# #     print("numero invalido tente novamente")
# #     numero=int(input("digite um numero de 0 a 10: "))

# # # print("numero aceito")

# contador = 0
# soma = 0

# numero = int(input("Digite um número (0 para parar): "))

# while numero != 0:
#     soma += numero
#     contador += 1
#     numero = int(input("Digite outro número (0 para parar): "))

# print("Quantidade de números digitados:", contador)
# print("Somatória dos números:", soma)
# media = soma / contador * (contador > 0)
# print("Média aritmética:", media)


x = 0
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    x += numero

print(f"A somatória dos 10 números é: {x}")