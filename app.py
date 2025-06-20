import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import joblib

# Carregar o dataset Iris
data = load_iris()
# Criar a aplicação Streamlit
st.title('Classificação de Flores - Dataset Iris')
# Inputs do usuário
comprimento_sepala = st.slider('Comprimento da Sépala (cm)', 4.0, 8.0, 5.0)
largura_sepala = st.slider('Largura da Sépala (cm)', 2.0, 4.5, 3.0)
comprimento_petala = st.slider('Comprimento da Pétala (cm)', 1.0, 7.0, 4.0)
largura_petala = st.slider('Largura da Pétala (cm)', 0.1, 2.5, 1.0)
# Preparar os dados de entrada
entrada = np.array([[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]])
# Carregar o modelo salvo
modelo_carregado = joblib.load('model.pkl')
# Fazer a previsão
if st.button('Classificar'):
    previsao = modelo_carregado.predict(entrada)
    especie = data.target_names[previsao[0]]
    st.write(f'A flor prevista é da espécie: **{especie}**')