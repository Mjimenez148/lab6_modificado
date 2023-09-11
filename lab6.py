import matplotlib.pyplot as plt


print("Laboratorio de Suma Acumulativa")
cant = int(input("Ingrese cantidad de numeros a sumar: "))

acumulativa = 0
sumas_acumulativas = []

colores = ['pink', 'red', 'purple', 'orange',  'magenta']

for _ in range(cant):
    num = float(input("Ingrese un número: "))
    acumulativa += num
    sumas_acumulativas.append(acumulativa)

print("La suma acumulativa de los números es:", acumulativa)


etiquetas = [str(i + 1) for i in range(cant)] 
plt.bar(etiquetas, sumas_acumulativas, color=colores)
plt.xlabel('Número de entrada', color = 'blue')
plt.ylabel('Suma Acumulativa', color = 'green')
plt.title('Suma Acumulativa ', color = 'red')
plt.show()


