class program {
    program() {
        while (frontIsClear()) {
            if (leftIsClear()) {
                putbeeper();
            }
            move();
        }
        if (leftIsClear()) {
            putbeeper();
        }
    }
}
