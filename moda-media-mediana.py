import statistics as st

comprimento = [3, 5, 6, 8, 7, 3]

# Média aritmética
mediaSomada = sum(comprimento) / len(comprimento)
print("Média:", mediaSomada)

mediaStatistics = st.mean(comprimento)
print("Média:", mediaStatistics)

# Mediana
minimo = min(comprimento)
maximo = max(comprimento)
mediana = st.median(comprimento)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Mediana:", mediana)

# Moda
moda = st.mode(comprimento)
print("Moda:", moda)
