import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações do gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2.5, 2.5)
ax.set_title("Interferência de Ondas")
ax.set_xlabel("Espaço")
ax.set_ylabel("Amplitude")

# Eixos x fixo
x = np.linspace(0, 4 * np.pi, 1000)

# Linhas que serão animadas
linha_onda1, = ax.plot([], [], label='Onda 1', color='blue')
linha_onda2, = ax.plot([], [], label='Onda 2', color='green')
linha_resultante, = ax.plot([], [], label='Interferência', color='red')

ax.legend()
# Função de inicialização

#Entrada de usuario
Amplitude1 = float(input("Digite a amplitude da primeira onda : "))
fase1 = float(input("Digite a fase da primeira onda : "))
Amplitude2 = float(input("Digite a amplitude da segunda onda : "))
fase2 = float(input("Digite a fase da segunda onda : "))

#calculo das fases
diferenca_fase = abs(fase1 - fase2) % 360
if diferenca_fase == 0 or diferenca_fase == 360:
    tipo = "Construtiva"
elif diferenca_fase == 180 :
    tipo = "Destrutiva"
else :
    tipo = "Parcial" 
print(f"A interferencia de onda e {tipo}")

def init():
    linha_onda1.set_data([], [])
    linha_onda2.set_data([], [])
    linha_resultante.set_data([], [])
    return linha_onda1, linha_onda2, linha_resultante

# Função de animação
def animar(frame):
    t = frame / 10
    y1 = np.sin(x - t)
    y2 = np.sin(x + t)
    y_total = y1 + y2
    repeat=False

    linha_onda1.set_data(x, y1)
    linha_onda2.set_data(x, y2)
    linha_resultante.set_data(x, y_total)
    return linha_onda1, linha_onda2, linha_resultante

# Criar animação
anim = FuncAnimation(fig, animar, init_func=init, frames=200, interval=50, blit=True)
plt.show()