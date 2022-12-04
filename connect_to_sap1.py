#Import your dependencies
import platform
import os
import json
from hdbcli import dbapi

#verify the architecture of Python
print ("Platform architecture: " + platform.architecture()[0])

with open(os.path.join(os.getcwd(), 'env_cloud.json')) as f:
    hana_env_c = json.load(f)
    port_c = hana_env_c['port']
    user_c = hana_env_c['user']
    url_c  = hana_env_c['url']
    pwd_c  = hana_env_c['pwd']

#Initialize your connection
conn = dbapi.connect(
    #Option 1, retrieve the connection parameters from the hdbuserstore
    #key='USER1UserKey', # address, port, user and password are retrieved from the hdbuserstore

    #Option2, specify the connection parameters
    address=url_c,
    port=port_c,
    user=user_c,
    password=pwd_c,

    #Additional parameters
    #encrypt=True, # must be set to True when connecting to HANA as a Service
    #As of SAP HANA Client 2.6, connections on port 443 enable encryption by default (HANA Cloud)
    #sslValidateCertificate=False #Must be set to false when connecting
    #to an SAP HANA, express edition instance that uses a self-signed certificate.
)
#If no errors, print connected
print('connected')

cursor = conn.cursor()
sql_command = "select TITLE, FIRSTNAME, NAME from KIRAN_SCHEME.CUSTOMER;"
cursor.execute(sql_command)
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print ("%s" % col, end=" ")
    print ("  ")
cursor.close()
print("\n")

#Prepared statement example
sql_command2 = "call KIRAN_SCHEME.SHOW_RESERVATIONS(?,?);"
parameters = [11, "2020-12-24"]
cursor.execute(sql_command2, parameters)
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print ("%s" % col, end=" ")
    print (" ")
cursor.close()
conn.close()
