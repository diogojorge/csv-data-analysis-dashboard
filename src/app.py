import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Análise de Vendas",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Análise de Vendas - Avançado")
st.markdown("Sistema interativo para análise de dados de vendas a partir de arquivos CSV.")

st.sidebar.header("📁 Fonte de Dados")
uploaded_file = st.sidebar.file_uploader("Carregue seu arquivo CSV", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    # Conversão de datas
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    if 'Ticket date' in df.columns:
        df['Ticket date'] = pd.to_datetime(df['Ticket date'], errors='coerce')
    return df

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.sidebar.success("Arquivo carregado com sucesso!")
else:
    st.warning("⚠️ Por favor, faça o upload de um arquivo CSV na barra lateral para iniciar a análise.")
    st.stop()

st.sidebar.header("🔍 Filtros")

if 'Region' in df.columns:
    regions = df['Region'].unique().tolist()
    selected_regions = st.sidebar.multiselect("Filtrar por Região", regions, default=regions)
    df = df[df['Region'].isin(selected_regions)]

if 'Line of Product' in df.columns:
    lines = df['Line of Product'].unique().tolist()
    selected_lines = st.sidebar.multiselect("Filtrar por Linha de Produto", lines, default=lines)
    df = df[df['Line of Product'].isin(selected_lines)]

st.subheader("📈 Indicadores Gerais")

total_sales = df['Sales'].sum() if 'Sales' in df.columns else 0
total_orders = len(df)
avg_ticket = total_sales / total_orders if total_orders > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {total_sales:,.2f}")
col2.metric("Número de Pedidos", f"{total_orders:,}")
col3.metric("Ticket Médio", f"R$ {avg_ticket:,.2f}")

st.markdown("---")
st.subheader("📊 Estatísticas Descritivas (Métricas Avançadas)")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
if numeric_cols:
    selected_metric_col = st.selectbox("Selecione a coluna para detalhamento estatístico:", numeric_cols, index=numeric_cols.index('Sales') if 'Sales' in numeric_cols else 0)
    
    col_stat1, col_stat2, col_stat3, col_stat4, col_stat5 = st.columns(5)
    
    val_min = df[selected_metric_col].min()
    val_max = df[selected_metric_col].max()
    val_mean = df[selected_metric_col].mean()
    val_median = df[selected_metric_col].median()
    val_std = df[selected_metric_col].std()

    prefix = "R$ " if selected_metric_col == 'Sales' else ""
    
    col_stat1.metric("Mínimo", f"{prefix}{val_min:,.2f}")
    col_stat2.metric("Máximo", f"{prefix}{val_max:,.2f}")
    col_stat3.metric("Média", f"{prefix}{val_mean:,.2f}")
    col_stat4.metric("Mediana", f"{prefix}{val_median:,.2f}")
    col_stat5.metric("Desvio Padrão", f"{prefix}{val_std:,.2f}")

st.markdown("---")

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Vendas por Categoria")
    if 'Line of Product' in df.columns and 'Sales' in df.columns:
        df_cat = df.groupby('Line of Product')['Sales'].sum().reset_index()
        fig_cat = px.bar(df_cat, x='Line of Product', y='Sales', text_auto='.2s', color='Line of Product')
        st.plotly_chart(fig_cat, use_container_width=True)

with col_g2:
    st.subheader("Evolução de Vendas Mensais")
    if 'Date' in df.columns and 'Sales' in df.columns:
        df_date = df.set_index('Date').resample('ME')['Sales'].sum().reset_index()
        fig_date = px.line(df_date, x='Date', y='Sales', markers=True)
        st.plotly_chart(fig_date, use_container_width=True)

st.subheader("Relação entre Quantidade e Valor de Vendas (Dispersão)")
if 'Quantity' in df.columns and 'Sales' in df.columns:
    fig_scatter = px.scatter(
        df, 
        x='Quantity', 
        y='Sales', 
        color='Line of Product', 
        hover_data=['Name', 'Date'],
        title="Dispersão: Quantidade de Itens vs. Valor Total"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.subheader("📋 Visualização dos Dados Carregados")
st.dataframe(df, use_container_width=True)