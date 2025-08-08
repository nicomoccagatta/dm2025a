import pandas as pd

# Leer los CSVs
ka9500 = pd.read_csv("KA95000001_s20_10000.csv").rename(columns={"Predicted": "pred3"})
ka420 = pd.read_csv("KA420_016.csv").rename(columns={"Predicted": "pred1"})
ka4070 = pd.read_csv("KA4070.csv").rename(columns={"Predicted": "pred2"})

# Unir los tres datasets por numero_de_cliente
merged = ka9500.merge(ka420, on="numero_de_cliente", how="left")
merged = merged.merge(ka4070, on="numero_de_cliente", how="left")

# Rellenar NaNs con 0 (clientes que no aparecen en algún archivo)
merged.fillna(0, inplace=True)

# Aplicar estrategia de consenso sobre los positivos de pred3
merged["Predicted"] = (
    (merged["pred3"] == 1) & ((merged["pred1"] == 1) | (merged["pred2"] == 1))
).astype(int)

# Guardar el resultado
final = merged[["numero_de_cliente", "Predicted"]]
final.to_csv("predicciones_filtradas_consenso.csv", index=False)

print("✅ Archivo 'predicciones_filtradas_consenso.csv' generado correctamente.")

