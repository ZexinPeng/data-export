import geopandas as gpd
import os
import basetool

import pandas as pd
from shapely.geometry import Point, Polygon, MultiPolygon
from geoalchemy2 import Geometry, WKTElement

def create_wkt_point_element(geom,srid):
    return WKTElement(geom.wkt, srid)

def create_table_sql():
    return '''CREATE TABLE IF NOT EXISTS rfsnsw_bfpl (
                         category INT,
                         shape_leng FLOAT,
                         shape_area  NUMERIC,
                         location GEOMETRY(POINT,4326))'''

def get_table_name():
    return '''rfsnsw_bfpl'''

if __name__ == '__main__':
    pd.set_option('display.max_columns', 1500)  # 最大列数
    pd.set_option('display.max_rows', 100)  # 最大列数
    pd.set_option('display.width', 8000)

    # login to database
    db, conn = basetool.pgconnect()

    data_path = '''C:\data\RFSNSW_BFPL'''
    print('data path is '+data_path)
    srid = 4326

    # read data
    data = gpd.read_file( os.path.join(data_path, "RFSNSW_BFPL.shp") )

    data.rename(columns={'CATEGORY': 'category', 'SHAPE_LENG': 'shape_leng', 'SHAPE_AREA': 'shape_area'}, inplace=True)

    dataWkCpy = data.copy()
    dataWkCpy['location'] = dataWkCpy['geometry'].apply(lambda x: create_wkt_point_element(geom=x, srid=srid))
    # delete the old column before insert
    dataWkCpy = dataWkCpy.drop(columns="geometry")
    print(dataWkCpy)

    print('create table '+get_table_name())
    print(conn.execute(create_table_sql()))

    print('start inserting data-------')
    dataWkCpy.to_sql(get_table_name(), conn, if_exists='append', index=False,
                       dtype={'location': Geometry('POINT', srid)})

    print(pd.read_sql_query('select * from rfsnsw_bfpl', conn))