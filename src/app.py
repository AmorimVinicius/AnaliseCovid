import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados


## parametro default, deve ser o ultimo elemento da funcao
def grafico_comparativo(dados_2019, dados_2020, causa, uf = "BRASIL"):

    if uf == "BRASIL":
        total_2019 = dados_2019.groupby("tipo_doenca").sum()
        total_2020 = dados_2020.groupby("tipo_doenca").sum()
        lista = [int(total_2019.loc[causa]), int(total_2020.loc[causa])]
    else:    
        total_2019 = dados_2019.groupby(["uf", "tipo_doenca"]).sum()
        total_2020 = dados_2020.groupby(["uf", "tipo_doenca"]).sum()
        lista = [int(total_2019.loc[uf, causa]), int(total_2020.loc[uf, causa])]

    dados = pd.DataFrame({"Total": lista, 
                            "Ano": [2019, 2020]})

    # plt.figure(figsize = (8,6))
    return sns.barplot(x = "Ano", y = "Total", data = dados)
    # plt.title(f"Óbitos por {causa} - {uf}")
    # plt.show()

    ## a renderizacao da imagem, sera feita pelo stremlit


def main():
    
    obitos_2019 = pd.read_csv("dados\obitos-2019.csv")
    obitos_2020 = pd.read_csv("dados\obitos-2020.csv")
    figura = grafico_comparativo(obitos_2019, 
                                 obitos_2020, 
                                 "SRAG")
    
    # st.dataframe(obitos_2019)

    st.title("Análise de óbitos 2019-2020")
    st.markdown("Este trabalho analisa os dados dos **óbitos 2019-2020**")

    ## renderizando imagem com pyplot
    st.pyplot(figura)

  
## executar primeiro o main()
if __name__ == "__main__":
    main()