def resolver():
    numL = int(input())
    sec = [''] * numL
    
    def gen(k):
        if k == numL:
            print("".join(sec))
            return
            
        # 1. Prueba 'A'
        sec[k] = 'A'
        gen(k + 1)
        
        # 2. Prueba 'X'
        sec[k] = 'X'
        gen(k + 1)
            
    gen(0)

resolver()