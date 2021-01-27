# FASE DE IMPLANTACIÓN

## Manual técnico:

### Información relativa á instalación:

    **Requisitos hardware recomendados:**

        CPU: Intel Core i7 o AMD Ryzen 7

        RAM: 16 GB

        DISCO: 256 GB SSD

    **Software necesario:**

        Virtual Box u otro similar que permita la importacion de ficheros OVA.

    **Usuarios por defecto (usuario/contraseña):**

        Debian: root/abc123.

        Grafana: admin/abc123.

        PostgreSQL: postgres/abc123.

        Influxdb: admin/abc123.

    **Carga inicial de datos en la base de datos:**

        Los datos del servidor PIG vienen cargados por defecto en el sistema en el dashboard PIG SERVER INFO.

        Los datos de las estaciones de trabajo pueden crearse usando la base de datos de muestra incluida con el servidor y los scripts de recopilación de datos.

        O crear una base de datos propia e importar los datos existentes.

### Tareas que se deberán realizar una vez el sistema esté funcionando:

* Cambio de contraseña de los usuarios.
* Cambio del certificado autofirmado por uno propio.
* Actualizar la configuración de las aplicaciones con los nuevos usuarios.
* Creación de las fuentes de datos necesarias en Grafana.
* Creación de los paneles necesarios en Grafana.

### Información relativa al mantenimiento del sistema:

        Se recomienda mantener actualizado el sistema operativo y las aplicaciones siguiendo las recomendaciones de los desarrolladores.

## Manual de usuario

    El manual está disponible para su descarga aquí:

    [Manual de Usuario](doc/Manual_Usuario.pdf)
