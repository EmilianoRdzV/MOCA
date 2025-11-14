class program {
    program () {
        
        // --- 1. Esquina (1,1) ---
        // Karel ya está aquí.
        // Primero, limpia la esquina.
        while(nextToABeeper()) {
            pickbeeper();
        }
        // Segundo, pone los 3 zumbadores.
        iterate(3) {
            putbeeper();
        }
        
        // --- 2. Ir a la esquina (3,1) ---
        // Karel está viendo al Este
        move();
        move();
        
        // Ajustar esquina (3,1)
        while(nextToABeeper()) {
            pickbeeper();
        }
        iterate(3) {
            putbeeper();
        }
        
        // --- 3. Ir a la esquina (3,3) ---
        turnleft(); // Ver al Norte
        move();
        move();
        
        // Ajustar esquina (3,3)
        while(nextToABeeper()) {
            pickbeeper();
        }
        iterate(3) {
            putbeeper();
        }
        
        // --- 4. Ir a la esquina (1,3) ---
        turnleft(); // Ver al Oeste
        move();
        move();
        
        // Ajustar esquina (1,3)
        while(nextToABeeper()) {
            pickbeeper();
        }
        iterate(3) {
            putbeeper();
        }
    }
}