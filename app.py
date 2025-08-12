# Import necessary libraries
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Read CSV data
car_data = pd.read_csv('vehicles_us.csv')
print(car_data.head())


# Crear un encabezado para la aplicación de streamlit
st.header('Análisis preliminar de vehículos usados')

st.write('Esta aplicación muestra algunos gráficos con el análisis de datos relativos a la eficiencia de vehículos usados.')
# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Adición de un botón para un gráfico de dispersión
scatter_button = st.button(
    'Construir gráfico de dispersión (Odometer vs. Price)')
if scatter_button:
    st.write('Gráfico de dispersión: Odómetro vs Precio')
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(
            color=car_data['model_year'],  # Color por año
            colorscale='Viridis',
            showscale=True,
            size=8,
            opacity=0.7
        )
    )])
    fig_scatter.update_layout(
        title_text='Precio vs Kilometraje (Color por año)',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Construir casillas de verificación
    # Casilla de verificación para el histograma
build_histogram = st.checkbox('Mostrar histograma (Odómetro)')

if build_histogram:
    st.write('Distribución del odómetro de vehículos')
    fig_hist = go.Figure(data=[go.Histogram(
        x=car_data['odometer'],
        marker=dict(color='royalblue'))
    ])
    fig_hist.update_layout(
        title_text='Histograma del Odómetro',
        xaxis_title='Millas recorridas',
        yaxis_title='Cantidad de vehículos'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el scatter plot
build_scatter = st.checkbox(
    'Mostrar gráfico de dispersión (Odómetro vs Precio)')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(
            color=car_data['model_year'],
            colorscale='Viridis',
            showscale=True,
            size=8,
            opacity=0.6
        )
    )])
    fig_scatter.update_layout(
        title_text='Precio vs Odómetro (Color por año)',
        xaxis_title='Millas recorridas',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mensaje si no hay selección
if not build_histogram and not build_scatter:
    st.info('Selecciona al menos una opción para visualizar gráficos.')
