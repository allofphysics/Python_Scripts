def CoprimesCounting(array):
        def coprime(a,b):
            minimum = min(a,b)
            return [x==1 for x in xrange(minimum,0,-1) if a%x==0 and b%x==0][0]
         
        return [[int(coprime(x,y)) for x in array ]for y in array ]
