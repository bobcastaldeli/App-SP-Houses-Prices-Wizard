# [São Paulo Houses Prices Wizard - App](https://sp-houses-prices-wizard.herokuapp.com/)



São Paulo Houses Prices Wizard é um web app com objetivo de prever preços de compra e aluguel de imóveis na cidade de São Paulo -SP com base nas especificações dadas pelo usuário. Este tipo de aplicativo facilita a pesquisa por ambos os tipos de players do mercado imobiliário.

Este projeto foi elaborado a partir de uma ***Previsão de preços de imóveis da cidade de São Paulo*** o objetivo principal é realizar previsões referentes aos preços de imóveis para **locação** e **venda**. Como o dataset contém ambos tipos de imóveis as analises foram divididas em dois notebooks diferentes, um contendo a análise e previsão de preços de aluguíes e um segundo notebook contendo a análise e previsão dos preços para imóveis para venda. Este conjunto de dados pode pode ser encontrado no [Kaggle](https://www.kaggle.com/argonalyst/sao-paulo-real-estate-sale-rent-april-2019/kernels). Neste repositório é possível encontrar dois notebooks com as análises e seleção dos algoritmos utilizados para realizar a previsão de preços do web app.

Por meio de uma análise neste dataset é possível foi possível a criação deste web app com a utilização do framework [streamlit](https://www.streamlit.io/) para front e back-end, o web app foi hospedado como uma platform as a service (PaaS) por meio do [Heroku](https://www.heroku.com/). O web app pode ser acesso por meio deste endereço https://sp-houses-prices-wizard.herokuapp.com/.

Para este projeto foram utilizados os seguintes pacotes:

* **Análise e manipulação de dados**
	* Numpy;
	* Pandas;
	* Pickle;

* **Machine Learning**
	* Scikit-Learn;
	* CatBoost;

* **Web App**
	* Streamlit;