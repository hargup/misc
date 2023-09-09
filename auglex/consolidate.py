import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

def consolidate_activities(activities, start_time, end_time):
    prompt = f"Summarize the following activities between {start_time} and {end_time}:\n{activities}"
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that can understand and summarize activities based on a list of descriptions."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        n=1,
        temperature=0.5
    )
    summary = response.choices[0].message['content'].strip()
    return summary

def read_data_from_db():
    conn = sqlite3.connect('screenshots.db')
    df = pd.read_sql_query("SELECT timestamp, activity FROM screenshots", conn)
    conn.close()
    return df

def process_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d-%H%M%S')
    df = df.set_index('timestamp').sort_index()
    df = df.resample('6T').agg({'activity': lambda x: x.tolist()})
    df['activity'] = df.apply(lambda row: 'idle' if len(row['activity']) < 3 else consolidate_activities(row['activity'], row.name - timedelta(minutes=6), row.name), axis=1)
    # Correct till here
    # I should anyput the aggregation activity in a seperate function
    # df = df.groupby((df['activity'] != df['activity'].shift()).cumsum()).agg({'activity': 'first', 'start_time': 'first', 'end_time': 'last'})
    return df

def main():
    data = read_data_from_db()
    result = process_data(data)
    print(result)

if __name__ == "__main__":
    main()