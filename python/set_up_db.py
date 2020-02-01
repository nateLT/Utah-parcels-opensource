import urllib.request
import os
import subprocess
from zipfile import ZipFile
import shutil
import psycopg2

url = 'https://opendata.arcgis.com/datasets/69477c1143924bc9990cdb930b033fb5_0.zip'
zipname = 'utahgis.zip'
def download_url(url):
    if os.path.exists(zipname):
        return 'already downloaded'
    else:
        urllib.request.urlretrieve(url, zipname)
        return 'downloaded'

def unzip_download(zipname):
    if os.path.exists('gis'):
        return 'zip compled'
    else:
        with ZipFile(zipname, 'r') as zipObj:
            zipObj.extractall('gis')
        return 'already ziped'

def reproject_code():
    try:
        os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:3857 gis\output.shp gis\Utah_Utah_County_Parcels_LIR.shp')
        return 'reprojection complete'
    except:
        return 'reprojection fail'

def import_postgis():
    try:
        os.system('ogr2ogr -append -f "PostgreSQL" -explodecollections -nlt POLYGON PG:"host=localhost user=postgres dbname=postgres password=password " gis\output.shp -nln parcel -lco geometry_name=geom   -t_srs EPSG:3857')
        return 'postgis complete'
    except:
        return 'postgis failed'

def delete_folder():
    try:
        shutil.rmtree('gis')
        return 'complete delete'
    except:
        return 'failed delete'

def query_postgres():
    #//not used set might add some stuff to clean the database
    con = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port="5432")
    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("INSERT INTO STUDENT (NAME,AGE,COURSE,DEPARTMENT) VALUES ('John', 18, 'Computer Science', 'ICT')")
    con.commit()
    print("Record inserted successfully")
    con.close()

    
downloadstatus = download_url(url)
print(downloadstatus)
zipstatus = unzip_download(zipname)
print(zipstatus)
reprojstatus = reproject_code()
print(reprojstatus)
postgisstatus = import_postgis()
print(postgisstatus)
deletestatus = delete_folder()
print(deletestatus)







