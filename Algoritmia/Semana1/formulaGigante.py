x, y, z = map(float, input().split())

# numerador de la fraccion principal
parteSuperiorNumerador = (2 * x + y) / z
parteSuperiorCubo = y**3 - z
numerador = parteSuperiorNumerador * parteSuperiorCubo

# denominador de la fraccion principal
fraccionInferior = (x + 2*y + 3*z) / (z - 2*y - 3*x)
cuadradosInferior = x**2 + z**2
denominador = fraccionInferior + cuadradosInferior

resultadoFinal = numerador / denominador

print(resultadoFinal)