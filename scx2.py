#!/usr/bin/env python

#YYYY MM DD HHMMSS tt CM Estacion 00 HH*
"""
Script que permite realizar extracciones del servido de seiscomp mediante el servicio web fdsn
v(1) Nelson David Perez e-mail: nperez@sgc.gov.co
"""
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import numpy as np
import sys

from colorama import *
init(autoreset=True)


#Se define url del servidor, puerto y formato

ip_fdsn = "http://10.100.100.232"
port_fdsn = "8091"
Format = "mseed"

#funcion que crea un nombre a partir de parametros de entrada
def archive_name(lista):
	name = ""
	for l in lista:
		if ('*' in l )== False:
			name += "_"+l
		elif ('*' in l)== True:
			name += "_"+l.strip('*')
		else:
			name += "_"
	return name
#Se revisan los parametros de entrada

if len(sys.argv) < 2:
	print (Fore.RED + "				No hay parametros de entrada, debe ser"+ Fore.CYAN + " YYYY MM DD HHMMSS tt CM Estacion 00 HH* "+ Fore.GREEN+ " (minimo hasta tt)")
	sys.exit()
if len(sys.argv) > 10:
	print (Fore.RED + "				Demasiados argumentos, debe ser"+ Fore.CYAN +" YYYY MM DD HHMMSS tt CM Estacion 00 HH*"+ Fore.GREEN+ "  (minimo hasta tt)")
	sys.exit()
year, MM, dd, hh, mm, ss = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4][0:2], sys.argv[4][2:4], sys.argv[4][4:6]

#Se define el tiempo y el nombre de la traza

t = UTCDateTime(int(year), int(MM), int(dd), int(hh), int(mm), int(ss))
t_ = float(sys.argv[5])
#name = year+"-"+MM+"-"+dd+"-"+hh+mm+ss+archive_name(sys.argv[5:])+"."+Format

print (t, t_)

#Se inicia el cliente FDSN para la solicitud
client = Client(ip_fdsn+":"+port_fdsn)
print (client)


#Se realizan solicitudes de formas de onda
if len(sys.argv) == 6:
	st = client.get_waveforms("*", "*", "*", "*", t, t+t_)
	#for tr in st:
    	#	if isinstance(tr.data, np.ma.masked_array):
        #		tr.data = np.array.filled(tr)
	#st.merge()
	#st.merge(method=0, fill_value='interpolate', interpolation_samples=0)
	name = year+"-"+MM+"-"+dd+"-"+hh+mm+"-"+ss+"M.COL___"+str(len(st))
	print (st)

if len(sys.argv) == 7:
	st = client.get_waveforms(sys.argv[6], "*", "*", "*", t, t+t_)
	#st.merge()
	#st.merge(method=0, fill_value='interpolate', interpolation_samples=0)
	name = year+"-"+MM+"-"+dd+"-"+hh+mm+"-"+ss+"M.COL___"+str(len(st))
	print (st)

if len(sys.argv) == 8:
	st = client.get_waveforms(sys.argv[6], sys.argv[7], "*", "*", t, t+t_)
	#st.merge()
	#st.merge(method=0, fill_value='interpolate', interpolation_samples=0)
	name = year+"-"+MM+"-"+dd+"-"+hh+mm+"-"+ss+"M.COL___"+str(len(st))
	print (st)

if len(sys.argv) == 9:
	st = client.get_waveforms(sys.argv[6], sys.argv[7], sys.argv[8], "*", t, t+t_)
	#st.merge()
	#st.merge(method=0, fill_value='interpolate', interpolation_samples=0)
	name = year+"-"+MM+"-"+dd+"-"+hh+mm+"-"+ss+"M.COL___"+str(len(st))
	print (st)

if len(sys.argv) == 10:
	st = client.get_waveforms(sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], t, t+t_)
	#st.merge()
	#st.merge(method=0, fill_value='interpolate', interpolation_samples=0)
	name = year+"-"+MM+"-"+dd+"-"+hh+mm+"-"+ss+"M.COL___"+str(len(st))
	print (st)

#Se escribe la forma de onda con el directorio local
st.write(name, Format)
	
