import pandas as pd
import matplotlib.pyplot as plt


file_path = 'data.csv'
data = pd.read_csv(file_path)

#clean
data.columns = data.columns.str.strip()
data['Sales Dollars'] = data['Sales Dollars'].replace({'\$': '', ',': ''}, regex=True).astype(float)

#filter by state
nc_data = data[data['State'] == 'North Carolina']

#the total sales for each brand in North Carolina and convert to millions of dollars
total_nc = nc_data.groupby('Brand')['Sales Dollars'].sum().sort_values(ascending=False) / 1e6

#plot 
plt.figure(figsize=(12, 8))
total_nc.plot(kind='bar', color='#253846')
plt.title('A&F Total Sales by Brand in North Carolina in 2017 April-August (in Millions of Dollars)', fontsize=14)
plt.ylabel('Sales in Millions of Dollars', fontsize=12)
plt.xlabel('Brand', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
