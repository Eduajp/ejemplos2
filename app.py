import pandas as pd

# Cargar el conjunto de datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar las primeras filas
print(df.head())
import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.header("Análisis Exploratorio de Vehículos en Venta")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para construir histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para el odómetro')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del kilometraje (odómetro)")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para construir gráfico de dispersión
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs. Kilometraje')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre kilometraje y precio",
                             opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)