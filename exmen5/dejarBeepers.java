class program {
    program () {
        putbeeper();
        while(frontIsClear()){
            move();
            putbeeper();
        }
    }
}