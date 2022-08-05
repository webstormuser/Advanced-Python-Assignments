import mysql.connector as conn
import pandas as pd


def createConnection():
    try:
        mydb = conn.connect(host='localhost', user='Ashwini', passwd='suhan10',
                            use_pure=True, auth_plugin='mysql_native_password')
        cursor = mydb.cursor()
        print('Connected Successfully')
    except Exception as e:
        print('Error occurred connecting to database', e)
    return mydb


conn = createConnection()

from sqlalchemy import create_engine


my_conn = create_engine("mysql+mysqldb://Ashwini:suhan10@localhost/sameer25")

data = [['Ashwini', 'Sujata', 'Abhishek', 'Sameer'], [31, 29, 21, 31], ['Jalgaon', 'Mp', 'CD', 'JL']]
df = pd.DataFrame(data)
print(df)

df.to_sql(con=my_conn, name='Mytable', if_exists='append')
