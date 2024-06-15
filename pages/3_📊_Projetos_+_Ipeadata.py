st.write(ListaSelic)'''
st.code(code, language='python')

df = main.carrega("https://raw.githubusercontent.com/WesleyInfoBr2/streamlit_Lista3/main/projetos.csv")
df = pd.read_csv("https://raw.githubusercontent.com/WesleyInfoBr2/streamlit_Lista3/main/projetos.csv", sep=";") 
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
