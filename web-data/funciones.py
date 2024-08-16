# # #Modulo de funciones
from sklearn.metrics.pairwise import cosine_similarity
# from collections import Counter


def similaridad(df, texto,vectorizador,matriz):
    new_text_vector = vectorizador.transform([texto])
    similarity_scores = cosine_similarity(new_text_vector, matriz)
    documentos_mas_similares = similarity_scores[0].argsort()[::-1] # indices de los valores mas similares
    # Filtrar índices fuera de rango
    documentos_mas_similares = [i for i in documentos_mas_similares if i < len(df)]
    # Solo seleccionamos los datos que tienen un índice válido
    datos_similares = df.iloc[documentos_mas_similares].copy()
    datos_similares.loc[:, 'similarity_score'] = similarity_scores[0][documentos_mas_similares]
    return datos_similares



def recomendar_ciudad(df_sin_filtrar):
    # 1.0: Filtrar ciudades con más de 100 negocios únicos
    unicos = df_sin_filtrar.groupby('city')['name'].nunique().reset_index()
    unicos.columns = ['ciudad', 'unicos']
    ciudades_filtradas = unicos[unicos['unicos'] > 20]['ciudad']
    df_filtrado = df_sin_filtrar[df_sin_filtrar['city'].isin(ciudades_filtradas)]
    # 1.1: Filtrar por la ciudad con el mayor puntaje de similitud promedio
    promedio_por_ciudad = df_filtrado.groupby('city')['similarity_score'].mean().reset_index()
    promedio_por_ciudad = promedio_por_ciudad.sort_values(by='similarity_score', ascending=False)
    ciudad_recomendada = promedio_por_ciudad.iloc[0].values[0]
    df_filtrado = df_filtrado[df_filtrado['city'] == ciudad_recomendada]
    # 1.2: Filtrar negocios con más de 3.5 estrellas promedio
    promedio_estrellas_negocio = df_filtrado.groupby('name')['stars_review'].mean().reset_index()
    promedio_estrellas_negocio = promedio_estrellas_negocio.query('stars_review > 3.5')
    df_final = df_filtrado.merge(promedio_estrellas_negocio, on='name', how='left', suffixes=('', '_promedio'))
    df_final.dropna(subset=['stars_review_promedio'], inplace=True)
    # 1.3: Filtrar por target = 1
    #df_final = df_final[df_final['target'] == 1]
    # 1.4: Filtrar por similarity_score > 0
    df_final = df_final[df_final['similarity_score'] > 0]
    # 1.5: Eliminar duplicados por nombre de negocio
    df_final.drop_duplicates(subset='name', inplace=True)
    return df_final


