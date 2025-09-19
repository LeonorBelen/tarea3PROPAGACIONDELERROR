import numpy as np
import matplotlib.pyplot as plt

# Generar un rango de valores para x que va de 0 a pi/2
# Usamos 100 puntos para una curva suave
x = np.linspace(0, np.pi/2, 100)

# Calcular los valores correspondientes de y = sen(x)
y = np.sin(x)

# Obtener los puntos específicos para pi/4 y pi/3
x_pi_4 = np.pi / 4
y_pi_4 = np.sin(x_pi_4)

x_pi_3 = np.pi / 3
y_pi_3 = np.sin(x_pi_3)

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Trazar la función seno
plt.plot(x, y, label='y = sen(x)')

# Marcar los puntos específicos en el gráfico
plt.plot(x_pi_4, y_pi_4, 'ro', label=f'($\pi$/4, {y_pi_4:.2f})')
plt.plot(x_pi_3, y_pi_3, 'go', label=f'($\pi$/3, {y_pi_3:.2f})')

# Personalizar el gráfico
plt.title('Gráfico de la función seno en el rango de [0, $\pi$/2]')
plt.xlabel('Ángulo (radianes)')
plt.ylabel('Seno(x)')
plt.legend()
plt.grid(True)
plt.show()