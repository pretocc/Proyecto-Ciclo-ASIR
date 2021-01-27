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

red_ini = [192,168,1,86] # Primera IP donde comenzará el escaneo
red_fin = [192,168,1,142] # Ultima IP que escaneará


# Comprobamos si el host admite la conexion al puerto 135 (RPC) usando sockets.
def scan(IP):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(0.50)
   estado = s.connect_ex((IP,135)) # Aqui es donde indicamos el puerto.
   s.close()
   if estado == 0:
      host = socket.gethostbyaddr(IP)[0] #Obtenemos el nombre de la estación de trabajo
      host = host.split(".")[0]
      dbpg.SaveData().hosts(host,IP) #Almacenamos los datos de la estacion de trabajo en la tabla hosts
      print(host)
      print(IP)
      d = dataw.Info(host) # Ejecutamos el modulo de recopilación de datos.
      d.start()
      d.join()

      return 1
   else :
      return 0


# Bucle que recorre todas las IPs del segmento de red configurado.
while True :
    IP = str(red_ini[0])+"."+str(red_ini[1])+"."+str(red_ini[2])+"."+str(red_ini[3]) # Almacenamos en un string la IP por la que vamos.
    if red_ini[3] == 254 : # Si el octeto alcanza el máximo salta al siguiente y asi sucesivamente.
        red_ini[3] = 0
        red_ini[2] += 1
        if red_ini[2] == 254 :
            red_ini[2] = 0
            red_ini[1] += 1
            if red_ini[1] == 254 :
                red_ini[1] = 0
                red_ini[0] += 1
                if red_ini[0] == 254 :
                    red_ini[1] = 0

    if IP == "254.254.254.254": # Si se ha recorrido todas las IPS posibles se para.
        break
    scan(IP)
    if red_ini == red_fin : # Si alcanzamos la ultima IP del rango paramos.
        break
    red_ini[3] += 1
