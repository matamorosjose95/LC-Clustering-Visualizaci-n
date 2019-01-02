# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:13:13 2018
@author: José
"""
#%% Imports
import os
import pickle

ruta_base='C:\\Users\Dell\Desktop\IC\BaseDatos' # cambiar cuando corresponda

# Crear lista subfolders con las rutas de todas las carpetas dentro de la 
# carpeta de base de datos
folders = [f.path for f in os.scandir(ruta_base)] # lista de carpetas CEPH, EB, RRL
subfolders = [] # aquí se guardan todas las rutas
for i in range(len(folders)):
    subfolders=subfolders+[f.path for f in os.scandir(folders[i])]

#%% Funciones importantes
    
# ls_dat toma una carpeta y retorna una lista con todos los archivos con
# extensión .dat
def ls_dat(ruta):
    return [arch.path for arch in os.scandir(ruta) if arch.name.endswith('.dat')]

# ls_time toma una carpeta y retorna una listaa con todos los archivos con
# extensión .time
def ls_time(ruta):
    return [arch.path for arch in os.scandir(ruta) if arch.name.endswith('.time')]

# recibe un str con la ruta y nombre del archivo .dat y extrae el periodo 
def get_periodo(filename): 
    dat_file=open(filename,'r')
    periodo=dat_file.readlines()[1][:-1] #lee la primera línea, debe decir #Period\n
    dat_file.close()
    return float(periodo)

def datos_1(ruta_time):
    archivo = open(ruta_time,'r')
    archivo.readline()
    linea = archivo.readline().split(' ')
    # eliminar todos los elementos vacíos
    while linea.count('')!=0:
        for i in linea:
            if i=='#' or i=='':
                linea.remove(i)
    #eliminar el \n del ultimo man
    linea[-1]=linea[-1][:-1]
    archivo.close()
    return linea

def datos_2(ruta_time):    
    #extraer las series de tiempo 
    date = []
    MagR = []
    ErMagR = []
    MagB = []
    ErMagB = []

    archivo = open(ruta_time,'r')
    archivo.readline()
    archivo.readline()
    archivo.readline() # linea vacía
    archivo.readline() # linea que describe los valores siguientes

    linea2 =  archivo.readline()
    while linea2!='':
        linea2 =  linea2.split(' ')
        while linea2.count('')!=0:
            for i in linea2:
                if i=='#' or i=='':
                    linea2.remove(i)
        linea2[-1]=linea2[-1][:-1]
        date.append(float(linea2[0]))
        MagR.append(float(linea2[1]))
        ErMagR.append(float(linea2[2]))
        MagB.append(float(linea2[3]))
        ErMagB.append(float(linea2[4]))
        linea2 = archivo.readline()

    return [date, MagR, ErMagR, MagB, ErMagB]

#%% Extracción de datos

# Listas de rutas con archivos .dat y .time para luego poder abrirlos y leerlos
rutas_dat = []
rutas_time = []
for i in range(len(subfolders)):
    rutas_dat = rutas_dat + ls_dat(subfolders[i])
    rutas_time = rutas_time + ls_time(subfolders[i])
      
Periodo = [] #guarda los periodos de todas las estrellas segun
for ruta in rutas_dat:
    Periodo.append(get_periodo(ruta))

Nombres = []
MR = [] # lista con los MagR de la linea 2 del archivo .time
ErrMR = [] # lista con los ErrMR de la linea 2 del archivo .time
XR = [] # lista con los XR de la linea 2 del archivo .time
YR = [] # lista con los YR de la linea 2 del archivo .time

MB = [] # lista con los MagB de la linea 2 del archivo .time
ErrMB = [] # lista con los ErrMB de la linea 2 del archivo .time
XB = [] # lista con los XB de la linea 2 del archivo .time
YB = [] # lista con los YB de la linea 2 del archivo .time

for i in rutas_time:
    datos = datos_1(i)
    Nombres.append(datos[0])
    MR.append(float(datos[1]))
    ErrMR.append(float(datos[2]))
    XR.append(float(datos[3]))
    YR.append(float(datos[4]))
    MB.append(float(datos[5]))
    ErrMB.append(float(datos[6]))
    XB.append(float(datos[7]))
    YB.append(float(datos[8]))
   
dateR = []
dateB = []    
MagR = []
ErMagR = []
MagB = []
ErMagB = []

for i in rutas_time:
    datos = datos_2(i)
    dateR.append(datos[0])
    dateB.append(datos[0])
    MagR.append(datos[1])
    ErMagR.append(datos[2])
    MagB.append(datos[3])
    ErMagB.append(datos[4])
    
#%% Guardar todo con pickle

file_Nombres=open('file_Nombres.obj','wb')
pickle.dump(Nombres,file_Nombres)

file_Periodo=open('file_Periodo.obj','wb')
pickle.dump(Periodo,file_Periodo)

file_dateB=open('file_dateB.obj','wb')
pickle.dump(dateB,file_dateB)

file_dateR=open('file_dateR.obj','wb')
pickle.dump(dateR,file_dateR)

file_MagB=open('file_MagB.obj','wb')
pickle.dump(MagB,file_MagB)

file_MagR=open('file_MagR.obj','wb')
pickle.dump(MagR,file_MagR)

file_ErMagB=open('file_ErMagB.obj','wb')
pickle.dump(ErMagB,file_ErMagB)

file_ErMagR=open('file_ErMagR.obj','wb')
pickle.dump(ErMagR,file_ErMagR)

file_ErrMB=open('file_ErrMB.obj','wb')
pickle.dump(ErrMB,file_ErrMB)

file_ErrMR=open('file_ErrMR.obj','wb')
pickle.dump(ErrMR,file_ErrMR)

#%%
file_MR=open('file_MR.obj','wb')
pickle.dump(MR,file_MR)

file_MB=open('file_MB.obj','wb')
pickle.dump(MB,file_MB)

file_ErrMR=open('file_ErrMR.obj','wb')
pickle.dump(ErrMR,file_ErrMR)

file_ErrMB=open('file_ErrMB.obj','wb')
pickle.dump(ErrMB,file_ErrMB)

file_XR=open('file_XR.obj','wb')
pickle.dump(XR,file_XR)

file_YR=open('file_YR.obj','wb')
pickle.dump(YR,file_YR)

file_XB=open('file_XB.obj','wb')
pickle.dump(XB,file_XB)

file_YB=open('file_YB.obj','wb')
pickle.dump(YB,file_YB)