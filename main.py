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

# import pandas as pd
# import matplotlib.pyplot as plt
# from pandasql import sqldf

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

# # Definindo os limites para identificar as anomalias no DataFrame 1
# media1 = df1["difference"].mean()
# desvio_padrao1 = df1["difference"].std()
# limite_superior1 = media1 + 1.5 * desvio_padrao1
# limite_inferior1 = media1 - 1.5 * desvio_padrao1

# anomaliasFull1 = df1[
#     (df1["difference"] > limite_superior1) | (df1["difference"] < limite_inferior1)
# ]
# print(anomaliasFull1)
# # Filtrar anomalias no DataFrame 1
# df1["anomaly"] = (df1["difference"] > limite_superior1) | (
#     df1["difference"] < limite_inferior1
# )
# # print(df1["anomaly"])
# # Adicionar limites superiores e inferiores
# plt.axhline(y=limite_superior1, color="r", linestyle="--", label="Limite Superior")
# plt.axhline(y=limite_inferior1, color="r", linestyle="--", label="Limite Inferior")

# # Adicionar bolinhas para cada valor
# plt.scatter(
#     df1[df1["anomaly"] == False].index,
#     df1[df1["anomaly"] == False]["difference"],
#     color="blue",
#     label="Normal",
# )
# plt.scatter(
#     df1[df1["anomaly"] == True].index,
#     df1[df1["anomaly"] == True]["difference"],
#     color="red",
#     label="Anomalia",
# )

# # Adicionar números de anomalias
# for index, row in df1[df1["anomaly"] == True].iterrows():
#     plt.annotate(int(row["difference"]), (index, row["difference"]))

# # Adicionar rótulos e legenda
# plt.xlabel("Índice")
# plt.ylabel("Diferença")
# plt.title("Limites Superior e Inferior com Anomalias - DataFrame 1")
# plt.legend()
# plt.show()

# # Criar uma coluna 'difference' para armazenar a diferença entre 'today' e 'same_day_last_week'
# df2["difference"] = df2["today"] - df2["same_day_last_week"]
# df2["filtered_difference"] = df2["difference"].apply(lambda x: x if x >= 0 else None)
# df2 = df2.dropna(subset=["filtered_difference"])
# df2 = df2.drop(columns=["filtered_difference"])

# # Definindo os limites para identificar as anomalias no DataFrame 2
# media2 = df2["difference"].mean()
# desvio_padrao2 = df2["difference"].std()
# limite_superior2 = media2 + 1.5 * desvio_padrao2
# limite_inferior2 = media2 - 1.5 * desvio_padrao2

# anomaliasFull2 = df2[
#     (df2["difference"] > limite_superior2) | (df2["difference"] < limite_inferior2)
# ]
# print(anomaliasFull2)
# # Filtrar anomalias no DataFrame 2
# df2["anomaly"] = (df2["difference"] > limite_superior2) | (
#     df2["difference"] < limite_inferior2
# )
# # print(df2["anomaly"])
# # Adicionar limites superiores e inferiores
# plt.axhline(y=limite_superior2, color="r", linestyle="--", label="Limite Superior")
# plt.axhline(y=limite_inferior2, color="r", linestyle="--", label="Limite Inferior")

# # Adicionar bolinhas para cada valor
# plt.scatter(
#     df2[df2["anomaly"] == False].index,
#     df2[df2["anomaly"] == False]["difference"],
#     color="blue",
#     label="Normal",
# )
# plt.scatter(
#     df2[df2["anomaly"] == True].index,
#     df2[df2["anomaly"] == True]["difference"],
#     color="red",
#     label="Anomalia",
# )

# # Adicionar números de anomalias
# for index, row in df2[df2["anomaly"] == True].iterrows():
#     plt.annotate(int(row["difference"]), (index, row["difference"]))

# # Adicionar rótulos e legenda
# plt.xlabel("Índice")
# plt.ylabel("Diferença")
# plt.title("Limites Superior e Inferior com Anomalias - DataFrame 2")
# plt.legend()
# plt.show()

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
# # plt.plot(result_df1["time"], result_df1["avg_yesterday"], label="Yesterday")
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
# # plt.plot(result_df2["time"], result_df2["avg_yesterday"], label="Yesterday")
# plt.plot(
#     result_df2["time"], result_df2["avg_same_day_last_week"], label="Same Day Last Week"
# )

# plt.xlabel("Time")
# plt.ylabel("Average Sales")
# plt.title("Average Sales Comparison - DataFrame 2")
# plt.legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# from pandasql import sqldf

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

# # Definindo os limites para identificar as anomalias no DataFrame 1
# media1 = df1["difference"].mean()
# desvio_padrao1 = df1["difference"].std()
# limite_superior1 = media1 + 1.5 * desvio_padrao1
# limite_inferior1 = media1 - 1.5 * desvio_padrao1

# anomaliasFull1 = df1[
#     (df1["difference"] > limite_superior1) | (df1["difference"] < limite_inferior1)
# ]
# print(anomaliasFull1)
# # Filtrar anomalias no DataFrame 1
# df1["anomaly"] = (df1["difference"] > limite_superior1) | (
#     df1["difference"] < limite_inferior1
# )
# # Adicionar limites superiores e inferiores
# plt.axhline(y=limite_superior1, color="r", linestyle="--", label="Limite Superior")
# plt.axhline(y=limite_inferior1, color="r", linestyle="--", label="Limite Inferior")

# # Adicionar bolinhas para cada valor
# plt.scatter(
#     df1[df1["anomaly"] == False].index,
#     df1[df1["anomaly"] == False]["difference"],
#     color="blue",
#     label="Normal",
# )
# plt.scatter(
#     df1[df1["anomaly"] == True].index,
#     df1[df1["anomaly"] == True]["difference"],
#     color="red",
#     label="Anomalia",
# )

# # Adicionar números de anomalias
# for index, row in df1[df1["anomaly"] == True].iterrows():
#     plt.annotate(int(row["difference"]), (index, row["difference"]))

# # Adicionar rótulos e legenda
# plt.xlabel("Índice")
# plt.ylabel("Diferença")
# plt.title("Limites Superior e Inferior com Anomalias - DataFrame 1")
# plt.legend()
# plt.show()

# # Criar uma coluna 'difference' para armazenar a diferença entre 'today' e 'same_day_last_week'
# df2["difference"] = df2["today"] - df2["same_day_last_week"]
# df2["filtered_difference"] = df2["difference"].apply(lambda x: x if x >= 0 else None)
# df2 = df2.dropna(subset=["filtered_difference"])
# df2 = df2.drop(columns=["filtered_difference"])

# # Definindo os limites para identificar as anomalias no DataFrame 2
# media2 = df2["difference"].mean()
# desvio_padrao2 = df2["difference"].std()
# limite_superior2 = media2 + 1.5 * desvio_padrao2
# limite_inferior2 = media2 - 1.5 * desvio_padrao2

# anomaliasFull2 = df2[
#     (df2["difference"] > limite_superior2) | (df2["difference"] < limite_inferior2)
# ]
# print(anomaliasFull2)
# # Filtrar anomalias no DataFrame 2
# df2["anomaly"] = (df2["difference"] > limite_superior2) | (
#     df2["difference"] < limite_inferior2
# )
# # Adicionar limites superiores e inferiores
# plt.axhline(y=limite_superior2, color="r", linestyle="--", label="Limite Superior")
# plt.axhline(y=limite_inferior2, color="r", linestyle="--", label="Limite Inferior")

# # Adicionar bolinhas para cada valor
# plt.scatter(
#     df2[df2["anomaly"] == False].index,
#     df2[df2["anomaly"] == False]["difference"],
#     color="blue",
#     label="Normal",
# )
# plt.scatter(
#     df2[df2["anomaly"] == True].index,
#     df2[df2["anomaly"] == True]["difference"],
#     color="red",
#     label="Anomalia",
# )

# # Adicionar números de anomalias
# for index, row in df2[df2["anomaly"] == True].iterrows():
#     plt.annotate(int(row["difference"]), (index, row["difference"]))

# # Adicionar rótulos e legenda
# plt.xlabel("Índice")
# plt.ylabel("Diferença")
# plt.title("Limites Superior e Inferior com Anomalias - DataFrame 2")
# plt.legend()
# plt.show()

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
# # plt.plot(result_df1["time"], result_df1["avg_yesterday"], label="Yesterday")
# plt.plot(
#     result_df1["time"], result_df1["avg_same_day_last_week"], label="Same Day Last Week"
# )

# # Adicionar bolinhas vermelhas nos horários com anomalias no gráfico do SQL
# for index, row in result_df1.iterrows():
#     if df1.loc[df1["anomaly"] == True, "time"].str.contains(row["time"]).any():
#         plt.scatter(
#             index,
#             row["avg_same_day_last_week"],
#             color="red",
#             label="Anomalia",
#             zorder=5,
#         )

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
# # plt.plot(result_df2["time"], result_df2["avg_yesterday"], label="Yesterday")
# plt.plot(
#     result_df2["time"], result_df2["avg_same_day_last_week"], label="Same Day Last Week"
# )

# for index, row in result_df2.iterrows():
#     if df2.loc[df2["anomaly"] == True, "time"].str.contains(row["time"]).any():
#         plt.scatter(
#             index,
#             row["avg_same_day_last_week"],
#             color="red",
#             label="Anomalia",
#             zorder=5,
#         )

# plt.xlabel("Time")
# plt.ylabel("Average Sales")
# plt.title("Average Sales Comparison - DataFrame 2")
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf


def read_data(file_path):
    return pd.read_csv(file_path)


def preprocess_data(df):
    df["difference"] = df["today"] - df["same_day_last_week"]
    df["filtered_difference"] = df["difference"].apply(lambda x: x if x >= 0 else None)
    df = df.dropna(subset=["filtered_difference"])
    df = df.drop(columns=["filtered_difference"])
    return df


def detect_anomalies(df, column="difference", multiplier=1.5):
    mean_value = df[column].mean()
    std_dev = df[column].std()
    upper_limit = mean_value + multiplier * std_dev
    lower_limit = mean_value - multiplier * std_dev
    anomalies = df[(df[column] > upper_limit) | (df[column] < lower_limit)]
    return anomalies, upper_limit, lower_limit


def plot_anomalies(df, column="difference", upper_limit=None, lower_limit=None):
    plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
    plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
    plt.scatter(
        df[df["anomaly"] == False].index,
        df[df["anomaly"] == False][column],
        color="blue",
        label="Normal",
    )
    plt.scatter(
        df[df["anomaly"] == True].index,
        df[df["anomaly"] == True][column],
        color="red",
        label="Anomalia",
    )
    for index, row in df[df["anomaly"] == True].iterrows():
        plt.annotate(int(row[column]), (index, row[column]))


def average_sales_comparison(
    df, time_column="time", value_column="avg_same_day_last_week"
):
    query = f"""
        SELECT
            {time_column},
            AVG(today) as avg_today,
            AVG(yesterday) as avg_yesterday,
            AVG(same_day_last_week) as {value_column}
        FROM df
        GROUP BY {time_column}
    """
    return sqldf(query, locals())


def main():
    checkout1 = "checkout_1.csv"
    checkout2 = "checkout_2.csv"

    df1 = read_data(checkout1)
    df2 = read_data(checkout2)

    df1 = preprocess_data(df1)
    df2 = preprocess_data(df2)

    anomalies1, upper_limit1, lower_limit1 = detect_anomalies(df1)
    anomalies2, upper_limit2, lower_limit2 = detect_anomalies(df2)

    print(anomalies1)
    print(anomalies2)

    df1["anomaly"] = (df1["difference"] > upper_limit1) | (
        df1["difference"] < lower_limit1
    )
    df2["anomaly"] = (df2["difference"] > upper_limit2) | (
        df2["difference"] < lower_limit2
    )

    plt.figure(figsize=(12, 6))
    plot_anomalies(df1, upper_limit=upper_limit1, lower_limit=lower_limit1)
    plt.xlabel("Índice")
    plt.ylabel("Diferença")
    plt.title("Limites Superior e Inferior com Anomalias - DataFrame 1")
    plt.legend()
    plt.show()

    result_df1 = average_sales_comparison(df1)
    plt.figure(figsize=(12, 6))
    plt.plot(result_df1["time"], result_df1["avg_today"], label="Today")
    plt.plot(
        result_df1["time"],
        result_df1["avg_same_day_last_week"],
        label="Same Day Last Week",
    )

    for index, row in result_df1.iterrows():
        if df1.loc[df1["anomaly"] == True, "time"].str.contains(row["time"]).any():
            plt.scatter(
                index,
                row["avg_same_day_last_week"],
                color="red",
                label="Anomalia",
                zorder=5,
            )

    plt.xlabel("Time")
    plt.ylabel("Average Sales")
    plt.title("Average Sales Comparison - DataFrame 1")
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    plot_anomalies(df2, upper_limit=upper_limit2, lower_limit=lower_limit2)
    plt.xlabel("Índice")
    plt.ylabel("Diferença")
    plt.title("Limites Superior e Inferior com Anomalias - DataFrame 2")
    plt.legend()
    plt.show()

    result_df2 = average_sales_comparison(df2)
    plt.figure(figsize=(12, 6))
    plt.plot(result_df2["time"], result_df2["avg_today"], label="Today")
    plt.plot(
        result_df2["time"],
        result_df2["avg_same_day_last_week"],
        label="Same Day Last Week",
    )

    for index, row in result_df2.iterrows():
        if df2.loc[df2["anomaly"] == True, "time"].str.contains(row["time"]).any():
            plt.scatter(
                index,
                row["avg_same_day_last_week"],
                color="red",
                label="Anomalia",
                zorder=5,
            )

    plt.xlabel("Time")
    plt.ylabel("Average Sales")
    plt.title("Average Sales Comparison - DataFrame 2")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
