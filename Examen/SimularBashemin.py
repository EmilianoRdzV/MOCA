def simular_bashemin():
    num_operaciones = int(input())

    parking_lot_list = []  # Lista para simular el carril, el último elemento es el más cercano a la salida
    cars_in_lot_set = set()   # Conjunto para verificar rápidamente si un auto está adentro
    move_counts = {}      # Diccionario para {placa: numero_de_movimientos}

    for _ in range(num_operaciones):
        linea = input().split()
        operacion = linea[0]
        placa = int(linea[1])

        if operacion == 'E': # Entrada
            if placa not in move_counts: # Inicializar contador si es la primera vez que vemos el auto
                move_counts[placa] = 0
            
            if len(parking_lot_list) < 10:
                parking_lot_list.append(placa)
                cars_in_lot_set.add(placa)
                # No se imprime nada en la entrada exitosa según los ejemplos
            else:
                print(f"ESTACIONAMIENTO LLENO {placa} NO PUDO ENTRAR")
        
        elif operacion == 'S': # Salida
            # Paso 1: El auto 'placa' intenta salir, esto cuenta como un "evento de salida" para él.
            # Su contador de movimientos se incrementa aquí para reflejar esta intención o acción de salida.
            # Este valor actualizado se usará en el mensaje "SALIO..."
            move_counts[placa] = move_counts.get(placa, 0) + 1
            contador_actual_salida = move_counts[placa]
            
            print(f"SALIO {placa} CON {contador_actual_salida} MOVIMIENTOS")

            # Paso 2: Si el auto está físicamente en el estacionamiento, realizar los movimientos.
            if placa in cars_in_lot_set:
                autos_bloqueadores_temporales = []
                
                # Sacar los autos que están encima (más cerca de la salida) del auto objetivo
                while parking_lot_list[-1] != placa:
                    auto_bloqueador = parking_lot_list.pop()
                    cars_in_lot_set.remove(auto_bloqueador)
                    
                    # Este es un movimiento físico para el auto bloqueador
                    move_counts[auto_bloqueador] = move_counts.get(auto_bloqueador, 0) + 1
                    autos_bloqueadores_temporales.append(auto_bloqueador)
                
                # Sacar el auto objetivo (su move_count ya fue incrementado por el evento 'S')
                auto_objetivo = parking_lot_list.pop()
                cars_in_lot_set.remove(auto_objetivo)
                
                # Volver a meter los autos bloqueadores en el orden inverso al que salieron
                while autos_bloqueadores_temporales:
                    auto_a_reingresar = autos_bloqueadores_temporales.pop()
                    parking_lot_list.append(auto_a_reingresar)
                    cars_in_lot_set.add(auto_a_reingresar)
            # Si el auto no estaba en el estacionamiento, solo se imprimió el mensaje "SALIO..."
            # con su contador de intentos de salida actualizado.

    # Al final de todas las operaciones
    print("AUTOS EN BASHEMIN")
    if not parking_lot_list:
        print("NINGUNO")
    else:
        # Imprimir desde el más cercano a la salida hasta el más profundo
        for i in range(len(parking_lot_list) - 1, -1, -1):
            placa_actual = parking_lot_list[i]
            # Usar .get(placa_actual, 0) por si un auto entró pero nunca se movió (mc aún no tiene la placa)
            # Aunque la lógica de 'E' ya inicializa move_counts.
            print(f"{placa_actual} CON {move_counts.get(placa_actual, 0)} MOVIMIENTOS")

if __name__ == "__main__":
    simular_bashemin()