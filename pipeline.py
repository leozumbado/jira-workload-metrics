from src.data.loader import load_dataset
from src.data.transformer import(
    classify_tickets_by_week,
    classify_tickets_by_labels,
    filter_open_tickets
)
from src.metrics.workload import calculate_weekly_metrics


df = load_dataset('data/raw/sample_jira_tickets.csv')

df = filter_open_tickets(df)
df = classify_tickets_by_labels(df)
df = classify_tickets_by_week(df)

metrics = calculate_weekly_metrics(df)

print("Tickets This Week:", metrics["tickets_this_week"])
print("Tickets Next Week:", metrics["tickets_next_week"])
print("\nAverage Workload Per Producer:")
print(metrics["avg_workload_per_producer"])