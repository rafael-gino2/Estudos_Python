import pandas as pd
import streamlit as sl

sl.title("Dashboard de Alunos")

def carregando_dados():
    alunos = pd.read_csv('alunos_filtrado.csv', low_memory=False)
    matriculas = pd.read_csv('Matriculas_pii_none.csv', low_memory=False)
    processos = pd.read_csv('processos_seletivos_filtrado_atualizado.csv', low_memory=False, on_bad_lines='skip')

    alunos = alunos.dropna(axis=1, how='all')
    matriculas = matriculas.dropna(axis=1, how='all')
    processos = processos.dropna(axis=1, how='all')

    return alunos, matriculas, processos

alunos, matriculas, processos = carregando_dados()

sl.header("Graficos de")


# Análise de alunos ativos com base em 'Tipo de Matrícula'
if 'Tipo de Matricula' in matriculas.columns and 'Data de Desistência do Curso' in matriculas.columns:
    
    # Filtra apenas alunos com Tipo de Matricula desejado
    matriculas_filtradas = matriculas[matriculas['Tipo de Matricula'].isin(['Curso Base', 'Curso de Extensão'])]

    # Total de inscritos considerados (apenas Curso Base ou Extensão)
    total_inscritos = len(matriculas_filtradas)

    # Considera como ATIVOS quem NÃO desistiu
    ativos = matriculas_filtradas[matriculas_filtradas['Data de Desistência do Curso'].isna()]
    total_ativos = len(ativos)

    taxa_ativos = (total_ativos / total_inscritos) * 100 if total_inscritos > 0 else 0

    sl.header("Análise de Alunos Ativos (Curso Base e Extensão)")

    col1, col2, col3 = sl.columns(3)
    col1.metric("Total de Inscritos (Base + Extensão)", total_inscritos)
    col2.metric("Total Ativos (Cursando)", total_ativos)
    col3.metric("Taxa de Atividade (%)", f"{taxa_ativos:.2f}")

    # Gráfico com distribuição dos ATIVOS por tipo
    ativos_por_tipo = ativos['Tipo de Matricula'].value_counts().rename_axis('Tipo de Matricula').reset_index(name='Quantidade')
    ativos_por_tipo_df = ativos_por_tipo.set_index('Tipo de Matricula')

    sl.subheader("Distribuição de Ativos por Tipo de Matrícula")
    sl.bar_chart(ativos_por_tipo_df)

else:
    sl.warning("Colunas necessárias não encontradas: 'Tipo de Matricula' ou 'Data de Desistência do Curso'.")









# Gráfico de comparação entre Curso Base e Curso de Extensão
if 'Tipo de Matricula' in matriculas.columns:
    sl.subheader("Comparativo por Tipo de Matricula")

    tipo_matricula_counts = matriculas['Tipo de Matricula'].value_counts().rename_axis('Tipo de Matricula').reset_index(name='Quantidade')
    tipo_matricula_df = tipo_matricula_counts.set_index('Tipo de Matricula')

    sl.bar_chart(tipo_matricula_df)

else:
    sl.warning("Coluna 'Tipo de Matrícula' não encontrada nos dados.")


