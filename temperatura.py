#file ncdf
from sys import argv, exit
import numpy as np
from netCDF4 import Dataset

#errore in caso di mancato inserimento del percorso del file da cui prelevare i dati
if len(argv)<=1:
	print("Errore: non hai inserito il percorso del file")
	exit(1)
percorso = argv[1]
fg = Dataset(percorso, "r")
atmc = fg.groups["atmospheric_components"]
t = atmc.variables['T']
temp = np.array(t)
medie = []
n_fov = temp.shape[0]
somma= 0
n_al = temp.shape[1]
for i in range(n_fov):
	somma += temp[i, :]
medie=somma/n_fov
print(medie)
fg.close()