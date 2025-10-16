class program {
    
    // Defines a new command to make Karel turn right.
    void turnRight() {
        turnleft();
        turnleft();
        turnleft();
    }

    program () {
        // This is the main part of the program.
        
        // Loop 4 times, once for each side of the square.
        iterate (4) {
            
            // Each side requires 9 steps.
            // In each step, Karel picks up a beeper and then moves.
            iterate (9) {
                pickbeeper();
                move();
            }
            
            // After finishing a side, Karel turns right to face the next one.
            turnRight();
        }
        
        // The task is complete.
        turnoff();
    }
}