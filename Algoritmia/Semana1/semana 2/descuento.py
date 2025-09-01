monto = int(input())

montoFinal = monto * 0.85 if monto > 1000 else monto

print (f"{montoFinal:.2f}")
