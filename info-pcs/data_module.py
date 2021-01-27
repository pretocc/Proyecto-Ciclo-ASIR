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

import dbpg_module as dbpg
import pythoncom
import wmi
import threading # Vamos a usar hilos para la ejecucion del script
import time


# Obtenemos los datos de la tarjeta de red activa de la estación de trabajo.
def network(computer):
        pythoncom.CoInitialize()

        try:
            #En exta conexión se especifica un usuario concreto con el que conectarse a los equipos remotos, este debe de tener permisos para realizar consultas wmi.
            #c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy', user="sprego", password="abc123.") 
            c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy') # Con esta conexión el usuario que ejecuta el script debe de terner permisos para consultas wmi a los equipos destino.
            for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1): # IPEnabled=1 indica la tarjeta activa
                model = interface.description
                mac = interface.MACAddress
                ip = interface.IPAddress[0]
                dbpg.SaveData().network_info(computer,mac,ip,model)

        except wmi.x_wmi as e:
            print(e.com_error.strerror,e.com_error.excepinfo[2])
            return e.com_error.strerror,e.com_error.excepinfo[2]

        finally:
            pythoncom.CoUninitialize()

# Obtenemos los datos de los servicios que se están ejecutando en la estación de trabajo.
def services(computer):
        pythoncom.CoInitialize()
        try:
            #c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy', user="sprego", password="abc123.")
            c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy')
            for s in c.Win32_Service(): # Servicios del sistema operativo y su estado.
                name = s.Name
                state = s.State
                #print(computer,name,state)
                dbpg.SaveData().services(computer,name,state)

        except wmi.x_wmi as e:
            print(e.com_error.strerror,e.com_error.excepinfo[2])
            return e.com_error.strerror,e.com_error.excepinfo[2]

        finally:
            pythoncom.CoUninitialize()

# Obtenemos los datos del software instalado en la estación de trabajo
def software(computer):
        pythoncom.CoInitialize()
        try:
            #c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy', user="sprego", password="abc123.")
            c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy')
            for s in c.Win32_Product(): # Nombre, vendedor y version del software instalado.
                dbpg.SaveData().software(computer,s.Name,s.Version,s.Vendor)
                print(computer,s.Name,s.Version,s.Vendor)

        except wmi.x_wmi as e:
            #print(e.com_error.strerror,e.com_error.excepinfo[2])
            return e.com_error.strerror,e.com_error.excepinfo[2]

        finally:
            pythoncom.CoUninitialize()

# Obtenemos los datos hardware de la estación de trabajo
def infocpu(computer):
        pythoncom.CoInitialize()
        try:
            #c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy', user="sprego", password="abc123.")
            c = wmi.WMI(computer=computer, impersonation_level='impersonate', authentication_level='pktPrivacy')
            for d in c.Win32_LogicalDisk(DriveType=3):
                if d.Caption == "C:" : # Nos quedamos solo con los datos de la unidad C:
                    disk = round((int(d.Size)/1024**3)) # Pasamos a GB y redondeamos el espacio en disco total
                    free_disk = round(int(d.FreeSpace)/1024**3) # Pasamos a GB y redondeamos el espacio en disco libre
            for d in c.Win32_ComputerSystemProduct():
                model = d.Name # Modelo del ordenador
                sn = d.IdentifyingNumber # Numero de serie del ordenador (si lo tiene)
            for d in c.Win32_OperatingSystem():
                so = d.Caption # Sistema operativo instalado
                memory = round(int(d.TotalVisibleMemorySize)/1024**2) # Memoria total visible por el sistema operativo.
            for d in c.Win32_Processor():
                cpu = d.Name # Modelo del procesador
            #print(cpu,so,memory,disk,free_disk,sn,model)
            dbpg.SaveData().infocpu(computer, cpu, so, memory, disk, free_disk, sn, model)

        except wmi.x_wmi as e:
            print(e.com_error.strerror,e.com_error.excepinfo[2])
            return e.com_error.strerror,e.com_error.excepinfo[2]

        finally:
            pythoncom.CoUninitialize()

# Clase principal con la que recopilaremos los datos de las estaciones de trabajo separadas en funciones independientes.
# Lo separamos en funciones para que sea mas modular pudiendo escoger que datos guardar.
class Info(threading.Thread):
    """ Obtain info about the workstation."""

    def __init__(self, computer):
        self.computer = computer
        super(Info, self).__init__()

    # Ejecutamos las funciones de las que queramos obtener lo datos
    def run(self):
        network(self.computer)
        services(self.computer)
        software(self.computer)
        infocpu(self.computer)

if __name__ == '__main__':
    t = Info('DESKTOP-0DMC064')
    t.start()
    t.join()


