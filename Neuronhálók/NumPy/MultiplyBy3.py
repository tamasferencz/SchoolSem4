import numpy as np

# Bemeneti számok (x)
x = np.array([1, 2, 3, 4, 5])  

# Kimeneti számok (y) - minden számot megszorzunk 3-mal
y = np.array([3, 6, 9, 12, 15])  

print("Bemenetek:", x)
print("Kimenetek:", y)

# Számoljuk ki a legjobb theta1 értéket
theta1 = np.mean(y / x)  

print("A megtanult theta1 érték:", theta1)

def josol(szam):
    return theta1 * szam

# Próbáljuk ki egy új számmal (pl. 10)
teszt_szam = 10
josolt_ertek = josol(teszt_szam)
print(f"{teszt_szam} * 3 = {josolt_ertek}")
