import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# Datos de ejemplo
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': [1500, 2300, 3100, 2800, 3400, 4200],
    'Objetivo': [2000, 2500, 3000, 3500, 4000, 4500]
}

df = pd.DataFrame(data)

# Crear gráfica de barras para las ventas
trace1 = go.Bar(
    x=df['Mes'],
    y=df['Ventas'],
    name='Ventas',
    marker={'color': 'blue'}
)

# Crear gráfica de línea para el objetivo de ventas
trace2 = go.Scatter(
    x=df['Mes'],
    y=df['Objetivo'],
    mode='lines+markers',
    name='Objetivo',
    line={'color': 'orange'}
)

# Configuración del layout
layout = go.Layout(
    title='Crecimiento de Ventas',
    xaxis={'title': 'Mes'},
    yaxis={'title': 'Cantidad de Ventas'},
    barmode='group'
)

# Crear la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrar la gráfica en Streamlit
st.title('Crecimiento de Ventas')
st.plotly_chart(fig)
