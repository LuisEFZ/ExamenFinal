import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Generación de Gráficas Estadísticas")

# Generar un DataFrame artificial con NumPy
np.random.seed(42)
data = {
    'Variable_A': np.random.normal(50, 10, 100),
    'Variable_B': np.random.normal(60, 15, 100),
    'Variable_C': np.random.normal(70, 20, 100),
    'Variable_D': np.random.normal(80, 5, 100)
}
df = pd.DataFrame(data)

# Mostrar el DataFrame generado
st.write("DataFrame Artificial:")
st.dataframe(df)

# Función para graficar un diagrama de barras
def plot_bar():
    fig, ax = plt.subplots()
    sns.barplot(data=df, ci=None, ax=ax)
    st.pyplot(fig)

# Función para graficar un violin plot
def plot_violin():
    fig, ax = plt.subplots()
    sns.violinplot(data=df, ax=ax)
    st.pyplot(fig)

# Función para graficar un diagrama de dispersión
def plot_scatter():
    fig, ax = plt.subplots()
    sns.scatterplot(x='Variable_A', y='Variable_B', data=df, ax=ax)
    st.pyplot(fig)

# Función para graficar un heatmap
def plot_heatmap():
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Función para graficar la correlación de Pearson
def plot_correlation():
    fig, ax = plt.subplots()
    corr_matrix = df.corr(method='pearson')
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Botones para cada tipo de gráfico
if st.button('Generar Diagrama de Barras'):
    plot_bar()

if st.button('Generar Violin Plot'):
    plot_violin()

if st.button('Generar Diagrama de Dispersión'):
    plot_scatter()

if st.button('Generar Heatmap'):
    plot_heatmap()

if st.button('Generar Gráfica de Correlación de Pearson'):
    plot_correlation()
