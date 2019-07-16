import numpy as np
N = [10, 100, 1000, 10000, 100000, 1000000]
L = 0.7
llista = []

for i in N:
  dades = L * np.random.rand(i, 2)
  inside_circle = (dades**2).sum(axis=1) <= L ** 2
  pi = 4*(inside_circle.sum()/i)
  llista.append(pi)

print (llista)
