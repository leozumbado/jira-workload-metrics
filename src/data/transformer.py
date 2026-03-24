import pandas as pd
from src.data.loader import load_all_csv
from datetime import datetime, timedelta

def classify_tickets_by_week(df: pd.DataFrame) -> pd.DataFrame: #Función que define las semanas y clasifica los tickets dependiendo de la fecha entre la semana actual y la semana siguiente.

    today = datetime.today()
    start_week_day = today - timedelta(days=today.weekday())
    end_week_day = start_week_day + timedelta(days=6)
    next_week_start_day = start_week_day + timedelta(days=7)
    next_week_end_day = next_week_start_day + timedelta(days=6)

    df["week_category"] = "Later"

    df.loc[
        (df['Due date'] >= start_week_day) &
        (df['Due date'] <= end_week_day), 
        'week_category'
        ] = "This Week"
    
    df.loc[
        (df['Due date'] >= next_week_start_day) &
        (df['Due date'] <= next_week_end_day), 
        'week_category'
        ] = "Next Week"
    
    return df


def classify_tickets_by_labels(df: pd.DataFrame) -> pd.DataFrame: #Función que modifica los labels de los tickets, se elimina 'c-' ya que solo necesitamos las iniciales del Producer en el label.

    df['Labels'] = df['Labels'].str.replace('c-', '')
    
    return df

def filter_open_tickets(df: pd.DataFrame) -> pd.DataFrame: #Función que filtra y solo devuelve un DataFrame de los tickets que están abiertos.

    df = df[df["Status"] != 'Done']

    return df
