import matplotlib.pyplot as plt
import numpy as np

def draw_lucie(num_sauts, p, q, rayon=0.5):
    theta = np.linspace(0, 2 * np.pi, 100)
    x_terrain = rayon * np.cos(theta)
    y_terrain = rayon * np.sin(theta)

    plt.plot(x_terrain, y_terrain, label='Terrain circulaire')

    lucie_x = []
    lucie_y = []

    for k in range(num_sauts + 1):
        theta_saut = (p / q) * 2 * k * np.pi
        lucie_x.append(rayon * np.cos(theta_saut))
        lucie_y.append(rayon * np.sin(theta_saut))

    plt.scatter(lucie_x, lucie_y, color='red', label='Lucie la puce')
    plt.plot(lucie_x, lucie_y, linestyle='-', color='blue', label='Trace de Lucie')

    # Calcul des coordonnées de M et N
    theta_M = (1 / (2 * np.pi), (p / q) * 2 * num_sauts * np.pi)
    theta_N = (1 / (2 * np.pi), (p / q) * 2 * (num_sauts + 1) * np.pi)


    plt.title(f"Lucie la puce - {num_sauts} sauts (p/q = {p}/{q})")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.axis('equal')
    plt.show()

# Exemple d'utilisation avec 5 sauts, p/q = 2/5
draw_lucie(6, 3, 15)
