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

import time
import psycopg2
from environs import Env

# Clase que usaremos para guardar los datos en PostgreSQL
class SaveData:
    """Connect to the PostgreSQL DB and insert the data of the workstations.\n
       Conecta a la BD PostgreSQL e inserta los datos de las estaciones de trabajo. """

    def __init__(self):
        global env,hostdb,database,user,password
        env = Env()
        env.read_env()
        hostdb=env('POSTGRES_HOST')
        database=env('POSTGRES_DB')
        user=env('POSTGRES_USER')
        password=env('POSTGRES_PASSWORD')
    
    # Guardamos los datos en la tabla hosts. Se creará una función por cada prodedimiento almacenado creado en PostgreSQL
    def hosts(self, host, ip):
        """Save data to hosts table. """
        self.host = host
        self.ip = ip

        try:    
            #Datos de la conexion almacenados en el fichero .env
            self.connect = psycopg2.connect(host=hostdb,dbname=database,user=user,password=password)
            self.cur = self.connect.cursor()
            #Llamamos al procedimiento almacenado para realizar la inserción.
            self.cur.execute("CALL add_hosts(%s,%s,'');",(self.host,self.ip))
            #Hacemos un commit, de lo contrario no se reflejara en la bd.
            self.connect.commit() 

        #Controlamos las excepciones por si ocurre algun error.
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
        finally:
            #Cuando terminamos cerramos la conexion con la base de datos.
            if(self.connect != None):
                self.cur.close()
                self.connect.close()

    def infocpu(self, host, cpu, so, memory, disk, free_disk, sn, model):
        """Save data to infocpu table. """
        self.host = str(host)
        self.cpu = cpu
        self.so = so
        self.memory = memory
        self.disk = disk
        self.free_disk = free_disk
        self.sn = sn
        self.model = model
        try:    
            #Datos de la conexion almacenados en el fichero .env
            self.connect = psycopg2.connect(host=hostdb,dbname=database,user=user,password=password)
            self.cur = self.connect.cursor()
            #Llamamos al procedimiento almacenado para realizar la inserción.
            #print(self.cur.mogrify("CALL add_infocpu(%s,%s,%s,'%s','%s','%s',%s,%s,'');",(self.host,self.cpu,self.so,self.memory,self.disk,self.free_disk,self.sn,self.model)))
            self.cur.execute("CALL add_infocpu(%s,%s,%s,'%s','%s','%s',%s,%s,'');",(self.host,self.cpu,self.so,self.memory,self.disk,self.free_disk,self.sn,self.model))
            #print(self.cur.query)
            #Hacemos un commit, de lo contrario no se reflejara en la bd.
            self.connect.commit() 

        #Controlamos las excepciones por si ocurre algun error.
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
        finally:
            #Cuando terminamos cerramos la conexion con la base de datos.
            if(self.connect != None):
                self.cur.close()
                self.connect.close()

    def network_info(self, host, mac, ip, model):
        """Save data to network_info table. """
        self.host = host
        self.mac = mac
        self.ip = ip
        self.model = model

        try:    
            #Datos de la conexion almacenados en el fichero .env
            self.connect = psycopg2.connect(host=hostdb,dbname=database,user=user,password=password)
            self.cur = self.connect.cursor()
            #Llamamos al procedimiento almacenado para realizar la inserción.
            self.cur.execute("CALL add_network_info(%s,%s,%s,%s,'');",(self.host,self.mac,self.ip,self.model))
            #Hacemos un commit, de lo contrario no se reflejara en la bd.
            self.connect.commit() 

        #Controlamos las excepciones por si ocurre algun error.
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
        finally:
            #Cuando terminamos cerramos la conexion con la base de datos.
            if(self.connect != None):
                self.cur.close()
                self.connect.close()

    def services(self, host, name, state):
        """Save data to services table. """
        self.host = host
        self.name = name
        self.state = state

        try:    
            #Datos de la conexion almacenados en el fichero .env
            self.connect = psycopg2.connect(host=hostdb,dbname=database,user=user,password=password)
            self.cur = self.connect.cursor()
            #Llamamos al procedimiento almacenado para realizar la inserción.
            self.cur.execute("CALL add_services(%s,%s,%s,'');",(self.host,self.name,self.state))
            #Hacemos un commit, de lo contrario no se reflejara en la bd.
            self.connect.commit() 

        #Controlamos las excepciones por si ocurre algun error.
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
        finally:
            #Cuando terminamos cerramos la conexion con la base de datos.
            if(self.connect != None):
                self.cur.close()
                self.connect.close()


    def software(self, host, name, version, editor):
        """Save data to software table. """
        self.host = host
        self.name = name
        self.version = version
        self.editor = editor

        try:    
            #Datos de la conexion almacenados en el fichero .env
            self.connect = psycopg2.connect(host=hostdb,dbname=database,user=user,password=password)
            self.cur = self.connect.cursor()
            #Llamamos al procedimiento almacenado para realizar la inserción.
            self.cur.execute("CALL add_software(%s,%s,%s,%s,'');",(self.host,self.name,self.version,self.editor))
            #Hacemos un commit, de lo contrario no se reflejara en la bd.
            self.connect.commit() 

        #Controlamos las excepciones por si ocurre algun error.
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
        finally:
            #Cuando terminamos cerramos la conexion con la base de datos.
            if(self.connect != None):
                self.cur.close()
                self.connect.close()

if __name__ == '__main__':
   #d = SaveData().hosts('pc20','192.168.4.10')
   d = SaveData().services('pc12','wmi','Running')
   
