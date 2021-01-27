# ESTUDIO DE NECESIDADES Y MODELO DE NEGOCIO

## Publico objetivo

Este proyecto está destinado a un departamento de soporte o sistemas de una empresa con un parque de ordenadores de tamaño medio o grande. Está basado en las necesidades que hemos encontrado trabajando en una empresa con un parque de más de mil equipos, centrándome principalmente en la gestión de los equipos cliente.

## Necesidades detectadas

Cuando el parque de ordenadores es muy grande la gestión y control del mismo se vuelve cada vez más compleja sin un sistema que te ayude a llevar el control. Actualmente se dispone de un gestor de activos pero tiene carencias que se pretenden cubrir con este proyecto.

El software actual es privativo, carece de la posibilidad de crear paneles de visualización con los datos existentes, y no se le pueden añadir módulos personalizados según surjan necesidades.

Sería útil llevar un registro de las intervenciones realizadas en cada equipo.

## Requisitos que se pretenden cubrir

Se busca crear un proyecto que muestre la información de una forma visual, que sea modular, fácilmente escalable y que necesite poco mantenimiento.

##### Visual

Necesitamos ver por ejemplo el porcentaje de cada sistema operativo instalado, esto será útil sobre todo en momentos en los que se migre de una versión a otra, por ejemplo de Windows 7 a Windows 10. Otro ejemplo sería para llevar un seguimiento de una línea base de software, versiones de software instalada, evolución de la implantación de una nueva aplicación, control de licencias, etc.

Aquí podemos ver un ejemplo de visualización de datos que permite hacerse una idea de lo que se pretende conseguir.

![](../img/Grafana-Ejemplo.PNG)

##### Modular

Se le deben de poder ir agregando módulos según vayan surgiendo necesidades nuevas interrumpiendo el servicio lo menos posible.

##### Escalable

Debe de ser posible aumentar fácilmente tanto el número de dispositivos controlados como el tipo de dispositivos y número de parámetros a monitorizar.

##### Mantenimiento

El mantenimiento debe de ser sencillo y no consumir mucho tiempo ni tampoco recursos económicos, una vez un módulo nuevo se desarrolle este debería de cumplir los mismos requisitos.

## Cómo se van a cumplir esos requisitos.

##### Visual

Para ello se utilizará Grafana el cual permite una amplia variedad de gráficos y análisis que permitirán de un vistazo poder valorar el estado del parque informático.

##### Modular

Se va a utilizar software externo y software propio intentando que cada módulo sea independiente y afecte a los demás lo menos posible, permitiendo realizar intervenciones sobre partes concretas sin necesidad de parar todo el sistema.

Los gráficos de Grafana se alimentan de fuentes externas, permitiendo agregar nuevas funcionalidades simplemente ampliando las fuentes de datos existentes o creando nuevas fuentes.

##### Escalable

Al alimentarse de fuentes externas se pueden desarrollar nuevas funcionalidades adaptadas a nuevos dispositivos que vayan apareciendo. En cuanto a recursos hardware al tratarse de una máquina virtual se le pueden aumentar según vaya creciendo antes de que el rendimiento se vea penalizado.

##### Mantenimiento

Usaremos software externo y desarrollo propio para buscar un equilibrio entre costes de desarrollo y flexibilidad para llegar al detalle que necesitemos.

El mantenimiento del software externo consistirá en mantener actualizado a las últimas versiones estables los productos y adaptar las configuraciones a los posibles cambios que se den en la arquitectura, pudiendo desentendernos del desarrollo.

El mantenimiento del software propio consistirá en la creación de nuevos módulos y la corrección de fallos de seguridad que se detecten en los mismos o cambios en la arquitectura.

## Actividades a llevar a cabo

A continuación se detallan las actividades necesarias para llevar a cabo el proyecto.

- Instalación de un Debian 10 en una máquina virtual.

- Instalación y configuración de Grafana

- Instalación y configuración de InfluxDB

- Instalación y configuración de Telegraf

- Instalación y configuración de PostgreSQL

- Diseño y creación de una base de datos en PostgreSQL

- Creación de un certificado autofirmado para habilitar el acceso a las aplicaciones web a través de https.

- Exportación de la máquina virtual a un fichero .OVA basado en el estándar OVF.

- Creación de un manual de usuario y un manual de administración.

Actividades extra si se dispone de tiempo suficiente.

- Creación de un software para la búsqueda automática de equipos en la red y recopilación de datos de los mismos.

- Diseño de la aplicación CRUD para los datos de las estaciones de trabajo desde la cual se podrá introducir datos sobre las tareas realizadas en los equipos, dejando abierta la posibilidad de integrarla en el futuro con una herramienta de *ticketing*.

## Metodología a seguir

    Dado que la mayoría de metodologías de desarrollo están orientadas a casos en los que existe mas de un programador (SCRUM, Agile, Kanban, etc) no me ceñiré a ninguna específica, en mi caso usaré una metodología propia en la que dividiré el proyecto en varias fases dentro de las cuales habrá una lista de tareas que se irán haciendo de forma secuencial. No debo preocuparme por el cliente ya que en este caso yo mismo seré el cliente, yo usaré el desarrollo final. 

## Viabilidad

   **Viabilidad técnica**

            Será necesaria una persona para el desarrollo e implantación del proyecto.

            Requisitos hardware recomendados:

                   CPU: Intel Core i7 o AMD Ryzen 7

                   RAM: 16 GB

                   DISCO: 256 GB SSD

   **Viabilidad económica**

                Todo el software que se empleará, tanto para el diseño y desarrollo como para la implantación es software libre, por lo que los costos de licenciamiento serán inexistentes.

                No será necesaria la compra hardware para llevarlo a cabo, ya que se usará el existente.

                Se usará la conexión a Internet existente y lo único que generaría un gasto adicional será el consumo eléctrico extra.

## Comercialización

No está planeada su comercialización, será ofrecido de forma gratuita bajo licencia de software libre.

En caso de que el proyecto llegase a alcanzar una gran popularidad se podría llegar a ofrecer servicios de asesoramiento, formación e implantación. Pero esos ingresos serían invertidos de nuevo en la mejora y creación de nuevas funcionalidades para el proyecto.

## Tiempo necesario para el proyecto

El proyecto fin de ciclo consta de 150 horas lo que permitirá entregar la fase 1 completa y una parte o la totalidad de la fase 2. La fase tres no se podrá entregar dentro de ese plazo.

Para la realización de las tres fases del proyecto se necesitarán 300 horas, este es un tiempo estimado que actualizaré al final del proyecto.
