class program {
    program() {
        while (frontIsClear()) {
            putbeeper();
            move();
        }
        putbeeper();

        turnleft();
        turnleft();

        while (frontIsClear()) {
            pickbeeper();
            while (frontIsClear()) {
                move();
            }
            putbeeper();
            turnleft();
            turnleft();
            move();
            while (nextToABeeper()) {
                move();
            }
            turnleft();
            turnleft();
            move();
        }
    }
}
