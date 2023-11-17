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
    print(df["difference"])
    mean_value = df[column].mean()
    print(mean_value)
    std_dev = df[column].std()
    print(std_dev)
    upper_limit = mean_value + multiplier * std_dev
    print(upper_limit)
    lower_limit = mean_value - multiplier * std_dev
    print(lower_limit)
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
            AVG(today) as {value_column},
            AVG(yesterday) as avg_yesterday,
            AVG(same_day_last_week) as avg_same_day_last_week
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

    result_df1 = average_sales_comparison(df1, value_column="avg_today")
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
                row["avg_today"],
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

    result_df2 = average_sales_comparison(df2, value_column="avg_today")
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
                row["avg_today"],
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
