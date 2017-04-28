from numpy import exp, array, random, dot, mean, abs

import numpy

girdi = array([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) 


gerceksonuc = array([[0, 1, 1]]).T
                    
agirlik = array([[1.0, 1.0, 1.0]]).T # -1 ile 1 arasında rastgele ağırlık
                
for tekrar in range(100000):
    hucredegeri = dot(girdi,agirlik)
    tahmin = 1 / (1 + exp(-hucredegeri)) 
    agirlik = agirlik + dot(girdi.T, ((gerceksonuc - tahmin) * tahmin * (1 - tahmin)))
    print(str(numpy.mean(numpy.abs(gerceksonuc-tahmin))))
 

print(1/(1+exp(-(dot(array([1,0,0]),agirlik)))))