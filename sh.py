import geopandas as gpd
import os

data_path = 'C:\Users\10413\Desktop\1270055001_sa2_2016_aust_shape(2)'

statistical_areas = gpd.read_file( os.path.join(data_path, "SA2_2016_AUST.shp") )

sa2_areas_schema = '''CREATE TABLE SA2_Statistical_Areas (
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

pgquery(conn, "DROP TABLE IF EXISTS SA2_Statistical_Areas")
pgquery(conn, sa2_areas_schema)