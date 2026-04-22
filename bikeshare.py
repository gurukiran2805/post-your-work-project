import pandas as pd

# load data
df = pd.read_csv('data/chicago.csv')

# convert Start Time to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# most common month
print("Most Common Month:", df['Start Time'].dt.month.mode()[0])

# most common day
print("Most Common Day:", df['Start Time'].dt.day_name().mode()[0])

# most common start station
print("Most Common Start Station:", df['Start Station'].mode()[0])

# trip duration stats
print("Total Trip Duration:", df['Trip Duration'].sum())
print("Average Trip Duration:", df['Trip Duration'].mean())

# user types
print("\nUser Types:\n", df['User Type'].value_counts())
