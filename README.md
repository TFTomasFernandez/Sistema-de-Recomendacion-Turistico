
# Proyecto Final SoyHenry

![Data Forge - Crafting the Awesome](img/data-forge-logo.jpg)
Data Forge - Crafting the Awesome


## Introducción
*Dataforge esta conformado por un conjunto de profesionales que busca entender los patrones del pasado para comprender mejor las tendencias actuales y ayudar de la mejor manera a construir el futuro.
El volcan, la representacion de nuestra pasion en su estado puro, utilizando nuestras habilidades y conocimientos para dar forma a ese deseo.*

Este proyecto esta orientado a acompañar una pasion que muchos de nosotros compartimos y uno de los hobbies favoritos de la humanidad: **Viajar**

## Índice
1. [Introducción](#introducción)
2. [Orientación del Proyecto](#orientación-del-proyecto)
   - [Modelo de Recomendación: Turismo Emergente](#modelo-de-recomendación-turismo-emergente)
   - [Base de Datos: Turismo de Interés](#base-de-datos-turismo-de-interés)
3. [Foco del Proyecto](#foco-del-proyecto)
4. [Creación de funciones](#creación-de-funciones)
5. [Análisis Exploratorio de los Datos (EDA)](#análisis-exploratorio-de-los-datos-eda)
6. [Modelo de Recomendación](#modelo-de-recomendación)
7. [Consideraciones Finales](#consideraciones-finales)

## Orientación del Proyecto
Este proyecto esta dividido en dos productos:
1. Un [Modelo de Recomendacion llamado 'Turismo Emergente'](#modelo-de-recomendacion:-turismo-emergente), que busca identificar lugares con potencial poco explotado de turismo en determinadas provincias en relacion a la region geografica.
2. Un [Base de Datos llamada 'Turismo de Interes'](#base-de-datos:-turismo-de-interes), que es una base de datos creada a partir de las busquedas llevadas a cabo en el sistema de recomendacion con intencion de informar a posibles inversores de puntos de interes y/o tendencias de busqueda.

A continuacion observaremos en mas detalle cada una de estos productos:

### Modelo de Recomendación: Turismo Emergente
El proyecto utiliza las bases de datos de [Yelp](https://www.yelp.com/) y [Google Maps](https://www.google.com/maps) otorgadas por el PO para formar un Sistema de Recomendacion haciendo una Vectorizacion de Reseñas para extraer palabras clave de un grupo especifico de Estados de USA donde el turismo esta disminuido o tiene propuestas de interes emergentes para sus posibles visitantes.

Utilizamos, ademas, un conjunto de fuentes adicionales como el [Sitio de Viajes Oficial de USA](https://www.visittheusa.com/) o el [Sitio oficial de Administracion de Viaje Internacional](https://www.trade.gov/) para hacer la seleccion de estados con potencial de crecimiento. [Mas adelante](#foco-del-proyecto) haremos un analisis mas profundo de los Estados elegidos, acompañado del rasonamiento utilizado.

El sistema de recomendacion sera consumido por el usuario en formato de pagina web, donde podremos encontrar menus que permiten personalizar la busqueda como, por ejemplo; actividades, comida, clima, etc. Al ejecutarse el sistema recomendara una lista de lugares con el mayor numero de coincidencias, ordenada por el promedio de las estrellas otorgadas de las reviews, y una serie de links:
- Algunos de los negocios mejor valorados de la zona.
- La busqueda de el area seleccionada en [Booking](https://booking.com/).
- La busqueda de el area seleccionada en [Airbnb](https://www.airbnb.com).

### Base de Datos: Turismo de Interés
Una vez establecido el Sistema de Recomendacion se creara una base de datos donde se almacenaran de manera sistematica las busquedas realizadas por los usuarios en la web, dando insigths sobre potenciales puntos de inversion y las tendencias de interes de los usuarios con la intencion de informar las decisiones tomadas por potenciales inversores.

La forma de consumo de dicha base de datos tambien sera en formato web, se le otorgara un usuario y contraseña al personal autorizado a acceder y una vez ingresado tendran dos pestañas centrales:
- Datos crudos, almacenados en un servidor para su procesamiento.
- Dashbord de datos procesados, con la informacion mas relevante al objetivo y el progreso de los KPIs.

## Foco del Proyecto
Tras un analizis completo de los datos disponibles sumado a algunos datos externos que consideramos relevantes para el proyecto nos definimos por dos Estados iniciales. Cabe recalcar que si el proyecto resulta fructifero seria interesante aumentar este numero. Los estados elegidos, acompañado con el razonamiento utilizado son:

### Luisiana

![Luisiana en el mapa](img/luisiana_maploc.png)

Luisiana se encuentra en una posicion *sumamente interesante*, ubicada entre dos potencias turisticas: **Florida** a la izquierda, **Texas** a la derecha.
Sus caracteristicas topograficas son similares a las de Florida, incluyendo playas caribeñas, bellos bosques tropicales y asombrosos pantanos. Sus ciudades son pintorescas, con una hermosa arquitectura inspirda en su mescla de culturas Francesa, Africana y Americana.
Algunas de sus ciudades llevan un espiritu festivo tanto de dia, con sus carnavales, desfiles y ferias, como de noche con sus fiestas callejeras y clubes nocturnos.

Sin embargo, a pesar de todo esto, la cantidad de visitantes internacionales lo pone en el **Ranking 23** de USA, con apenas unos **318.000 visitantes internacionales** (En comparacion a casi **2 millones de Texas**, en el puesto 5, y casi **8 millones de Florida** en el puesto 2).
Luisiana cuenta ademas con un crecimiento positivo, indicando cierto interes, pero el volumen de viajantes aumento tan solo en 4000 personas (1,3%) en el año 2023 respecto al 2022.

![Fuente: www.trade.gov](img/luisiana_rank.png)

## Tecnologias