class program {
    program () {
        
        // --- 1. Cuadrado Grande (3 Zumbadores) ---
        // Karel está en (2,2) viendo al Norte.
        // Es un cuadrado de 4 movimientos por lado.
        
        iterate(4) { // Repite 4 veces (para los 4 lados)
            
            iterate(4) { // Repite 4 movimientos/segmentos por lado
                putbeeper();
                putbeeper();
                putbeeper();
                
                // Mover solo si el frente está libre
                if(frontIsClear()) {
                    move();
                }
            }
            
            // Gira a la derecha (turnRight)
            turnleft();
            turnleft();
            turnleft();
        }
        
        // --- 2. Moverse al siguiente cuadrado (con precaución) ---
        // Karel terminó en (2,2) viendo al Norte.
        
        if(frontIsClear()) {
            move(); // Mover a (2,3)
        }
        turnleft(); turnleft(); turnleft(); // Girar a la derecha (ver Este)
        
        if(frontIsClear()) {
            move(); // Mover a (3,3)
        }
        turnleft(); // Girar a la izquierda (ver Norte)
        
        
        // --- 3. Cuadrado Mediano (2 Zumbadores) ---
        // Karel está en (3,3) viendo al Norte.
        // Es un cuadrado de 2 movimientos por lado.
        
        iterate(4) { // 4 lados
            iterate(2) { // 2 movimientos por lado
                putbeeper();
                putbeeper();
                
                if(frontIsClear()) {
                    move();
                }
            }
            // Gira a la derecha
            turnleft();
            turnleft();
            turnleft();
        }
        
        // --- 4. Moverse al centro (con precaución) ---
        // Karel terminó en (3,3) viendo al Norte.
        
        if(frontIsClear()) {
            move(); // Mover a (3,4)
        }
        turnleft(); turnleft(); turnleft(); // Girar a la derecha (ver Este)
        
        if(frontIsClear()) {
            move(); // Mover a (4,4)
        }
        
        // --- 5. Poner el zumbador central ---
        putbeeper();
    }
}