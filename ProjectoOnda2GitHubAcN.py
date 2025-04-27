import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Entradas do usuário
amplitude1 = float(input("Insira a amplitude da primeira onda: "))
fase1 = float(input("Insira a fase da primeira onda (em graus): "))
amplitude2 = float(input("Insira a amplitude da segunda onda: "))
fase2 = float(input("Insira a fase da segunda onda (em graus): "))

# Verificação do tipo de interferência
diferenca_fase = abs(fase1 - fase2) % 360
if diferenca_fase == 0 or diferenca_fase == 360:
    tipo = "Construtiva"
elif diferenca_fase == 180:
    tipo = "Destrutiva"
else:
    tipo = "Parcial"

print(f"Tipo de interferência: {tipo}")

# Configurações do gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(- (amplitude1 + amplitude2) - 1, (amplitude1 + amplitude2) + 1)
ax.set_title("Interferência de Ondas")
ax.set_xlabel("Espaço")
ax.set_ylabel("Amplitude")

x = np.linspace(0, 4 * np.pi, 1000)

linha_onda1, = ax.plot([], [], label='Onda 1', color='blue')
linha_onda2, = ax.plot([], [], label='Onda 2', color='green')
linha_resultante, = ax.plot([], [], label='Onda Resultante', color='red')

ax.legend()

# Inicialização da animação
def init():
    linha_onda1.set_data([], [])
    linha_onda2.set_data([], [])
    linha_resultante.set_data([], [])
    return linha_onda1, linha_onda2, linha_resultante

# Função de animação
def animar(frame):
    t = frame / 10
    y1 = amplitude1 * np.sin(x - t + np.radians(fase1))
    y2 = amplitude2 * np.sin(x - t + np.radians(fase2))
    y_total = y1 + y2

    linha_onda1.set_data(x, y1)
    linha_onda2.set_data(x, y2)
    linha_resultante.set_data(x, y_total)
    return linha_onda1, linha_onda2, linha_resultante

# Criar animação
anim = FuncAnimation(fig, animar, init_func=init, frames=200, interval=50, blit=True)
plt.show()