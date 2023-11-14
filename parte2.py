import pandas as pd
import matplotlib.pyplot as plt
from alert import email_alert
import os


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
        image_path = save_plot_to_image(
            df[df["status"] == status_column], status_column, column_to_use
        )
        image_paths.append(image_path)

    # Send the email with anomalies data and plots
    email_alert("Anomaly Report", email_body, "danielcf147@gmail.com", image_paths)

    # Delete the images after sending the email
    for image_path in image_paths:
        os.remove(image_path)


if __name__ == "__main__":
    main()
