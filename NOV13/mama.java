class program {
    program () {
        
    
        while(notFacingSouth()) {
            turnleft();
        }
        while(frontIsClear()) {
            move();
        }
        while(notFacingWest()) {
            turnleft();
        }
        while(frontIsClear()) {
            move();
        }
       
        turnleft();
        turnleft();
        
        while(frontIsClear()) {
            while(nextToABeeper()) {
                pickbeeper();
            }
            move();
        }

        while(nextToABeeper()) {
            pickbeeper();
        }
        
    
        turnleft();
        
        while(frontIsClear()) {
            move();
        }
        
        // Ver al Este
        turnleft();
        turnleft();
        turnleft();
        
        move();
        

        turnleft();
        turnleft();
        turnleft();

        while(frontIsClear()) {
            move();
        }
        

        while(beepersInBag()) {
            putbeeper();
        }
    }
}