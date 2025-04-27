import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Configurações iniciais
amplitude1_inicial = 1
fase1_inicial = 0
amplitude2_inicial = 1
fase2_inicial = 0

# Gráfico
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)  # espaço para sliders
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-4, 4)
ax.set_title("Interferência de Ondas")
ax.set_xlabel("Espaço")
ax.set_ylabel("Amplitude")

x = np.linspace(0, 4 * np.pi, 1000)

linha_onda1, = ax.plot([], [], label ='Onda 1', color ='blue')
linha_onda2, = ax.plot([], [], label ='Onda 2', color ='green')
linha_resultante, = ax.plot([], [], label='Onda Resultante', color='red')

ax.legend()

# Espaços dos sliders
ax_amp1 = plt.axes([0.1, 0.25, 0.8, 0.03])
ax_fase1 = plt.axes([0.1, 0.20, 0.8, 0.03])
ax_amp2 = plt.axes([0.1, 0.15, 0.8, 0.03])
ax_fase2 = plt.axes([0.1, 0.10, 0.8, 0.03])

# Sliders
slider_ampli1 = Slider(ax_amp1, 'Amplitude 1', 0.1, 3.0, valinit=amplitude1_inicial)
slider_fase1 = Slider(ax_fase1, 'Fase 1 (graus)', 0, 360, valinit=fase1_inicial)
slider_amp2 = Slider(ax_amp2, 'Amplitude 2', 0.1, 3.0, valinit=amplitude2_inicial)
slider_fase2 = Slider(ax_fase2, 'Fase 2 (graus)', 0, 360, valinit=fase2_inicial)

# Função para determinar o tipo de interferência
def tipo_interferencia(fase1, fase2):
    diferenca_fase = abs(fase1 - fase2) % 360
    if diferenca_fase == 0 or diferenca_fase == 360:
        return "Construtiva"
    elif diferenca_fase == 180:
        return "Destrutiva"
    else:
        return "Parcial"

# Inicialização da animação
def iniciar():
    linha_onda1.set_data([], [])
    linha_onda2.set_data([], [])
    linha_resultante.set_data([], [])
    return linha_onda1, linha_onda2, linha_resultante

# Função de animação
def animar(frame):
    t = frame / 10
    amp1 = slider_amp1.val
    fase1 = slider_fase1.val
    amp2 = slider_amp2.val
    fase2 = slider_fase2.val
#calculo das amplitudes pela formula 
    y1 = amp1 * np.sin(x - t + np.radians(fase1))
    y2 = amp2 * np.sin(x - t + np.radians(fase2))
    y_total = y1 + y2

    linha_onda1.set_data(x, y1)
    linha_onda2.set_data(x, y2)
    linha_resultante.set_data(x, y_total)

    # Atualizar o título com o tipo de interferência
    tipo = tipo_interferencia(fase1, fase2)
    ax.set_title(f"Interferência {tipo}")

    return linha_onda1, linha_onda2, linha_resultante

# Criar animação
anim = FuncAnimation(fig, animar, init_func=iniciar, frames=200, interval=50, blit=True)
plt.show()