import pandas as pd
import basetool as bt
import os


def getCreateTableSql():
    return """CREATE TABLE IF NOT EXISTS statisticalareas (
                         area_id        INT PRIMARY KEY,
                         area_name      TEXT,
                         parent_area_id INT
                   )"""


def getTableName():
    return 'statisticalareas'


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1500)  # 最大列数
    pd.set_option('display.max_rows', 100)  # 最大列数
    pd.set_option('display.width', 8000)

    # login to database
    db, conn = bt.pgconnect()

    data_path = '''C:\data'''
    print('data path is ' + data_path)
    print('--------------------------------------')

    # read data
    neightbourhoods = pd.read_csv(os.path.join(data_path, "StatisticalAreas.csv"))

    print(neightbourhoods)

    print('create table ' + getTableName())
    print('-------------------')
    conn.execute(getCreateTableSql())

    print('start inserting data')
    print('-------------------')
    neightbourhoods.to_sql(getTableName(), con=conn, if_exists='replace')

    print(pd.read_sql_query('SELECT * FROM ' + getTableName(), conn))