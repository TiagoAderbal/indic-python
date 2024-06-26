import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.write("Indicadores Contábeis")

wp = pd.read_excel("WP - Fictício - 2022.xlsx", sheet_name="WP 2022", usecols=[4,5,7])
wp = wp.drop(range(4))

wp = wp.rename(columns={"Unnamed: 4": "Descrição", "Unnamed: 5": "2022", "Unnamed: 7":"2023"})

atv_circ = wp[wp["Descrição"].str.contains("ATIVO CIRCULANTE", na=False, case=False)]
psv_circ = wp[wp["Descrição"].str.contains("PASSIVO CIRCULANTE", na=False, case=False)]
estoq = wp[wp["Descrição"].str.contains("ESTOQUES", na=False, case=False)]
dispon = wp[wp["Descrição"].str.contains("DISPONIVEL", na=False, case=False)]
psv_ncirc = wp[wp["Descrição"].str.contains("PASSIVO NAO CIRCULANTE", na=False, case=False)]

atv_circ_2022 = atv_circ["2022"].iloc[0]
psv_circ_2022 = psv_circ["2022"].iloc[0]
estoq_2022 = estoq["2022"].iloc[0]
dispon_2022 = dispon["2022"].iloc[0]
psv_ncirc_2022 = psv_ncirc["2022"].iloc[0]

atv_circ_2023 = atv_circ["2023"].iloc[0]
psv_circ_2023 = psv_circ["2023"].iloc[0]
estoq_2023 = estoq["2023"].iloc[0]
dispon_2023 = dispon["2023"].iloc[0]
psv_ncirc_2023 = psv_ncirc["2023"].iloc[0]

data = { "Ano": ["2022", "2023"],
         "AC": [atv_circ_2022, atv_circ_2023],
         "PC": [psv_circ_2022, psv_circ_2023],
         "PNC": [psv_ncirc_2022, psv_ncirc_2023],
         "Estoques": [estoq_2022, estoq_2023],
         "Disponivel": [dispon_2022, dispon_2023]}

ind = pd.DataFrame(data)

ind["LC"] = ind["AC"] / ind["PC"]
ind["LS"] = (ind["AC"] - ind["Estoques"]) / ind["PC"]
ind["LI"] = ind["Disponivel"] / ind["PC"]
ind["CCL"] = ind["AC"] - ind["PC"]
ind["CE"] = (ind["PC"] / (ind["PC"] + ind["PNC"])) * 100

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

graf_liq_cor = px.bar(ind, x="Ano", y="LC", title="Liquidez Corrente")
graf_liq_sec = px.bar(ind, x="Ano", y="LS", title="Liquidez Seca")
graf_liq_ime = px.bar(ind, x="Ano", y="LI", title="Liquidez Imediata")
graf_cap_circ = px.bar(ind, x="Ano", y="CCL", title="Capital Circulante Líquido")
graf_comp_end = px.bar(ind, x="Ano", y="CE", title="Composição do Endividamento")


col1.plotly_chart(graf_liq_cor)
col2.plotly_chart(graf_liq_sec)
col3.plotly_chart(graf_liq_ime)
col4.plotly_chart(graf_cap_circ)
col5.plotly_chart(graf_comp_end)