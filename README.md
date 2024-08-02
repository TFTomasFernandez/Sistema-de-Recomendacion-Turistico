# Proyecto Final SoyHenry
<p style="text-align: center;">
   <img src="img/data-forge-logo.jpg" alt="Data Forge - Forging the Future">
</p>
<p style="text-align: center;">
   <em>Data Forge - Forging the Future</em>
</p>

## Introducción
>*DataForge está conformado por un conjunto de profesionales que busca entender los patrones del pasado para comprender mejor las tendencias actuales y ayudar de la mejor manera a construir el futuro. El volcán, la representación de nuestra pasión en su estado puro, utilizando nuestras habilidades y conocimientos para dar forma a ese deseo.*

Este proyecto está orientado a acompañar una pasión que muchos de nosotros compartimos y uno de los hobbies favoritos de la humanidad: **Viajar**

## Índice
1. [Introducción](#introducción)
2. [Productos a Desarrollar](#productos-a-desarrollar)
   - [Modelo de Recomendación: Turismo Emergente](#modelo-de-recomendación-turismo-emergente)
   - [Base de Datos: Turismo de Interés](#base-de-datos-turismo-de-interés)
   - [Dashboard: Indicadores Turísticos](#dashboard-indicadores-turisticos)
3. [Alcance del Proyecto](#alcance-del-proyecto)
4. [Tecnologías](#tecnologias)
5. [Integrantes](#integrantes)

## Productos a Desarrollar
Este proyecto tiene como intención desarrollar tres productos:

1. Un [Modelo de Recomendación](#modelo-de-recomendacion:-turismo-emergente) que busca identificar lugares con potencial poco explotado de turismo en determinados estados en relación a la región geográfica.

2. Una [Base de Datos](#base-de-datos:-turismo-de-interes) que es una base de datos creada a partir de las búsquedas llevadas a cabo en el sistema de recomendación con la intención de informar a posibles inversores de puntos de interés y/o tendencias de búsqueda.

3. Un [Dashboard](#dashboard-indicadores-turisticos) con los indicadores principales a tratar e información relevante para el objetivo a alcanzar.

A continuación observaremos en más detalle cada uno de estos productos:

### Modelo de Recomendación: Turismo Emergente
El proyecto utiliza las bases de datos de [Yelp](https://www.yelp.com/) y [Google Maps](https://www.google.com/maps) otorgadas por el PO para formar un Sistema de Recomendación haciendo una Vectorización de Reseñas para extraer palabras clave de un grupo específico de estados de EE. UU. donde el turismo está disminuido o tiene propuestas de interés emergentes para sus posibles visitantes.

Utilizamos, además, un conjunto de fuentes adicionales como el [Sitio de Viajes Oficial de EE. UU.](https://www.visittheusa.com/) o el [Sitio oficial de Administración de Viaje Internacional](https://www.trade.gov/) para hacer la selección de estados con potencial de crecimiento. [Más adelante](#foco-del-proyecto) haremos un análisis más profundo de los estados elegidos, acompañado del razonamiento utilizado.

El sistema de recomendación será consumido por el usuario en formato de página web, donde podremos encontrar menús que permiten personalizar la búsqueda como, por ejemplo, actividades, comida, temperatura, etc. Al ejecutarse, el sistema recomendará una lista de lugares con el mayor número de coincidencias, ordenada por el promedio de estrellas otorgadas en las reseñas, y una serie de enlaces:
- Algunos de los negocios mejor valorados de la zona.
- La búsqueda del área seleccionada en [Booking](https://booking.com/).
- La búsqueda del área seleccionada en [Airbnb](https://www.airbnb.com).

### Base de Datos: Turismo de Interés
Una vez establecido el Sistema de Recomendación se creará una base de datos donde se almacenarán de manera sistemática las búsquedas realizadas por los usuarios en la web, dando insights sobre potenciales puntos de inversión y las tendencias de interés de los usuarios con la intención de informar las decisiones tomadas por potenciales inversores.

La forma de consumo de dicha base de datos también será en formato web. Se le otorgará un usuario y contraseña al personal autorizado a acceder y, una vez ingresado, tendrán la posibilidad de observar y descargar los datos en crudo, almacenados en un servidor para su posterior procesamiento.

### Dashboard: Indicadores Turísticos

Es importante que haya una correcta visualización de los datos para poder aprovechar los posibles puntos de inversión y desarrollo, estar al día con las últimas tendencias y, en definitiva, tener siempre en vista el objetivo.

Para eso proponemos la creación de un Dashboard de los contenidos de la nueva base de datos procesada, con una clara visualización del progreso de los indicadores y otra información relevante al objetivo.

## Alcance del Proyecto
Tras un análisis completo de los datos disponibles sumado a algunos datos externos que consideramos relevantes para el proyecto, nos definimos por dos estados iniciales. Cabe recalcar que si el proyecto resulta fructífero sería interesante aumentar este número. Los estados elegidos, acompañados con el razonamiento utilizado, son:

### Indiana

<p style="text-align: center;">
   <img src="img/indiana_maploc.png" alt="Indiana en el mapa">
</p>

Indiana es un estado que puede no llamar la atención en un principio; sin embargo, **no se dejen engañar**: capitales ajetreadas, viñedos pacíficos, dunas ardientes, aguas frescas, colinas altas, cavernas profundas y bellísimos bosques. Todo eso envuelto en un paquete de **hospitalidad** y productos locales, criados y cultivados en esta misma tierra. Indiana promete una estadía **pacífica y variada**.

<p style="text-align: center;">
   <img src="img/indiana_sight.png" alt="Paisajes de Indiana">
</p>
<p style="text-align: center;">
   <em>Paisajes de Indiana</em>
</p>

Es por eso que nos *llamó la atención* que se encontrara en el **Ranking 26** de estados más visitados de EE. UU., con **poco más de 200 mil visitas** en 2023 (en comparación con su vecino inmediato, Illinois, **Ranking 7** con **casi 1 millón** y medio de visitas). *Y está claro que no somos los únicos que lo notaron!* El crecimiento en 2023 respecto al año anterior fue de un **25%** (unos 43 mil visitantes más), demostrando que su belleza no solo tiene *potencial*, sino *interés*.

<p style="text-align: center;">
   <img src="img/indiana_rank.png" alt="Ranking Indiana">
</p>
<p style="text-align: center;">
   <em> Datos obtenidos de la
      <a href="https://www.trade.gov/us-states-cities-visited-overseas-travelers">Página Oficial de la Administración de Comercio Internacional</a>
   </em>
</p>

### Luisiana

<p style="text-align: center;">
   <img src="img/luisiana_maploc.png" alt="Luisiana en el mapa">
</p>

Luisiana se encuentra en una posición *sumamente interesante*, ubicada entre dos potencias turísticas: **Florida** a la derecha y **Texas** a la izquierda. Sus características topográficas son similares a las de Florida, incluyendo playas caribeñas, bellos bosques tropicales y asombrosos pantanos. Sus ciudades son pintorescas, con una hermosa arquitectura inspirada en su mezcla de culturas francesa, africana y americana. Algunas de sus ciudades llevan un espíritu festivo tanto de día, con sus carnavales, desfiles y ferias, como de noche, con sus fiestas callejeras y clubes nocturnos.

<p style="text-align: center;">
   <img src="img/luisiana_sight.png" alt="Paisajes de Luisiana">
</p>
<p style="text-align: center;">
   <em>Paisajes de Luisiana</em>
</p>

Sin embargo, a pesar de todo esto, la cantidad de visitantes internacionales lo pone en el **Ranking 23** de EE. UU., con apenas unos **318.000 visitantes internacionales** (en comparación con casi **2 millones de Texas**, en el puesto 5, y casi **8 millones de Florida** en el puesto 2). Luisiana cuenta además con un crecimiento positivo, indicando cierto interés, pero el volumen de viajeros aumentó tan solo en 4.000 personas (1,3%) en el año 2023 respecto al 2022.

<p style="text-align: center;">
   <img src="img/luisiana_rank.png" alt="Ranking Luisiana">
</p>
<p style="text-align: center;">
   <em> Datos obtenidos de la
      <a href="https://www.trade.gov/us-states-cities-visited-overseas-travelers">Página Oficial de la Administración de Comercio Internacional</a>
   </em>
</p>

## Tecnologías

El proyecto requiere de múltiples sistemas funcionando en conjunto para garantizar un trabajo ordenado y eficiente, y un producto funcional.

- **Google Cloud Platform (GCP)**: Es el centro de nuestro ecosistema de almacenamiento y base de datos relacional. Su infraestructura global y segura proporciona escalabilidad, fiabilidad y rendimiento, además de integraciones con otras herramientas y servicios populares.

- **Python**: Es el principal motor de procesamiento de datos que utilizaremos. Su versatilidad y su sintaxis clara y legible nos permite un manejo de la información eficiente y un trabajo colaborativo eficaz. Será usado en la ingesta y procesamiento de los datos y en el entrenamiento del modelo de recomendación, aprovechando muchas de sus librerías.

- **GitHub**: La principal plataforma de alojamiento y comunicación de código que utilizaremos, ideal para tener un buen control de versiones y del código fuente a lo ancho del grupo y lo largo del proyecto. Facilitará mucho el trabajo colaborativo entre los desarrolladores, el seguimiento de problemas y la accesibilidad.

- **Structured Query Language (SQL)**: Es el lenguaje estándar para la gestión y manipulación de la base de datos relacional. Será utilizado para realizar consultas, actualizar y gestionar los datos almacenados. Su capacidad para manejar grandes volúmenes de datos y realizar operaciones complejas de manera eficiente lo convierte en una herramienta fundamental para el proyecto.

- **Google Slides**: Parte de la suite de productividad de Google Workspace, Google Slides permite la creación, edición y colaboración en presentaciones de manera sencilla y accesible desde cualquier dispositivo con acceso a internet. En este proyecto, Google Slides se utiliza constantemente para presentar de manera visual proyectos e ideas. Su capacidad para colaborar en tiempo real facilita la organización y el acceso a la información presentada.

<p style="text-align: center;">
   <img src="img/tecnologies_banner.png" alt="Tecnologías utilizadas">
</p>

## Integrantes
<table style="width: 100%; text-align: center; border-collapse: collapse; border-bottom: 1px solid #ccc;">
  <tr>
    <td style="border-right: 1px solid #ccc; border-left: 1px solid #ccc; border-top: 1px solid #ccc; border-bottom: none; padding: 10px;">
      <strong>Tomas Fernandez</strong><br>(Data Scientist)
    </td>
    <td style="border-right: 1px solid #ccc; border-top: 1px solid #ccc; border-bottom: none; padding: 10px;">
      <strong>Nahuel Salamone</strong><br>(Data Engineer)
    </td>
    <td style="border-right: 1px solid #ccc; border-top: 1px solid #ccc; border-bottom: none; padding: 10px;">
      <strong>Martin Ferrari</strong><br>(Data Analyst)
    </td>
    <td style="border-right: 1px solid #ccc; border-top: 1px solid #ccc; border-bottom: none; padding: 10px;">
      <strong>Pablo Chamena</strong><br>(Data Scientist)
    </td>
    <td style="border-top: 1px solid #ccc; border-right: 1px solid #ccc; border-bottom: none; padding: 10px;">
      <strong>Giada de Carlo</strong><br>(Data Analyst)
    </td>
  </tr>
  <tr>
    <td style="border-right: 1px solid #ccc; border-left: 1px solid #ccc; border-top: none; padding: 10px;">
      <img src="img/Integrantes/Tomas_Fernandez_Token.png" alt="Tomas Fernandez" width="100" height="100">
    </td>
    <td style="border-right: 1px solid #ccc; border-top: none; padding: 10px;">
      <img src="img/Integrantes/Nahuel_Salamone_Token.png" alt="Nahuel Salamone" width="100" height="100">
    </td>
    <td style="border-right: 1px solid #ccc; border-top: none; padding: 10px;">
      <img src="img/Integrantes/Martin_Ferrari_Token.png" alt="Martin Ferrari" width="100" height="100">
    </td>
    <td style="border-right: 1px solid #ccc; border-top: none; padding: 10px;">
      <img src="img/Integrantes/Pablo_Chamena_Token.png" alt="Pablo Chamena" width="100" height="100">
    </td>
    <td style="border-top: none; border-right: 1px solid #ccc; padding: 10px;">
      <img src="img/Integrantes/Giada_de_Carlo_Token.png" alt="Giada de Carlo" width="100" height="100">
    </td>
  </tr>
</table>


