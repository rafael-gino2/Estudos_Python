import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Carrega o arquivo CSV
df = pd.read_csv("Matriculas_pii_none.csv")

st.title("Análise de Matrículas - Escola da Nuvem")

total_matriculas = len(df)
desistentes = df["Data de Desistência do Curso"].notna().sum()
ativos = df["Data de Desistência do Curso"].isna().sum()

# Métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Matrículas", total_matriculas)
with col2:
    st.metric("Total de Desistentes", desistentes)
with col3:
    st.metric("Total de Ativos", ativos)






# ---------------------- Certificação ---------------------------
# ---------------------- Certificação AWS (Aprovado x Reprovado) ---------------------------
st.subheader("Certificação AWS")

cert_status_map = {
    "Aprovado": ["Aprovado", "Passou", "Passed"],
    "Reprovado": ["Não passou", "Reprovado", "NoShow", "Reprovado por falta", "Desistente"]
}

for cert in ["AWS Certified Cloud Practitioner", "AWS Certified Solutions Architect Associate"]:
    if cert in df.columns:
        cert_raw = df[cert].dropna().astype(str)

        # Classifica os status como Aprovado ou Reprovado
        cert_classif = cert_raw.apply(lambda x: "Aprovado" if any(kw in x for kw in cert_status_map["Aprovado"])
                                      else "Reprovado")

        # Conta valores
        cert_counts = cert_classif.value_counts().reset_index()
        cert_counts.columns = ["Resultado", "Quantidade"]

        # Cria gráfico
        fig_cert = px.pie(
            cert_counts,
            names="Resultado",
            values="Quantidade",
            title=f"Aprovação na Certificação: {cert}",
            color="Resultado",
            color_discrete_map={"Aprovado": "green", "Reprovado": "red"}
        )
        st.plotly_chart(fig_cert)

# ---------------------- Análise de Desistências a partir de Outubro de 2024 ---------------------------
st.subheader("Meses com Mais Desistências (Desde Out/2024)")

# Garantir que as datas estejam corretas
df['Data de Desistência do Curso'] = pd.to_datetime(df['Data de Desistência do Curso'], dayfirst=True, errors='coerce')
df['Hora da modificação'] = pd.to_datetime(df['Hora da modificação'], dayfirst=True, errors='coerce')

# Trata a data usada como base para a desistência
desistencias = df[(df['Estágio'] == 'Desistência') | (df['Estágio'] == 'Sem interesse')].copy()
desistencias['Data Desistência'] = desistencias['Data de Desistência do Curso'].fillna(desistencias['Hora da modificação'])
desistencias['Mês/Ano'] = desistencias['Data Desistência'].dt.to_period('M')

# Filtra a partir de Outubro de 2024
desistencias = desistencias[desistencias['Mês/Ano'] >= '2024-10']

# Conta desistências por mês
desistencias_contagem = desistencias['Mês/Ano'].value_counts().sort_index()

# Cria DataFrame
dados = pd.DataFrame({
    'Mês/Ano': [str(m) for m in desistencias_contagem.index],
    'Desistências': desistencias_contagem.values
})

# Ordena do maior para o menor
dados = dados.sort_values(by='Desistências', ascending=False)

# ----- GRÁFICO -----
fig = go.Figure()
fig.add_trace(go.Bar(
    x=dados['Mês/Ano'],
    y=dados['Desistências'],
    marker_color='orange',
    name='Desistências'
))

fig.update_layout(
    title='Meses com Mais Desistências (Desde Outubro de 2024)',
    xaxis_title='Mês/Ano',
    yaxis_title='Quantidade de Desistências',
    barmode='group'
)

st.plotly_chart(fig)




st.subheader("Evolução Mensal: Aprovados x Reprovados (AWS CCP e CSSA)")

df['Hora da modificação'] = pd.to_datetime(df['Hora da modificação'], dayfirst=True, errors='coerce')

status_map = {
    "Aprovado": ["Aprovado", "Passou", "Passed"],
    "Reprovado": ["Não passou", "Reprovado", "NoShow", "Reprovado por falta", "Desistente"]
}

def classificar_resultado(valor):
    valor_str = str(valor).lower()
    if any(k.lower() in valor_str for k in status_map["Aprovado"]):
        return "Aprovado"
    else:
        return "Reprovado"

# Função para processar os dados de uma certificação
def processar_certificacao(coluna_cert):
    temp = df[['Hora da modificação', coluna_cert]].dropna()
    temp['Resultado'] = temp[coluna_cert].apply(classificar_resultado)
    temp['Mês/Ano'] = temp['Hora da modificação'].dt.to_period('M').astype(str)
    return temp[['Mês/Ano', 'Resultado']]

# Processar CCP e CSSA
ccp = processar_certificacao('AWS Certified Cloud Practitioner')
cssa = processar_certificacao('AWS Certified Solutions Architect Associate')

# Unir os dois dataframes
df_resultados = pd.concat([ccp, cssa], ignore_index=True)

# Agrupar por mês/ano e resultado (somando CCP + CSSA)
resultado_mes = df_resultados.groupby(['Mês/Ano', 'Resultado']).size().reset_index(name='Quantidade')

# Criar gráfico
fig = px.bar(
    resultado_mes,
    x="Mês/Ano",
    y="Quantidade",
    color="Resultado",
    barmode="group",
    title="Evolução Mensal das Certificações (AWS CCP + CSSA)"
)

st.plotly_chart(fig)



# ---------------------- Desistência ---------------------------
st.subheader("Top 5 Motivos de Desistência")

# Remove valores nulos e conta ocorrências
desistencia = df["Motivo da Desistência"].dropna()
desistencia_df = desistencia.value_counts().reset_index()
desistencia_df.columns = ['Motivo da Desistência', 'Quantidade']

# Pega apenas os 5 primeiros
desistencia_df = desistencia_df.head(5)

# Cria gráfico
fig_desistencia = px.bar(
    desistencia_df,
    x='Motivo da Desistência',
    y='Quantidade',
)

st.plotly_chart(fig_desistencia)