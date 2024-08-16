# <div align="center" > Procesamiento y limpieza de los datos
</div>

<div align="center"><img src="https://www.tridant.com/wp-content/uploads/2022/07/azure-cloud-data-ecosystem.jpg"> </div>


## Tabla de contenido

1. ### [Ciclo de vida del dato](#ciclo-de-vida-del-dato)
2. ### [Distribucion del trabajo por archivo](#distribucion-del-trabajo-por-archivo)
3. ### [Datasets](#datasets)



## Ciclo de vida del dato
Como primera instancia se inyectan los datos de los <i>datasets</i> de `Google Maps` y `Yelp` a los cuales se les realizo un proceso de **ETL** (<u>Extraccion, Transformacion y Carga </u> (por sus siglas en ingles)). Este proceso es administrado en **Google Cloud** en donde utilizaremos la herramienta de *Google Composer* para automatizar el trabajo, ejecutandose una vez al mes.<br>

Este proceso de automatizacion lo puedes en encontrar en los siguientes archivos: <br>
[`src/dag.py`](../src/dag.py): Ya que *Google Composer* trabajo con *Airflow*, realizamos lo que se conoce como *DAG* (Directed Acyclic Graph) para que ejecute los archivos que realizaran el *ETL*. <br>
[`src/combined.py`](../src/combined.py) y [`src/business_etl.py`](../src/business_etl.py): Archivos donde se encuentra el ETL realizado

Luego de este proceso, los datos son redirigidos hacia `Big Query`. Aqui los datos seran utilizados tanto por un sistema de recomendacion utilizando Machine Learning y la presentacion visual de los datos en un *dashboard*.

Una vez tengamos los datos limpios, se les aplico un analisis exploratorio (**EDA**) de los mismos, para detectar tendencias y patrones. El analisis anteriormente mencionado los puedes visualizar haciendo click [aqui](./EDA/eda.ipynb).

## Distribucion del trabajo por archivo
`ETL/business_yelp.ipynb:` limpieza del archivo que contiene los negocios de Yelp <br>
`ETL/business_google.ipynb:` limpieza y unificacion de los archivos que contiene los negocios de Google Maps <br>
`ETL/estados.ipynb:` limpieza y unificacion de los archivos que contiene los estados a analizar (Louisiana e Indiana). <br>
`ETL/googleMerge.ipynb:` Unificacion de los archivos resultantes de `estados.ipynb` y `business_google.ipynb`. <br>
`ETL/yelpMerged.ipynb:` Unificacion de los archivos resultantes de `business_yelp.ipynb` y del archivo en crudo *reviews.json* que puedes encontrar en los links al final de este documento


## Datasets
En los siguientes enlaces puedes encontrar los datos utilizados:
- <a href="https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF">Datos en crudo Yelp </a>
- <a href="https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA">Datos en crudo Google Maps </a>
- <a href="https://drive.google.com/drive/folders/1zTELkvEirOUWKmtd17N2i2ohSR4TDVLy?usp=sharing">Datos limpios</a>