import pandas as pd
from sqlalchemy import create_engine
import config

def pgconnect():
    # login credential of one group member xzha9245
    YOUR_UNIKEY = config.YOUR_UNIKEY
    YOUR_PW     = config.YOUR_PW
    DB_LOGIN    = 'y21s1d2x01_'+YOUR_UNIKEY
    conn = None
    try:
#         db = create_engine('postgres+psycopg2://'+DB_LOGIN+':'+YOUR_PW+'@soitpw11d59.shared.sydney.edu.au/', echo=False)
        db = create_engine('postgresql+psycopg2://'+DB_LOGIN+':'+YOUR_PW+'@soitpw11d59.shared.sydney.edu.au/', echo=False)
        conn = db.connect()
        print('connected')
    except Exception as e:
        print("unable to connect to the database")
        print(e)
    return db,conn

def pgquery( conn, sqlcmd, args=None, silent=False ):
    """ utility function to execute some SQL query statement
    can take optional arguments to fill in (dictionary)
    will print out on screen the result set of the query
    error and transaction handling built-in """
    retdf = pd.DataFrame()
    retval = False
    try:
        if args is None:
            retdf = pd.read_sql_query(sqlcmd,conn)
            print(retdf)
        else:
            retdf = pd.read_sql_query(sqlcmd,conn,params=args)
        if silent == False:
            print(retdf.shape)
            print(retdf.to_string())
        retval = True
    except Exception as e:
        if silent == False:
            print("db read error: ")
            print(e)
    return retval,retdf

def pgexecute(conn, sqlcmd, args=None, msg='', silent=False):
    """ utility function to execute some SQL query statement
       can take optional arguments to fill in (dictionary)
       will print out on screen the result set of the query
       error and transaction handling built-in """
    retval = False
    result_set = None

    try:
        if args is None:
            result_set = conn.execute(sqlcmd).fetchall()
        else:
            result_set = conn.execute(sqlcmd, args).fetchall()

        if silent == False:
            print("success: " + msg)
            for record in result_set:
                print(record)
        retval = True
    except Exception as e:
        if silent == False:
            print("db read error: ")
            print(e)
    return retval