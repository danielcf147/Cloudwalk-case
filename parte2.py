# import pandas as pd


# def read_data(file_path):
#     return pd.read_csv(file_path)


# def traiter_valeurs_extremes_continues(df, variable):
#     q1 = df[variable].quantile(0.25)
#     q3 = df[variable].quantile(0.75)
#     IC_valeur_non_aberantes = [q1 - 2 * (q3 - q1), q3 + 2 * (q3 - q1)]
#     df.loc[df[variable] < IC_valeur_non_aberantes[0], variable] = df[variable].mean()
#     df.loc[df[variable] > IC_valeur_non_aberantes[1], variable] = df[variable].mean()
#     return df[variable]


# def main():
#     transactions1 = "transactions_1.csv"
#     transactions2 = "transactions_2.csv"

#     # df1 = read_data(transactions1)
#     df2 = read_data(transactions2)

#     # print("DataFrame 1:")
#     # print(df1)

#     variable_to_treat = "count"

#     # # Tratamento para DataFrame 1
#     # df1[variable_to_treat] = traiter_valeurs_extremes_continues(df1, variable_to_treat)

#     # print("\nDataFrame 1 após tratamento:")
#     # print(df1)

#     # print("\nDataFrame 2:")
#     # print(df2)

#     # Tratamento para DataFrame 2
#     df2[variable_to_treat] = traiter_valeurs_extremes_continues(df2, variable_to_treat)

#     print("\nDataFrame 2 após tratamento:")
#     print(df2)


# if __name__ == "__main__":
#     main()

# import pandas as pd

# # Leia o CSV
# transactions1 = "transactions_1.csv"
# transactions2 = "transactions_2.csv"
# df1 = pd.read_csv(transactions1)
# df2 = pd.read_csv(transactions2)
# # print(df1["time"])
# # df = pd.read_csv(file_path, delimiter="\t")  # Ajuste o delimitador conforme necessário

# # Se a coluna 'time' estiver no formato "00h 00", ajuste o formato
# df1["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")
# df2["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")

# # Certifique-se de que a coluna 'time' está correta
# if "time" not in df1.columns:
#     raise ValueError(
#         "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#     )
# if "time" not in df2.columns:
#     raise ValueError(
#         "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#     )

# # Crie uma coluna 'hour' para representar a hora
# df1["hour"] = df1["time"].dt.hour
# df2["hour"] = df2["time"].dt.hour

# # Filtrar as compras aprovadas, negadas e reembolsadas
# denied_df1 = df1[df1["status"] == "denied"]
# reversed_df1 = df1[df1["status"] == "reversed"]
# failed_df1 = df1[df1["status"] == "failed"]

# # Calcular a média por hora
# average_denied_by_hour1 = denied_df1.groupby("hour")["f0_"].mean()
# average_reversed_by_hour1 = reversed_df1.groupby("hour")["f0_"].mean()
# average_failed_by_hour1 = failed_df1.groupby("hour")["f0_"].mean()

# # Exibir os resultados
# print("Média de compras aprovadas por hora:")
# print(average_denied_by_hour1)

# print("\nMédia de compras negadas por hora:")
# print(average_reversed_by_hour1)

# print("\nMédia de compras reembolsadas por hora:")
# print(average_failed_by_hour1)


# # Filtrar as compras aprovadas, negadas e reembolsadas
# denied_df2 = df2[df2["status"] == "denied"]
# reversed_df2 = df2[df2["status"] == "reversed"]
# failed_df2 = df2[df2["status"] == "failed"]

# # Calcular a média por hora
# average_denied_by_hour2 = denied_df2.groupby("hour")["count"].mean()
# average_reversed_by_hour2 = reversed_df2.groupby("hour")["count"].mean()
# average_failed_by_hour2 = failed_df2.groupby("hour")["count"].mean()

# # Exibir os resultados
# print("Média de compras aprovadas por hora:")
# print(average_denied_by_hour2)

# print("\nMédia de compras negadas por hora:")
# print(average_reversed_by_hour2)

# print("\nMédia de compras reembolsadas por hora:")
# print(average_failed_by_hour2)

# import pandas as pd
# import matplotlib.pyplot as plt


# def calculate_anomalies_limits(df, column, multiplier=2):
#     mean_value = df[column].mean()
#     std_dev = df[column].std()
#     upper_limit = mean_value + multiplier * std_dev
#     lower_limit = mean_value - multiplier * std_dev
#     anomalies = df[(df[column] > upper_limit) | (df[column] < lower_limit)]
#     return anomalies, upper_limit, lower_limit


# def plot_anomalies_limits(df, column, multiplier=2):
#     anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
#         df, column, multiplier
#     )

#     # Plote a série temporal e destaque anomalias
#     plt.figure(figsize=(10, 6))
#     plt.plot(df.index, df[column], label=column)
#     plt.scatter(anomalies.index, anomalies[column], color="red", label="Anomalias")
#     plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
#     plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
#     plt.xlabel("Índice")
#     plt.ylabel(column)
#     plt.title(f"Anomalias para '{column}' com Limites Superior e Inferior")
#     plt.legend()
#     plt.show()


# def calculate_and_plot_anomalies(df, status_column, value_column, multiplier=2):
#     status_df = df[df["status"] == status_column]
#     anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
#         status_df, value_column, multiplier
#     )
#     print(anomalies)

#     # Plote a série temporal e destaque anomalias
#     plt.figure(figsize=(10, 6))
#     plt.plot(
#         status_df["hour"],
#         status_df[value_column],
#         label=f"{status_column} - {value_column}",
#     )
#     plt.scatter(
#         anomalies["hour"], anomalies[value_column], color="red", label="Anomalias"
#     )
#     plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
#     plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
#     plt.xlabel("Hora")
#     plt.ylabel(value_column)
#     plt.title(
#         f"Anomalias para '{status_column}' - '{value_column}' com Limites Superior e Inferior"
#     )
#     plt.legend()
#     plt.show()


# def main():
#     # Leia o CSV
#     transactions1 = "transactions_1.csv"
#     transactions2 = "transactions_2.csv"
#     df1 = pd.read_csv(transactions1)
#     df2 = pd.read_csv(transactions2)

#     # Se a coluna 'time' estiver no formato "00h 00", ajuste o formato
#     df1["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")
#     df2["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")

#     # Certifique-se de que a coluna 'time' está correta
#     if "time" not in df1.columns:
#         raise ValueError(
#             "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#         )
#     if "time" not in df2.columns:
#         raise ValueError(
#             "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#         )

#     # Crie uma coluna 'hour' para representar a hora
#     df1["hour"] = df1["time"].dt.hour
#     df2["hour"] = df2["time"].dt.hour

#     # Calcule e plote anomalias para df1
#     calculate_and_plot_anomalies(df1, "denied", "f0_")
#     calculate_and_plot_anomalies(df1, "reversed", "f0_")
#     calculate_and_plot_anomalies(df1, "failed", "f0_")

#     # Calcule e plote anomalias para df2
#     calculate_and_plot_anomalies(df2, "denied", "count")
#     calculate_and_plot_anomalies(df2, "reversed", "count")
#     calculate_and_plot_anomalies(df2, "failed", "count")


# if __name__ == "__main__":
#     main()

# import pandas as pd
# import matplotlib.pyplot as plt


# def calculate_anomalies_limits(df, column, multiplier=1.5):
#     mean_value = df[column].mean()
#     std_dev = df[column].std()
#     upper_limit = mean_value + multiplier * std_dev
#     lower_limit = mean_value - multiplier * std_dev
#     anomalies = df[(df[column] > upper_limit) | (df[column] < lower_limit)]
#     return anomalies, upper_limit, lower_limit


# def plot_anomalies_limits(df, column, multiplier=2):
#     anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
#         df, column, multiplier
#     )

#     # Plote a série temporal e destaque anomalias
#     plt.figure(figsize=(10, 6))
#     plt.scatter(df.index, df[column], label=column, color="blue", alpha=0.7)
#     plt.scatter(anomalies.index, anomalies[column], color="red", label="Anomalias")
#     plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
#     plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
#     plt.xlabel("Índice")
#     plt.ylabel(column)
#     plt.title(f"Anomalias para '{column}' com Limites Superior e Inferior")
#     plt.legend()
#     plt.show()


# def calculate_and_plot_anomalies(df, status_column, value_column, multiplier=2):
#     status_df = df[df["status"] == status_column]
#     anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
#         status_df, value_column, multiplier
#     )
#     print(anomalies)

#     # Plote a série temporal e destaque anomalias
#     plt.figure(figsize=(10, 6))
#     plt.scatter(
#         status_df["hour"],
#         status_df[value_column],
#         label=f"{status_column} - {value_column}",
#         color="blue",
#         alpha=0.7,
#     )
#     plt.scatter(
#         anomalies["hour"], anomalies[value_column], color="red", label="Anomalias"
#     )
#     plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
#     plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
#     plt.xticks(range(0, 24))  # Definindo os ticks do eixo X para 0-23
#     plt.xlabel("Hora")
#     plt.ylabel(value_column)
#     plt.title(
#         f"Anomalias para '{status_column}' - '{value_column}' com Limites Superior e Inferior"
#     )
#     plt.legend()
#     plt.show()


# def main(transaction):
#     # Leia o CSV
#     transactions1 = "transactions_1.csv"
#     transactions2 = "transactions_2.csv"
#     df1 = pd.read_csv(transactions1)
#     df2 = pd.read_csv(transactions2)

#     # Se a coluna 'time' estiver no formato "00h 00", ajusta o formato
#     df1["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")
#     df2["time"] = pd.to_datetime(df1["time"], format="%Hh %M", errors="coerce")

#     # Certificando que a coluna 'time' está correta
#     if "time" not in df1.columns:
#         raise ValueError(
#             "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#         )
#     if "time" not in df2.columns:
#         raise ValueError(
#             "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#         )

#     # Criando uma coluna 'hour' para representar a hora
#     df1["hour"] = df1["time"].dt.hour
#     df2["hour"] = df2["time"].dt.hour

#     # Calcule e plote anomalias para df1
#     calculate_and_plot_anomalies(df1, "denied", "f0_")
#     calculate_and_plot_anomalies(df1, "reversed", "f0_")
#     calculate_and_plot_anomalies(df1, "failed", "f0_")

#     # Calcule e plote anomalias para df2
#     calculate_and_plot_anomalies(df2, "denied", "count")
#     calculate_and_plot_anomalies(df2, "reversed", "count")
#     calculate_and_plot_anomalies(df2, "failed", "count")


# if __name__ == "__main__":
#     main()


import pandas as pd
import matplotlib.pyplot as plt
from alert import email_alert
import io
import base64


def calculate_anomalies_limits(df, column, multiplier=1.5):
    mean_value = df[column].mean()
    std_dev = df[column].std()
    upper_limit = mean_value + multiplier * std_dev
    lower_limit = mean_value - multiplier * std_dev
    anomalies = df[(df[column] > upper_limit) | (df[column] < lower_limit)]
    return anomalies, upper_limit, lower_limit


def plot_anomalies_limits(df, column, multiplier=2):
    anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
        df, column, multiplier
    )

    # Plote a série temporal e destaque anomalias
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df[column], label=column, color="blue", alpha=0.7)
    plt.scatter(anomalies.index, anomalies[column], color="red", label="Anomalias")
    plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
    plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
    plt.xlabel("Índice")
    plt.ylabel(column)
    plt.title(f"Anomalias para '{column}' com Limites Superior e Inferior")
    plt.legend()
    plt.show()


def calculate_and_plot_anomalies(df, status_column, value_column, multiplier=2):
    status_df = df[df["status"] == status_column]
    anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
        status_df, value_column, multiplier
    )
    print(anomalies)

    # Plote a série temporal e destaque anomalias
    plt.figure(figsize=(10, 6))
    plt.scatter(
        status_df["hour"],
        status_df[value_column],
        label=f"{status_column} - {value_column}",
        color="blue",
        alpha=0.7,
    )
    plt.scatter(
        anomalies["hour"], anomalies[value_column], color="red", label="Anomalias"
    )
    plt.axhline(y=upper_limit, color="r", linestyle="--", label="Limite Superior")
    plt.axhline(y=lower_limit, color="r", linestyle="--", label="Limite Inferior")
    plt.xticks(range(0, 24))  # Definindo os ticks do eixo X para 0-23
    plt.xlabel("Hora")
    plt.ylabel(value_column)
    plt.title(
        f"Anomalias para '{status_column}' - '{value_column}' com Limites Superior e Inferior"
    )
    plt.legend()
    plt.show()
    return anomalies


# def main(transaction_file):
#     # Leia o CSV
#     df = pd.read_csv(transaction_file)

#     # Se a coluna 'time' estiver no formato "00h 00", ajusta o formato
#     df["time"] = pd.to_datetime(df["time"], format="%Hh %M", errors="coerce")

#     # Certificando que a coluna 'time' está correta
#     if "time" not in df.columns:
#         raise ValueError(
#             "O DataFrame não possui uma coluna chamada 'time'. Verifique o formato do seu arquivo CSV."
#         )

#     # Criando uma coluna 'hour' para representar a hora
#     df["hour"] = df["time"].dt.hour

#     # Verificando se a coluna 'f0_' está presente
#     if "f0_" in df.columns:
#         # Processamento semelhante a df1
#         calculate_and_plot_anomalies(df, "denied", "f0_")
#         calculate_and_plot_anomalies(df, "reversed", "f0_")
#         calculate_and_plot_anomalies(df, "failed", "f0_")
#     else:
#         # Processamento semelhante a df2
#         calculate_and_plot_anomalies(df, "denied", "count")
#         calculate_and_plot_anomalies(df, "reversed", "count")
#         calculate_and_plot_anomalies(df, "failed", "count")
#     email_alert('report', )


# def save_plot_to_image(df, status_column, value_column, multiplier=2):
#     anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
#         df, value_column, multiplier
#     )

#     plt.figure(figsize=(10, 6))
#     plt.scatter(
#         df["hour"],
#         df[value_column],
#         label=f"{status_column} - {value_column}",
#         color="blue",
#         alpha=0.7,
#     )
#     plt.scatter(
#         anomalies["hour"], anomalies[value_column], color="red", label="Anomalies"
#     )
#     plt.axhline(y=upper_limit, color="r", linestyle="--", label="Upper Limit")
#     plt.axhline(y=lower_limit, color="r", linestyle="--", label="Lower Limit")
#     plt.xticks(range(0, 24))
#     plt.xlabel("Hour")
#     plt.ylabel(value_column)
#     plt.title(
#         f"Anomalies for '{status_column}' - '{value_column}' with Upper and Lower Limits"
#     )
#     plt.legend()

#     # Save the plot to an image file
#     image_path = f"{status_column}_{value_column}_plot.png"
#     plt.savefig(image_path, format="png")
#     plt.close()

#     return image_path


def save_plot_to_image(df, status_column, value_column, multiplier=2):
    anomalies, upper_limit, lower_limit = calculate_anomalies_limits(
        df, value_column, multiplier
    )

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["hour"],
        df[value_column],
        label=f"{status_column} - {value_column}",
        color="blue",
        alpha=0.7,
    )
    plt.scatter(
        anomalies["hour"], anomalies[value_column], color="red", label="Anomalies"
    )
    plt.axhline(y=upper_limit, color="r", linestyle="--", label="Upper Limit")
    plt.axhline(y=lower_limit, color="r", linestyle="--", label="Lower Limit")
    plt.xticks(range(0, 24))
    plt.xlabel("Hour")
    plt.ylabel(value_column)
    plt.title(
        f"Anomalies for '{status_column}' - '{value_column}' with Upper and Lower Limits"
    )
    plt.legend()

    # Save the plot to an image file
    image_path = f"{status_column}_{value_column}_plot.png"
    plt.savefig(image_path, format="png")
    plt.close()

    return image_path


# def main(transaction_file):
#     df = pd.read_csv(transaction_file)

#     if "time" not in df.columns:
#         raise ValueError(
#             "The DataFrame does not have a column named 'time'. Check the format of your CSV file."
#         )

#     df["time"] = pd.to_datetime(df["time"], format="%Hh %M", errors="coerce")
#     df["hour"] = df["time"].dt.hour

#     # Prepare email content
#     anomalies_data = "\n\n".join(
#         [
#             f"Anomalies for {status_column}:\n{calculate_and_plot_anomalies(df, status_column, 'f0_')}"
#             for status_column in ["denied", "reversed", "failed"]
#         ]
#     )
#     email_body = f"Anomalies Data:{anomalies_data}\n\n"

#     # Collect image paths
#     image_paths = []
#     for status_column in ["denied", "reversed", "failed"]:
#         image_path = save_plot_to_image(
#             df[df["status"] == status_column], status_column, "f0_"
#         )
#         # email_body += f"\n![{status_column}_Plot]({image_path})"
#         image_paths.append(image_path)

#     # Send the email with anomalies data and plots
#     email_alert("Anomaly Report", email_body, "danielcf.vix@hotmail.com", image_paths)


# def main(transaction_file):
#     df = pd.read_csv(transaction_file)

#     if "time" not in df.columns:
#         raise ValueError(
#             "The DataFrame does not have a column named 'time'. Check the format of your CSV file."
#         )

#     df["time"] = pd.to_datetime(df["time"], format="%Hh %M", errors="coerce")
#     df["hour"] = df["time"].dt.hour

#     # Prepare email content
#     anomalies_data = "\n\n".join(
#         [
#             f"Anomalies for {status_column}:\n{calculate_and_plot_anomalies(df, status_column, 'f0_' if 'f0_' in df.columns else 'count')}"
#             for status_column in ["denied", "reversed", "failed"]
#         ]
#     )
#     email_body = f"Anomalies Data:{anomalies_data}\n\n"

#     # Collect image paths
#     image_paths = []
#     for status_column in ["denied", "reversed", "failed"]:
#         column_to_use = "f0_" if "f0_" in df.columns else "count"
#         image_path = save_plot_to_image(
#             df[df["status"] == status_column], status_column, column_to_use
#         )
#         image_paths.append(image_path)

#     # Send the email with anomalies data and plots
#     email_alert("Anomaly Report", email_body, "danielcf147@gmail.com", image_paths)


def main(transaction_file):
    df = pd.read_csv(transaction_file)

    if "time" not in df.columns:
        raise ValueError(
            "The DataFrame does not have a column named 'time'. Check the format of your CSV file."
        )

    df["time"] = pd.to_datetime(df["time"], format="%Hh %M", errors="coerce")
    df["hour"] = df["time"].dt.hour

    # Prepare email content
    anomalies_data = "\n\n".join(
        [
            f"Anomalies for {status_column}:\n{calculate_and_plot_anomalies(df, status_column, 'f0_' if 'f0_' in df.columns else 'count')}"
            for status_column in ["denied", "reversed", "failed"]
        ]
    )
    email_body = f"Anomalies Data:{anomalies_data}\n\n"

    # Collect image paths
    image_paths = []
    for status_column in ["denied", "reversed", "failed"]:
        column_to_use = "f0_" if "f0_" in df.columns else "count"
        image_path = f"{status_column}_{column_to_use}_plot.png"
        image_paths.append(image_path)

    # Send the email with anomalies data and plots
    email_alert("Anomaly Report", email_body, "danielcf147@gmail.com", image_paths)

    # Delete the images after sending the email
    for image_path in image_paths:
        os.remove(image_path)


if __name__ == "__main__":
    main()
