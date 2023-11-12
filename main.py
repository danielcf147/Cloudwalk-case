# import pandas as pd
# import matplotlib.pyplot as plt


# # Supondo que você tenha lido os dados do CSV
# checkout1 = "checkout_1.csv"
# checkout2 = "checkout_2.csv"
# df1 = pd.read_csv(checkout1)
# df2 = pd.read_csv(checkout2)


# # Criar uma coluna 'difference' para armazenar a diferença entre 'today' e 'same_day_last_week'
# df1["difference"] = df1["today"] - df1["same_day_last_week"]

# df1["filtered_difference"] = df1["difference"].apply(lambda x: x if x >= 0 else None)
# df1 = df1.dropna(subset=["filtered_difference"])
# df1 = df1.drop(columns=["filtered_difference"])

# # print(df1["difference"])

# # Calcule a média e o desvio padrão da coluna
# media1 = df1["difference"].mean()
# desvio_padrao1 = df1["difference"].std()

# # print(media)
# # print(desvio_padrao)


# # Definindo os limites para identificar as anomalias
# limite_superior1 = media1 + 1.5 * desvio_padrao1
# limite_inferior1 = media1 - 1.5 * desvio_padrao1

# # print(limite_superior1)
# # print(limite_inferior1)


# anomalias1 = df1[
#     (df1["difference"] > limite_superior1) | (df1["difference"] < limite_inferior1)
# ]
# print(anomalias1)
# print("-----------------------------------------------------------------------")

# # plt.boxplot(df1["difference"])
# # plt.xlabel("Coluna")
# # plt.ylabel("Valor")

# # plt.title("Boxplot da Coluna Valor")

# # # Exiba o boxplot
# # plt.show()


# df2["difference"] = df2["today"] - df2["same_day_last_week"]

# df2["filtered_difference"] = df2["difference"].apply(lambda x: x if x >= 0 else None)
# df2 = df2.dropna(subset=["filtered_difference"])
# df2 = df2.drop(columns=["filtered_difference"])

# # print(df2["difference"])

# media2 = df2["difference"].mean()
# desvio_padrao2 = df2["difference"].std()

# limite_superior2 = media2 + 1.5 * desvio_padrao2
# limite_inferior2 = media2 - 1.5 * desvio_padrao2

# # print(limite_superior2)
# # print(limite_inferior2)

# # print(limite_superior1)
# # print(limite_inferior1)


# anomalias2 = df2[
#     (df2["difference"] > limite_superior2) | (df2["difference"] < limite_inferior2)
# ]

# print(anomalias2)
# # Exiba os resultados
# # print("Anomalias:")
# # print(anomalias)

# plt.boxplot(df2["difference"])
# plt.xlabel("Coluna")
# plt.ylabel("Valor")

# plt.title("Boxplot da Coluna Valor")

# # Exiba o boxplot
# # plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf

# Supondo que você tenha lido os dados do CSV
checkout1 = "checkout_1.csv"
checkout2 = "checkout_2.csv"
df1 = pd.read_csv(checkout1)
df2 = pd.read_csv(checkout2)

# Criar uma coluna 'difference' para armazenar a diferença entre 'today' e 'same_day_last_week'
df1["difference"] = df1["today"] - df1["same_day_last_week"]
df1["filtered_difference"] = df1["difference"].apply(lambda x: x if x >= 0 else None)
df1 = df1.dropna(subset=["filtered_difference"])
df1 = df1.drop(columns=["filtered_difference"])

# Definindo os limites para identificar as anomalias no DataFrame 1
media1 = df1["difference"].mean()
desvio_padrao1 = df1["difference"].std()
limite_superior1 = media1 + 1.5 * desvio_padrao1
limite_inferior1 = media1 - 1.5 * desvio_padrao1

anomaliasFull1 = df1[
    (df1["difference"] > limite_superior1) | (df1["difference"] < limite_inferior1)
]
print(anomaliasFull1)
# Filtrar anomalias no DataFrame 1
df1["anomaly"] = (df1["difference"] > limite_superior1) | (
    df1["difference"] < limite_inferior1
)
# print(df1["anomaly"])
# Adicionar limites superiores e inferiores
plt.axhline(y=limite_superior1, color="r", linestyle="--", label="Limite Superior")
plt.axhline(y=limite_inferior1, color="r", linestyle="--", label="Limite Inferior")

# Adicionar bolinhas para cada valor
plt.scatter(
    df1[df1["anomaly"] == False].index,
    df1[df1["anomaly"] == False]["difference"],
    color="blue",
    label="Normal",
)
plt.scatter(
    df1[df1["anomaly"] == True].index,
    df1[df1["anomaly"] == True]["difference"],
    color="red",
    label="Anomalia",
)

# Adicionar números de anomalias
for index, row in df1[df1["anomaly"] == True].iterrows():
    plt.annotate(int(row["difference"]), (index, row["difference"]))

# Adicionar rótulos e legenda
plt.xlabel("Índice")
plt.ylabel("Diferença")
plt.title("Limites Superior e Inferior com Anomalias - DataFrame 1")
plt.legend()
plt.show()

# Criar uma coluna 'difference' para armazenar a diferença entre 'today' e 'same_day_last_week'
df2["difference"] = df2["today"] - df2["same_day_last_week"]
df2["filtered_difference"] = df2["difference"].apply(lambda x: x if x >= 0 else None)
df2 = df2.dropna(subset=["filtered_difference"])
df2 = df2.drop(columns=["filtered_difference"])

# Definindo os limites para identificar as anomalias no DataFrame 2
media2 = df2["difference"].mean()
desvio_padrao2 = df2["difference"].std()
limite_superior2 = media2 + 1.5 * desvio_padrao2
limite_inferior2 = media2 - 1.5 * desvio_padrao2

anomaliasFull2 = df2[
    (df2["difference"] > limite_superior2) | (df2["difference"] < limite_inferior2)
]
print(anomaliasFull2)
# Filtrar anomalias no DataFrame 2
df2["anomaly"] = (df2["difference"] > limite_superior2) | (
    df2["difference"] < limite_inferior2
)
# print(df2["anomaly"])
# Adicionar limites superiores e inferiores
plt.axhline(y=limite_superior2, color="r", linestyle="--", label="Limite Superior")
plt.axhline(y=limite_inferior2, color="r", linestyle="--", label="Limite Inferior")

# Adicionar bolinhas para cada valor
plt.scatter(
    df2[df2["anomaly"] == False].index,
    df2[df2["anomaly"] == False]["difference"],
    color="blue",
    label="Normal",
)
plt.scatter(
    df2[df2["anomaly"] == True].index,
    df2[df2["anomaly"] == True]["difference"],
    color="red",
    label="Anomalia",
)

# Adicionar números de anomalias
for index, row in df2[df2["anomaly"] == True].iterrows():
    plt.annotate(int(row["difference"]), (index, row["difference"]))

# Adicionar rótulos e legenda
plt.xlabel("Índice")
plt.ylabel("Diferença")
plt.title("Limites Superior e Inferior com Anomalias - DataFrame 2")
plt.legend()
plt.show()

# Consulta SQL
pysqldf = lambda q: sqldf(q, globals())

# Consulta SQL para DataFrame 1
query_df1 = """
    SELECT
        time,
        AVG(today) as avg_today,
        AVG(yesterday) as avg_yesterday,
        AVG(same_day_last_week) as avg_same_day_last_week
    FROM df1
    GROUP BY time
"""

result_df1 = pysqldf(query_df1)

# Gráfico para DataFrame 1
plt.figure(figsize=(12, 6))
plt.plot(result_df1["time"], result_df1["avg_today"], label="Today")
# plt.plot(result_df1["time"], result_df1["avg_yesterday"], label="Yesterday")
plt.plot(
    result_df1["time"], result_df1["avg_same_day_last_week"], label="Same Day Last Week"
)

plt.xlabel("Time")
plt.ylabel("Average Sales")
plt.title("Average Sales Comparison - DataFrame 1")
plt.legend()
plt.show()

# Consulta SQL para DataFrame 2
query_df2 = """
    SELECT
        time,
        AVG(today) as avg_today,
        AVG(yesterday) as avg_yesterday,
        AVG(same_day_last_week) as avg_same_day_last_week
    FROM df2
    GROUP BY time
"""

result_df2 = pysqldf(query_df2)

# Gráfico para DataFrame 2
plt.figure(figsize=(12, 6))
plt.plot(result_df2["time"], result_df2["avg_today"], label="Today")
# plt.plot(result_df2["time"], result_df2["avg_yesterday"], label="Yesterday")
plt.plot(
    result_df2["time"], result_df2["avg_same_day_last_week"], label="Same Day Last Week"
)

plt.xlabel("Time")
plt.ylabel("Average Sales")
plt.title("Average Sales Comparison - DataFrame 2")
plt.legend()
plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# from pandasql import sqldf

# # Supondo que você tenha lido os dados do CSV
# checkout1 = "checkout_1.csv"
# checkout2 = "checkout_2.csv"
# df1 = pd.read_csv(checkout1)
# df2 = pd.read_csv(checkout2)

# # Consulta SQL
# pysqldf = lambda q: sqldf(q, globals())

# # Consulta SQL para DataFrame 1
# query_df1 = """
#     SELECT
#         time,
#         AVG(today) as avg_today,
#         AVG(yesterday) as avg_yesterday,
#         AVG(same_day_last_week) as avg_same_day_last_week
#     FROM df1
#     GROUP BY time
# """

# result_df1 = pysqldf(query_df1)

# # Gráfico para DataFrame 1
# plt.figure(figsize=(12, 6))
# plt.plot(result_df1["time"], result_df1["avg_today"], label="Today")
# plt.plot(result_df1["time"], result_df1["avg_yesterday"], label="Yesterday")
# plt.plot(
#     result_df1["time"], result_df1["avg_same_day_last_week"], label="Same Day Last Week"
# )

# plt.xlabel("Time")
# plt.ylabel("Average Sales")
# plt.title("Average Sales Comparison - DataFrame 1")
# plt.legend()
# plt.show()

# # Consulta SQL para DataFrame 2
# query_df2 = """
#     SELECT
#         time,
#         AVG(today) as avg_today,
#         AVG(yesterday) as avg_yesterday,
#         AVG(same_day_last_week) as avg_same_day_last_week
#     FROM df2
#     GROUP BY time
# """

# result_df2 = pysqldf(query_df2)

# # Gráfico para DataFrame 2
# plt.figure(figsize=(12, 6))
# plt.plot(result_df2["time"], result_df2["avg_today"], label="Today")
# plt.plot(result_df2["time"], result_df2["avg_yesterday"], label="Yesterday")
# plt.plot(
#     result_df2["time"], result_df2["avg_same_day_last_week"], label="Same Day Last Week"
# )

# plt.xlabel("Time")
# plt.ylabel("Average Sales")
# plt.title("Average Sales Comparison - DataFrame 2")
# plt.legend()
# plt.show()
