import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
freq = np.random.randint(1, 9, size=4)

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
amplitud = np.random.uniform(3, 6, size=4)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]
t = np.arange(0, 1, 1/2000)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# y(t) = A * sin(2 * pi * B * t) donde A es la amplitud y B es la frecuencia
sinusoids = [amplitud[i] * np.sin(2 * np.pi * freq[i] * t) for i in range(4)]

# Sugerencia: para visualizar las ondas sinusoidales, descomenta las siguientes líneas si deseas verlas por separado.
# for i in range(4):
#     plt.plot(t, sinusoids[i])
#     plt.title(f'Onda Sinusoidal {i+1}: Frecuencia {freq[i]}, Amplitud {amplitud[i]}')
#     plt.show()

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales
x = np.sum(sinusoids, axis=0)

# Numpy también permite aplicar operadores tales como la transformada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
X = np.fft.fft(x)

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = np.arange(2000)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
absX = np.abs(X)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
top4_values = np.sort(absX[:10])[-4:]  # Los 4 valores más grandes
top4_indices = np.argsort(absX[:10])[-4:]  # Los índices de esos 4 valores

# Imprimir los resultados
print(f"Las 4 amplitudes máximas entre los primeros 10 elementos son: {top4_values}")
print(f"Los índices de esos 4 elementos son: {top4_indices}")

# Para mostrar la frecuencia y la amplitud en el dominio de Fourier use las siguientes líneas de código
plt.stem(frequence, absX)
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.title('Transformada de Fourier')
plt.show()
