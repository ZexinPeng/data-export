# data-export
export data from local files into the database
# how to do
1. config the python environment, download it on https://www.python.org/, and select the latest version(3.9.5)
2. use pip to install all dependencies(you may encounter some unexpected errors depending on your machine's running environment)

hints: if the download speed may be not satisfactory. You can change the source of pip installation.


* pip install pandas
* pip install sqlalchemy
* pip install geoalchemy2
* pip install geopandas
* pip install shapely
3. config and connect VPN
4. add 'config.py' into the directory, and add and modify the following two lines according to your unikey and password in 'YOUR_UNIKEY' and 'YOUR_PASSWORD'.

YOUR_UNIKEY = 'YOUR_UNIKEY'

YOUR_PW = 'YOUR_PASSWORD'
5. modify the 'data_path' parameter in 'business.py', 'neighbor.py', 'statistical.py', 'rfsn.py', 'SA2.py' respectively and run them to export data into your database.

## Attention
There are some errors in your offering template code, but , do not worry, I have corrected them. Another important thing to point out: the column name in postgresql must 
be lower case, and you have to rename the column name of data that are export from the data files and keep them consistent with the column names in your database， 
ohterwise you will not add any dateum into your database.

# Any question that you cannot sovle or feedback
contact me directivly with wechat: pzx19971204
