import pandas as pd

import basetool
import basetool as bt


def get_tables(conn):
    return pd.read_sql_query('select * from pg_tables limit 10', conn)


def get_data_statisticalareas(conn):
    return pd.read_sql_query('select * from statisticalareas', conn)


def get_data_bussinessstats(conn):
    return pd.read_sql_query('select * from businessstats', conn)


def get_data_neighbourhoods(conn):
    return pd.read_sql_query('select * from neighbourhoods', conn)


def get_data_sa2(conn):
    return pd.read_sql_query('select * from sa2_2016_aust', conn)


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1500)  # 最大列数
    pd.set_option('display.max_rows', 100)  # 最大列数
    pd.set_option('display.width', 8000)

    # login to database
    db, conn = bt.pgconnect()

    # print all tables in the database
    print(get_tables(conn))

    print(get_data_statisticalareas(conn))
    print(get_data_neighbourhoods(conn))
    print(get_data_bussinessstats(conn))

    query = "SELECT COUNT(*) FROM sa2_2016_aust"
    query = "SELECT COUNT(*) FROM rfsnsw_bfpl"
    retval, retdf = basetool.pgquery(conn, query)
    print(retdf)
    # print(pd.read_sql_query('select * from rfsnsw_bfpl', conn))
