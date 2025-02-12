import numpy as np
import matplotlib.pyplot as plt

# Véletlenszerű adatok generálása (Lakosság tízezrekben, Autók száma tízezrekben)
np.random.seed(42)
lakossag = np.random.randint(50, 500, 20)  # Városok lakossága 50k és 500k között
autok = lakossag * 0.4 + np.random.randint(-50, 50, 20)  # Autók száma = 0.4 * Lakosság + zaj

# Alakítsuk át NumPy tömbökké
X = lakossag.reshape(-1, 1)  # Bemenet (lakosság)
y = autok.reshape(-1, 1)     # Kimenet (autók száma)

# Bias (x0 = 1) hozzáadása a mátrixhoz
X_b = np.c_[np.ones((X.shape[0], 1)), X]  

# Theta kiszámítása a normál egyenlettel
theta_legjobb = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Előrejelző függvény
def josol_autok(lakossag):
    X_uj = np.array([[1, lakossag]])  # Bias hozzáadása
    return X_uj.dot(theta_legjobb)[0, 0]

# Teszteljük egy 300 ezres várossal
teszt_lakossag = 300  # 300 ezer fős város
josolt_autok = josol_autok(teszt_lakossag)
print(f"Egy {teszt_lakossag} ezres városban várható autók száma: {josolt_autok:.2f} ezer")

# Adatok és regressziós egyenes kirajzolása
plt.scatter(lakossag, autok, color="blue", label="Valós adatok")
plt.plot(lakossag, X_b.dot(theta_legjobb), color="red", label="Lineáris regressziós egyenes")
plt.xlabel("Lakosság száma (ezer fő)")
plt.ylabel("Autók száma (ezer)")
plt.title("Lineáris regresszió: Lakosság vs. Autók száma")
plt.legend()
plt.show()
