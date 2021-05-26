import pandas as pd
import basetool as bt
import os


def getCreateTableSql():
    return """CREATE TABLE IF NOT EXISTS businessstats (
                         area_id         INT PRIMARY KEY,
                         area_name      TEXT,
                         number_of_businesses       INT,
                         accommodation_and_food_services   INT,
                         retail_trade   INT,
                         agriculture_forestry_and_fishing INT,
                         health_care_and_social_assistance INT,
                         public_administration_and_safety INT,
                         transport_postal_and_warehousing INT
                   )"""


def getTableName():
    return 'businessstats'


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1500)  # 最大列数
    pd.set_option('display.max_rows', 100)  # 最大列数
    pd.set_option('display.width', 8000)

    # login to database
    db, conn = bt.pgconnect()

    data_path = '''C:\data'''
    print('data path is '+data_path)
    print('--------------------------------------')

    # read data
    business_areas = pd.read_csv(os.path.join(data_path, "BusinessStats.csv"))

    print(business_areas)

    print('create table '+getTableName())
    print('-------------------')
    conn.execute(getCreateTableSql())

    print('start inserting data')
    print('-------------------')
    business_areas.to_sql(getTableName(), con=conn, if_exists='replace')

    print(pd.read_sql_query('SELECT * FROM '+getTableName(), conn))