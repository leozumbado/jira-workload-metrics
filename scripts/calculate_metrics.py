import pandas as pd

def calculate_weekly_metrics(df: pd.DataFrame) -> dict:

    tickets_this_week = int((df["week_category"] == "This Week").sum())
    tickets_next_week = int((df["week_category"] == "Next Week").sum())

    weekly_workload = (
        df[df["week_category"].isin(["This Week", "Next Week"])]
        .groupby(["Labels", "week_category"])
        .size()
        .reset_index(name="tickets")
    )

    avg_workload = (
        weekly_workload.groupby("Labels")["tickets"]
        .mean()
        .round(2)
        .reset_index(name="avg_weekly_workload")
    )

    return {
        "tickets_this_week": tickets_this_week,
        "tickets_next_week": tickets_next_week,
        "avg_workload_per_producer": avg_workload
    }