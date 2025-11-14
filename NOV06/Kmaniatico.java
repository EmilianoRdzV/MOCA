class program {
    program () {
        while(notFacingEast()) {
            turnleft();
        }
        putbeeper();
        while(frontIsClear()) {
            move();
            if(frontIsClear()) {
                move();
                putbeeper();
            }
        }
    }
}
