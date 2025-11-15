class program {
    program () {
        
        while(nextToABeeper()) {
            
            // INTENTA CONTAR 1 (Norte)
            pickbeeper();
            
            if(notNextToABeeper()) {
                // --- INSTRUCCIÓN: 1 ZUMBADOR (NORTE) ---
                // Gira hasta ver al Norte
                while(notFacingNorth()) {
                    turnleft();
                }
                move();
                
            } else {
                // INTENTA CONTAR 2 (Este)
                pickbeeper();
                
                if(notNextToABeeper()) {
                    // --- INSTRUCCIÓN: 2 ZUMBADORES (ESTE) ---
                    // Gira hasta ver al Este
                    while(notFacingEast()) {
                        turnleft();
                    }
                    move();
                    
                } else {
                    // INTENTA CONTAR 3 (Sur)
                    pickbeeper();
                    
                    if(notNextToABeeper()) {
                        // --- INSTRUCCIÓN: 3 ZUMBADORES (SUR) ---
                        // Gira hasta ver al Sur
                        while(notFacingSouth()) {
                            turnleft();
                        }
                        move();
                        
                    } else {
                        // --- INSTRUCCIÓN: 4 ZUMBADORES (OESTE) ---
                        // Si no fue 1, 2 o 3, debe ser 4.
                        pickbeeper();
                        
                        // (Limpia por si acaso hay más de 4)
                        while(nextToABeeper()) {
                            pickbeeper();
                        }
                        
                        // Gira hasta ver al Oeste
                        while(notFacingWest()) {
                            turnleft();
                        }
                        move();
                    }
                }
            }
        }
        
    }
}