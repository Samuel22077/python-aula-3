#a=float(input("Digite um número: "))
#b=float(input("Digite outro número: "))
#if a>b:
#    print("O primeiro é maior")
#    print(a)
 #   print("fim do if")
#if b>a:
#    print("O segundo é maior")
#    print(b)
 #   print("fim do if")

#a=float(input("Digite um numero:"))
#if a>0:
    #print("Positivo!")
#else:
  #  print("Negativo!")

#segunda=1
##terça=2
#quarta=3
#sexta=5
#sabado=6
#domingo=7
#a=float(input("Digite um número"))
#if a==1:
    #print("Segunda")
#if a ==2:
    #print("Terça")
#if a==3:
  #  print("Quarta")
#if a==4:
   # print("Quinta")
#if a==5:
  #  print("Sexta")
#if a==6:
   # print("Sábado")
#if a==7
   # print("Domingo")

#salario=float(input("Qual é o salário do funcionário R$ "))
#if salario>1250:
   # print(f"Seu novo salário é de: R$ {salario + (salario * 0.10):.2f}")
#else:
   # print(f"Seu novo salário é de: R$ {salario + (salario * 0.15):.2f}")

#idade_carro=float(input("Qual é a idade do carro? "))
#if idade_carro<=3:
    #print("É novo! ")
#else:
    #print("É velho! ")


#distancia_percorrer=float(input("Quanto kms deseja percorrer? "))
#if distancia_percorrer<200:
 #   print(f"O preço da passagem é de: {distancia_percorrer * 0.50:.2f}")
#else:
  #  print(f"O preço da passagem é de: {distancia_percorrer * 0.45:.2f}")

from math import pi, ceil


altura= float(input("Digite a altura: "))
raio= float(input("Digite a raio: "))

#calculos
perimetro= 2 * pi * raio
lateral= altura* perimetro
base= pi * (raio ** 2)
cilindro= base + lateral


#Litros
litro= cilindro / 3

# Latas
latas= ceil(cilindro/5)

# Calculo do preço unitario
if latas == 1:
    preco_unitario = 50
elif latas == 2:
    preco_unitario = 48
elif latas == 3:
    preco_unitario= 46
else:
    preco_unitario= 45 

#Calculo do custo total
custo_total=latas*preco_unitario

print("\nÁrea total: {:.2f} m²" .format(cilindro))
print("Litros necessários: {:.2f}L" .format(litro))
print("Quantidade de latas: " , latas)
print("Preço Unitário da Lata: R$ " ,preco_unitario)
print("Custo total: R$ " , custo_total)








