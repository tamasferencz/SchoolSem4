import numpy as np

# Bemeneti számok (x)
x = np.array([1, 2, 3, 4, 5])  

# Kimeneti számok (y) - mindig hozzáadunk 5-öt
y = np.array([6, 7, 8, 9, 10])  

print("Bemenetek:", x)
print("Kimenetek:", y)

# Számoljuk ki a legjobb theta0 értéket
theta0 = np.mean(y - x)  # atlag - mean()

print("A megtanult theta0 érték:", theta0)

def josol(szam):
    return szam + theta0

# Próbáljuk ki egy új számmal (pl. 10)
teszt_szam = 25
josolt_ertek = josol(teszt_szam)
print(f"{teszt_szam} + 5 = {josolt_ertek}")
