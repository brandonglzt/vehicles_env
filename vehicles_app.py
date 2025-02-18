import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")  # Leer el conjunto de datos

st.title("📊 Análisis de anuncios de coches en EE.UU.")
st.write("Esta aplicación permite visualizar datos sobre anuncios de coches usados.")

# Histograma de Odómetro

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión (Precio vs Año)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre el año y el precio")
    fig = px.scatter(car_data, x="model_year", y="price",
                     title="Relación entre Año y Precio de los coches")
    st.plotly_chart(fig, use_container_width=True)

# Reemplazar botones con checkboxes

st.subheader("Selecciona el tipo de gráfico que deseas visualizar")

if st.checkbox("Mostrar histograma del odómetro"):
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar gráfico de dispersión Año vs. Precio"):
    st.write("Creación de un gráfico de dispersión entre el año y el precio")
    fig = px.scatter(car_data, x="model_year", y="price",
                     title="Relación entre Año y Precio de los coches")
    st.plotly_chart(fig, use_container_width=True)
