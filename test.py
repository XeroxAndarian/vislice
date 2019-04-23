import math

def izpis_vseh_praštevil_do_200():
    seznam = []
    for i in range(200):
        if i == 1 or i == 0:
            pass
        else:
            for j in range(i):
                if math.gcd(i,j) == j:
                    for a in range(100):
                        if a * j != i:
                            seznam.append(i)
            else: 
                pass
    return seznam


izpis_vseh_praštevil_do_200()



