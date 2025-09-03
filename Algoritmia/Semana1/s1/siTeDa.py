a = int(input())
b = int(input())

inicial_a = a
inicial_b = b

secuencia = [a, b]

while True:
    suma = secuencia[-2] + secuencia[-1]
    nuevo_digito = suma % 10
    
    secuencia.append(nuevo_digito)
    
    if secuencia[-2] == inicial_a and secuencia[-1] == inicial_b:
        break

linea_uno = " ".join(map(str, secuencia))
linea_dos = len(secuencia) - 2

print(linea_uno)
print(linea_dos)