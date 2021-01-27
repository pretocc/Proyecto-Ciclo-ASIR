"""
******************************************************************************
 * PIG
 * Santiago Prego López 2020
 * 
 * This file is part of PIG.
 * 
 * PIG is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * PIG is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License.
 * If not, see <http://www.gnu.org/licenses/>.
******************************************************************************
"""

import data_module as dataw
import dbpg_module as dbpg
import socket

# Comprobamos si el host admite la conexion al puerto 135 (RPC) usando sockets.
def scan(host):
   estado = 1
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(0.50)
   try:
       estado = s.connect_ex((host,135)) # Aqui es donde indicamos el puerto.
   except:
       pass
   s.close()
   if estado == 0:
      IP = socket.gethostbyname(host)
      print(host)
      dbpg.SaveData().hosts(host,IP) #Almacenamos los datos de la estacion de trabajo en la tabla hosts
      d = dataw.Info(host) # Ejecutamos el modulo de recopilación de datos.
      d.start()
      d.join()

      return 1
   else : # Guardamos en un fichero los ordenadores que no estaban disponibles.
      with open("pendientes.txt", "a") as p:
        p.write(host+"\n")
      print(host," no encontrado")
      return 0

try:
    with open("PCS.txt", "r", encoding='utf-8') as PCS: # Abrimos el fichero donde almacenamos los equipos a escanear.
        hosts = PCS.readlines()
    i = 0 
    for host in hosts:
        i=i+1
        host=host.split("\n")
        scan(host[0]) # Escaneamos cada host para ver si nos podemos conectar.

except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
    pass
except:
    pass
 