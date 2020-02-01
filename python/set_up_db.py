import urllib.request
import os
import subprocess
from zipfile import ZipFile
import shutil
import psycopg2

url = 'https://doc-08-3s-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/5ruob4uon2aqftuugcsc2pj6jd44lpmh/1575244800000/06829744149498025287/*/0ByStJjVZ7c7mZHE1UXowZ3QyRVE?e=download'
zipname = 'utahgis.zip'
def download_url(url):
    try:
        if os.pa
        
        return 'zip failed'

def reproject_code():
    try:
        os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:3857 gis\output.shp gis\Parcels_Utah\Parcels_Utah.shp')
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







