import pandas as pd

# Leer tus tres archivos originales
df1 = pd.read_csv("KA420_016.csv")
df2 = pd.read_csv("KA4070.csv")
df3 = pd.read_csv("KA95000001_s20_10000.csv")

# Unirlos y aplicar OR lógico
combined_df = pd.concat([df1, df2, df3])
result = combined_df.groupby("numero_de_cliente", as_index=False).agg({"Predicted": "max"})

# Guardar resultado
result.to_csv("predicciones_mejoradas.csv", index=False)

