import streamlit as st


st.sidebar.markdown('Desenvolvido por [Lucas Gabriel](https://github.com/lucasgabrieleng/Streamlit-Sales)')

st.markdown('# Analisador de Vendas')

st.divider()

st.markdown(
    '''
    Esse projeto foi desenvolvido baseado nos conteúdos ministrados pela Asimov Academy ***(https://www.asimov.academy.com)***.

    Utilizaremos três principais bibliotecas para o seu desenvolvimento:

    - `pandas`: para manipulação de dados em tabelas
    - `plotly`: para geração de gráficos
    - `streamlit`: para criação desse webApp interativo que você se encontra nesse momento

    Os dados utilizados foram gerados pelo script 'gerador_de_vendas.py' que se encontra junto do código fonte do projeto. Os dados podem ser visualizados na aba de tabelas!

    '''
            )