import pandas as pd
import streamlit as st
import dask.dataframe as dd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import pydeck as pdk

###############################################
# Configuaracion  de pagina
st.set_page_config(
    page_title="TURISMO EMERGENTE",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS styling
st.markdown(
    """
<style>
[data-testid="block-container"] {
padding-left: 2rem;
padding-right: 2rem;
padding-top: 1rem;
padding-bottom: 0rem;
margin-bottom: -7rem;
}
[data-testid="stVerticalBlock"] {
padding-left: 0rem;
padding-right: 0rem;
}
[data-testid="stMetric"] {
background-color: #393939;
text-align: center;
padding: 15px 0;
}
[data-testid="stMetricLabel"] {
display: flex;
justify-content: center;
align-items: center;
}
</style>
""",
    unsafe_allow_html=True,
)
#############################################
# importar datos

br = pd.read_parquet("DATA/br.parquet")
indiana = pd.read_parquet("DATA/indiana.parquet")
louisiana = pd.read_parquet("DATA/louisiana.parquet")

df_in_lu = pd.merge(
    indiana, louisiana, on=["name", "address", "latitude", "longitude"], how="outer"
)
df = pd.merge(
    df_in_lu, br, on=["name", "address", "latitude", "longitude"], how="outer"
)


####################################################################
# titulo
st.image(r'C:\Users\giada\Desktop\Immagine WhatsApp 2024-07-27 ore 20.10.04_9caacf98.jpg', width=200)
st.title("TURISMO EMERGENTE")
# subtitulo
st.write("## Valutacion del estado del turismo emergente en Indiana y Louisiana")



# Sidebar
st.sidebar.markdown("### Bienvenido!")
st.sidebar.markdown(
    "Aqui puedes filtrar por estado, n. de estrellas, tipo de negocio o ciudad"
)

with st.sidebar:
    st.title("Turismo emergente en USA")

    # selecciona el ano de interes
    state = st.sidebar.selectbox("Estado", pd.unique(br["state"]))

    # selecciona la provincia de interes
    stars = st.sidebar.selectbox("Estrellas", pd.unique(br["stars_review"]))

    # categorias
    categories = st.sidebar.selectbox("Tipo de negocio", pd.unique(br["categories"]))

    # ciudad
    city = st.sidebar.selectbox("Ciudad", br[br["state"] == state]["city"].unique())

    st.write("Data Forge")


br_city = br[(br["state"] == state) & (br["city"] == city)]



with st.container():

    column1, column2 = st.columns(2)

    with column1:
        # Mappa per Indiana
        st.subheader("Mapa de Indiana")
        st.map(indiana[["latitude", "longitude"]])

        br_filtered = br[
            (br["state"] == state)
            & (br["city"] == city)
            & (br["stars_review"] == stars)
        ]
        # Separar las categorias
        br_filtered["categories"] = br_filtered["categories"].str.split(", ")
        br_exploded = br_filtered.explode("categories")
        # Resenas totales por categorias
        category_counts = br_exploded["categories"].value_counts().reset_index()
        category_counts.columns = ["categories", "review_count"]
        category_counts = category_counts[category_counts["review_count"] > 1000]
        # Grafico
        fig = px.bar(
            category_counts,
            x="categories",
            y="review_count",
            title=f"Numeros de resenas por categorias en {state}",
            labels={
                "Numero di Recensioni": "Numero di Recensioni",
                "Categoria": "Categoria",
            },
            color='review_count',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig)

        ########################################
        # KPI2 Incremento de 0,5 puntos en el proximo semestre en las valutaciones
        current_mean_rating = br_city['stars_mean'].mean()
        future_mean_rating = current_mean_rating + 0.5
        increment = future_mean_rating - current_mean_rating

        # Creacion DF para el plot
        kpi_data = pd.DataFrame({
            'Prevision': ['Current Rating', 'Future Rating'],
            'Evaluacion': [current_mean_rating, future_mean_rating]
        })
        

        #   Crear el grafico con Plotly Express
        fig = px.bar(
            kpi_data,
            x='Prevision',
            y='Evaluacion',
            text='Evaluacion',
            title=f'KPI 1: Incremento de 0.5 puntos en el proximo semestre en {city}, {state}',
            color='Evaluacion',
            color_discrete_map={'Current Rating': 'yellow', 'Future Rating': 'orange'}
        )

        # Personalizacion
        fig.update_layout(
            yaxis_title='Evaluacion',
            xaxis_title='Prevision',
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            showlegend=False  # Nascondi la legenda se non necessaria
        )

        # Muestra grafico en streamlit
        st.plotly_chart(fig)

        # Extrae el ano de la columna date
        indiana['year'] = pd.to_datetime(indiana['date']).dt.year
        louisiana['year'] = pd.to_datetime(louisiana['date']).dt.year

        # Conteo de las resenas por ano
        reviews_per_year = indiana['year'].value_counts().sort_index()

        # Creacion grafico a lineas
        fig = px.line(
            reviews_per_year,
            x=reviews_per_year.index,
            y=reviews_per_year.values,
            labels={'x': 'Año', 'y': 'Cantidad de Reseñas'},
            title="Reseñas por Año en Indiana",
            line_shape='linear'
        )

        # Personalizar lineas y colores
        fig.update_traces(line=dict(color="orange", width=3))

        # Anadir grilla
        fig.update_layout(
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )   

        # Visualizacion grafico
        st.plotly_chart(fig)

###########################################################
    with column2:
        st.subheader("Mapa de Louisiana")
        st.map(louisiana[["latitude", "longitude"]])

        # Grafico de resenas por valutacion
        br_city = br[(br["state"] == state) & (br["city"] == city)]

        # Creacion grafico interactivo con plotly
        fig = px.pie(
            br_city["stars_review"].value_counts().sort_index().reset_index(),
            names="stars_review",  # Questa colonna contiene le diverse valutazioni (stars_review)
            values="count",  # Questa colonna contiene il conteggio delle valutazioni
            title=f"Distribucion de las resenas per evaluacion en {city}",
            color='stars_review',  # Questa colonna contiene le diverse valutazioni (stars_review)
            color_discrete_sequence=px.colors.sequential.Magma  # Usa la scala di colori 'Inferno'
        )
        st.plotly_chart(fig)



        # KPI2 Calcular incremento 5% resenas positivas para el proximo ano
        positive_reviews = br_city[br_city["stars_review"] >= 4]
        # numero actual de resenas
        current_positive_reviews = len(positive_reviews)
    
        incremented_positive_reviews = current_positive_reviews * 1.05

        # Visualizar el KPI
        kpi_data = pd.DataFrame(
            {
                "Tipo": ["Actual", "Previsto (Proximo ano)"],
                "Numero de resenas": [current_positive_reviews, incremented_positive_reviews],
            }
        )
        color_map = {
            'Categoria 1': 'white', 
            'Categoria 2': 'red'  }

        # Crear grafico interactivo con plotly
        
        fig = px.bar(
            kpi_data,
            x="Tipo",
            y="Numero de resenas",
            title=f"#KPI 2 : Incremento del 5% de las Resenas Positivas por {city}, {state}",
            labels={"Numero de resenas": "Numero de resenas positivas"},
            text_auto=True,
            color = 'Tipo',
            color_discrete_map=color_map
        )

        # Visualizar grafico
        st.plotly_chart(fig)
        

        #
        reviews_per_year = louisiana['year'].value_counts().sort_index()
        
        # Creacion grafico de lineas
        fig = px.line(
            reviews_per_year,
            x=reviews_per_year.index,
            y=reviews_per_year.values,
            labels={'x': 'Año', 'y': 'Cantidad de Reseñas'},
            title="Reseñas por Año en Indiana",
            line_shape='linear'
        )
        # Personalizar lineas y colores
        fig.update_traces(line=dict(color="red", width=3))
        # Anadir grilla
        fig.update_layout(
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )   
        #  Visualizar grafico en streamlit
        st.plotly_chart(fig)

    # Filtrar Dataframe por estado
    df_filtered = df[df['state'] == state]

    # Valutacion media de las ciudades
    df_grouped = df_filtered.groupby("city")["stars_mean"].mean().reset_index()

    # Creacion del grafico de barras
    fig = px.bar(
        df_grouped,
        x='city',
        y='stars_mean',
        title=f"Valutacion media de las empresas por ciudad en {state}",
        labels={'stars_mean': 'Valutacion media', 'city': 'Ciudad'},
        color_continuous_scale='inferno',  
        text='stars_mean'  # Mostra i valori sulle barre
    )

    # Personalizacion de garfico
    fig.update_layout(
        xaxis_title='Ciudad',
        yaxis_title='Valutacion media',
        title_x=0.5,  # Centra il titolo del grafico
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )

    # Muestra el grafico en Streamlit
    st.plotly_chart(fig)
    

######################################################################################################################################

'''
df_indiana = df[df["state"] == "Indiana"]
df_filtered = df[df['state'] == state]
st.subheader(f"Valutacion media de las empresas por ciudad en {state}")
fig, ax = plt.subplots()
df_grouped = df_filtered.groupby("city")["stars_mean"].mean().reset_index()
df_grouped.plot(kind="bar", x="city", y="stars_mean", ax=ax, color='orange', legend=False)
ax.set_ylabel("Valutacion media")
ax.set_xlabel("Ciudad")
st.pyplot(fig)'''

"""st.write('br')
st.write(br.head())
st.write('indiana')
st.write(indiana.head())
st.write('louisiana')
st.write(louisiana.head())"""