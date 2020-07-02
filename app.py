# App para prvisão de preços de imóveis para aluguéis e preços de venda para a cidade de São Paulo
# Import das bibliotecas
import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from catboost import CatBoostRegressor

def data_prep(dataset):
    
	# Encoding das Variáveis
	dataset['Elevator'] = dataset['Elevator'].map({'yes':1, 'no':0})
	dataset['Furnished'] = dataset['Furnished'].map({'yes':1, 'no':0})
	dataset['Swimming_Pool'] = dataset['Swimming_Pool'].map({'yes':1, 'no':0})

	# Criando a variável "Comercial"
	dataset['Comercial'] = (dataset['Price'] >= 8000) | (dataset['Size'] >= 200)
	dataset['Comercial'] = dataset['Comercial'].map({True: 1, False: 0})
	# Valor do metro quadrado por apartamento
	dataset['m2_Value'] = np.round((dataset['Price'] + dataset['Condo']) / dataset['Size'])
    

	return dataset

# Título
st.title('''
	São Paulo Houses Prices Wizard
		 ''')

st.image('SP-Skyline.jpg', use_column_width=True)
st.markdown('''Este é um web app criado para previsão de preços de imóveis na cidade de São Paulo \
	        o mesmo pode ser usado para prever preços de aluguel ou preços venda de imóveis. \
	        'Fique a vontade para experimetar :smiley:.
	        ''')

#st.sidebar.info('Qual tipo de finalide tem interesse em prver')
st.sidebar.title('Web App para Previsão de Preços de Imóveis em São Paulo - SP')
add_selectbox = st.sidebar.selectbox(
	'Escolha a Finalidade', ('Alugar', 'Comprar', 'About'))

st.sidebar.image('SP-Center.jpg', use_column_width=True)

if add_selectbox == 'Alugar':

	Size = st.number_input('Tamanho', min_value=30, max_value=880)
	Rooms = st.selectbox('Quantidade de Quartos', [1,2,3,4,5,6,7,8,9,10])
	Suites = st.selectbox('Quantidade de Suites', [0,1,2,3,4,5])
	Toilets = st.selectbox('Quantidade de banheiros', [1,2,3,4,5,6,7,8])
	
	if st.checkbox('Elevador'):
		Elevator = 'yes'
	else:
		Elevator = 'no'
	
	if st.checkbox('Imóvel Mobiliado'):
		Furnished = 'yes'
	else:
		Furnished = 'no'

	if st.checkbox('Piscina'):
		Swimming_Pool = 'yes'
	else:
		Swimming_Pool = 'no'
	
	Parking = st.selectbox('Vagas no Estacionamento', [0,1,2,3,4,5,6,7,8,9])
	Condo = st.number_input('Taxa de Condomínio', min_value=1, max_value=9500)
	Price = st.number_input('Valor que está disposto a pagar', min_value=480, max_value=50000)

	data ={'Condo':Condo,
	   	   'Size':Size, 
	   	   'Rooms':Rooms,
	       'Toilets':Toilets,
	       'Suites':Suites,
           'Parking':Parking,
           'Elevator':Elevator,
           'Furnished':Furnished,
           'Swimming_Pool':Swimming_Pool,
           'Price':Price}

	rent = pd.DataFrame(data, index=[0])
	X_test = data_prep(rent)

	df_cols =['Condo', 'Size', 'Rooms','Toilets', 
          	  'Suites', 'Parking', 'Elevator', 'Furnished', 
              'Swimming_Pool', 'Comercial', 'm2_Value']


	if st.button('Predict'):

		model = pickle.load(open('Model/Rental_CatBoost.pkl', 'rb'))
		ans = model.predict(rent[df_cols])
		st.subheader(f'O preço do imóvel com as características que você deseja alugar é {np.round(ans, 2)} (INR) ')

if add_selectbox == 'Comprar':
	
	Size = st.number_input('Tamanho', min_value=30, max_value=880)
	Rooms = st.selectbox('Quantidade de Quartos', [1,2,3,4,5,6,7,8,9,10])
	Suites = st.selectbox('Quantidade de Suites', [0,1,2,3,4,5])
	Toilets = st.selectbox('Quantidade de banheiros', [1,2,3,4,5,6,7,8])
	
	if st.checkbox('Elevador'):
		Elevator = 'yes'
	else:
		Elevator = 'no'
	
	if st.checkbox('Imóvel Mobiliado'):
		Furnished = 'yes'
	else:
		Furnished = 'no'

	if st.checkbox('Piscina'):
		Swimming_Pool = 'yes'
	else:
		Swimming_Pool = 'no'
	
	Parking = st.selectbox('Vagas no Estacionamento', [0,1,2,3,4,5,6,7,8,9])
	Condo = st.number_input('Taxa de Condomínio', min_value=1, max_value=9500)
	Price = st.number_input('Valor que está disposto a pagar', min_value=42000, max_value=10000000)

	data ={'Condo':Condo,
	   	   'Size':Size, 
	   	   'Rooms':Rooms,
	       'Toilets':Toilets,
	       'Suites':Suites,
           'Parking':Parking,
           'Elevator':Elevator,
           'Furnished':Furnished,
           'Swimming_Pool':Swimming_Pool,
           'Price':Price}

	sale = pd.DataFrame(data, index=[0])
	X_test = data_prep(sale)

	df_cols =['Condo', 'Size', 'Rooms','Toilets', 
          	  'Suites', 'Parking', 'Elevator', 'Furnished', 
              'Swimming_Pool', 'Comercial', 'm2_Value']


	if st.button('Predict'):

		model = pickle.load(open('Model/Sales_GradBoost.pkl', 'rb'))
		ans = model.predict(sale[df_cols])
		st.subheader(f'O preço do imóvel com as características que você deseja comprar é {np.round(ans, 2)} (INR) ')

if add_selectbox == 'About':

	st.markdown('''
		**São Paulo Houses Prices Wizard** é um **web app** com objetivo de prever preços de compra e aluguel de imóveis na cidade de \
		São Paulo -SP com base nas especificações dadas pelo usuário. Este tipo de aplicativo facilita a pesquisa por ambos os \
		tipos de players do mercado imobiliário.

		Este projeto foi desenvolvido por [Roberto Castaldeli](https://www.linkedin.com/in/robertocastaldeli/). A documentação deste \
		projeto pode ser encotrada no meu [Github](https://github.com/bobcastaldeli).
		''')

	st.image('about-me.jpg', use_column_width=True)

