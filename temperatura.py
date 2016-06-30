#file ncdf
from sys import argv, exit
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as mplt

#errore in caso di mancato inserimento del percorso del file da cui prelevare i dati
if len(argv)<=1:
	print("Errore: non hai inserito il percorso del file")
	exit(1)
percorso = argv[1]
fg = Dataset(percorso, "r")
atmc = fg.groups["atmospheric_components"]
t = atmc.variables['T']
temp = np.array(t)
n_al = temp.shape[1]
fg.close()
medie = np.mean(temp, axis=0)
medie -= 272.15
print(medie)
medie_mtx = medie.reshape(61, 1)
mplt.pcolor(medie_mtx)
mplt.ylim(0,61)
mplt.show()