class program {
    program () {
        
        // Bucle principal: se ejecuta mientras Karel NO esté en el zumbador de salida.
        while(notNextToABeeper()) {
            
            // 1. REGLA DE LA MANO DERECHA:
            // Si la derecha está libre (una esquina "abierta" hacia afuera).
            if(rightIsClear()) {
                
                // Gira a la derecha (dando 3 vueltas a la izquierda).
                turnleft();
                turnleft();
                turnleft();
                
                // Avanza un paso para "pegarse" a la nueva pared.
                move();
                
            } else {
                
                // 2. La derecha está bloqueada por una pared.
                // Revisa si puede seguir recto.
                if(frontIsClear()) {
                    
                    // 2a. Sigue recto por el pasillo.
                    move();
                    
                } else {
                    
                    // 2b. Derecha Y frente están bloqueados (esquina "cerrada").
                    // La única salida es girar a la izquierda.
                    turnleft();
                }
            }
        }
    }
}class program {
    program () {
        
        // Bucle principal: se ejecuta mientras Karel NO esté en el zumbador de salida.
        while(notNextToABeeper()) {
            
            // 1. REGLA DE LA MANO DERECHA:
            // Si la derecha está libre (una esquina "abierta" hacia afuera).
            if(rightIsClear()) {
                
                // Gira a la derecha (dando 3 vueltas a la izquierda).
                turnleft();
                turnleft();
                turnleft();
                
                // Avanza un paso para "pegarse" a la nueva pared.
                move();
                
            } else {
                
                // 2. La derecha está bloqueada por una pared.
                // Revisa si puede seguir recto.
                if(frontIsClear()) {
                    
                    // 2a. Sigue recto por el pasillo.
                    move();
                    
                } else {
                    
                    // 2b. Derecha Y frente están bloqueados (esquina "cerrada").
                    // La única salida es girar a la izquierda.
                    turnleft();
                }
            }
        }
    }
}