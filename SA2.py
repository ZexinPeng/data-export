import geopandas as gpd
import os
import basetool

import pandas as pd
from shapely.geometry import Point, Polygon, MultiPolygon
from geoalchemy2 import Geometry, WKTElement

# Use GeoAlchemy's WKTElement to create a geom with SRID
# NOTE :: THIS ONLY CHANGES POLYGON's to MULTI POLYGONS, IF YOU HAVE OTHER TYPES IN YOUR DATA,
#     YOU WILL HAVE TO CONSULT THE GEOALCHEMY AND SHAPELY DOCUMENTATION ON HOW TO HANDLE THOSE
def create_wkt_element(geom,srid):
    if (geom.geom_type == 'Polygon'):
        geom = MultiPolygon([geom])
    return WKTElement(geom.wkt, srid)

if __name__ == '__main__':
    pd.set_option('display.max_columns', 1500)  # 最大列数
    pd.set_option('display.max_rows', 100)  # 最大列数
    pd.set_option('display.width', 8000)

    # login to database
    db, conn = basetool.pgconnect()

    data_path = '''C:\data\SA2'''
    print('data path is '+data_path)
    srid = 4283

    # read data
    statistical_areas = gpd.read_file( os.path.join(data_path, "SA2_2016_AUST.shp"))
    statistical_areas.rename(columns={'SA2_MAIN16': 'sa2_maincode', 'SA2_5DIG16': 'sa2_5digitcode'
        , 'SA2_NAME16': 'sa2_name16', 'SA3_CODE16': 'sa3_code16', 'SA3_NAME16': 'sa3_name16'
        , 'SA4_CODE16': 'sa4_code', 'SA4_NAME16': 'sa4_name', 'GCC_CODE16': 'gccsa_code'
        , 'GCC_NAME16': 'gccsa_name', 'STE_CODE16': 'state_code', 'STE_NAME16': 'state_name'
        , 'AREASQKM16': 'area_in_sqkm'}, inplace=True)

    # convert POLYGON into MULTIPOLYGON
    countriesWkCpy = statistical_areas.copy()
    countriesWkCpy['geom'] = statistical_areas['geometry'].dropna().apply(lambda x: create_wkt_element(geom=x, srid=srid))

    # delete the old column before insert
    countriesWkCpy = countriesWkCpy.drop(columns="geometry")
    print(countriesWkCpy.dropna())

    sa2_areas_schema = '''CREATE TABLE sa2_2016_aust (
                     sa2_maincode INT,
                     sa2_5digitcode INT,
                     sa2_name16  TEXT,
                     sa3_code16 INT,
                     sa3_name16 TEXT,
                     sa4_code INT,
                     sa4_name TEXT,
                     gccsa_code INT,
                     gccsa_name TEXT,
                     state_code INT,
                     state_name TEXT,
                     area_in_sqkm NUMERIC,
                     geom GEOMETRY(MULTIPOLYGON, 4283))'''

    table_name = "sa2_2016_aust"

    print('start inserting data-------')
    countriesWkCpy.dropna().to_sql(table_name, conn, if_exists='replace', index=False,
                         dtype={'geom': Geometry('MULTIPOLYGON', srid)})
    query = "SELECT * FROM sa2_2016_aust"
    print(pd.read_sql_query(query, conn))