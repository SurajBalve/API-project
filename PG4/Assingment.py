import pandas as pd
import pg8000

conn = pg8000.connect(
    host= 'localhost',
    port=5432,
    database= 'postgres',
    user= 'postgres',
    password='root')



cursor= conn.cursor()
df = pd.read_csv('stu.csv')



table_name = 'Student'
Coloum = ' , '.join([f'{col} text' for col in df.columns])

Create_tablequery = f'Create Table if not exists {table_name}({Coloum})'
cursor.execute(Create_tablequery)


for _,row in df.iterrows():
    values = ','.join(str(val)for val in row.values)
    insertquery = f"insert into {table_name} values('{values}');"
    cursor.execute(insertquery)

print(table_name)
conn.commit()
cursor.close()
conn.close()
    
    