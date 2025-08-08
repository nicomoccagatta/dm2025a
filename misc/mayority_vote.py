import pandas as pd

# Leer los archivos
df1 = pd.read_csv("KA420_016.csv").rename(columns={"Predicted": "pred1"})
df2 = pd.read_csv("KA4070.csv").rename(columns={"Predicted": "pred2"})
df3 = pd.read_csv("KA95000001_s20_10000.csv").rename(columns={"Predicted": "pred3"})

# Unir por numero_de_cliente (outer para no perder ningún cliente)
merged = df1.merge(df2, on="numero_de_cliente", how="outer")
merged = merged.merge(df3, on="numero_de_cliente", how="outer")

# Reemplazar NaN por 0 (clientes que no fueron predichos en algún archivo)
merged.fillna(0, inplace=True)

# Aplicar majority vote: al menos 2 modelos deben predecir 1
merged["Predicted"] = ((merged["pred1"] + merged["pred2"] + merged["pred3"]) >= 2).astype(int)

# Crear el CSV final
final = merged[["numero_de_cliente", "Predicted"]]
final.to_csv("predicciones_majority_vote.csv", index=False)

print("✅ Archivo 'predicciones_majority_vote.csv' generado correctamente.")

