from bloco_risco import mostrar_painel_risco, mostrar_alertas
print("SOC Transparencia iniciado")


from bloco_risco import calcular_risco

df = calcular_risco(df)

st.subheader("🚨 Alertas de risco")

alertas = df[df["risco"] != "Normal"]

st.dataframe(alertas[["_conta_ref","_valor_base","zscore","risco"]])
