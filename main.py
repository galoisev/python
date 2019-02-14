# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


from methodes import *  
    
    

if __name__ == "__main__":
    # execute only if run as a script
  
    
    n = 3
    A = np.eye(n)
    A = ([[1 , 2 , 3],[2,20,26],[3,26,70]])
    print "A",A
    b = np.array([7 , 50 , 102])    
    print "b=",b
    # init.
    x0  = np.linspace(1,3,3)
   
    
    it=0
    delta = 1E3
    precision = 1.e-12
    while(delta > precision):
        x1 = GradConj(x0,A,b)
        b_calc = np.dot(A,x1)
        delta=np.sqrt( np.vdot(x1-x0,x1-x0) )
        if it>1e6:
            break
        it=it+1
        x0=x1
    print "Precision=",precision,", Nbre iterations=",it
    print "b_calc=",b_calc
    



    


    
    


    
