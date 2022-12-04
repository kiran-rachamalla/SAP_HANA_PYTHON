import json

from hdbcli import dbapi


class sap_hana_connect:

    def __init__(self):
        with open('env_cloud.json', 'r') as a:
            hana_env_c = json.load(a)
            port_c = hana_env_c['port']
            user_c = hana_env_c['user']
            url_c = hana_env_c['url']
            pwd_c = hana_env_c['pwd']

        self.__conn = dbapi.connect(
            # Option 1, retrieve the connection parameters from the hdbuserstore
            # key='USER1UserKey', # address, port, user and password are retrieved from the hdbuserstore

            # Option2, specify the connection parameters
            address=url_c,
            port=port_c,
            user=user_c,
            password=pwd_c,

            # Additional parameters
            # encrypt=True, # must be set to True when connecting to HANA as a Service
            # As of SAP HANA Client 2.6, connections on port 443 enable encryption by default (HANA Cloud)
            # sslValidateCertificate=False #Must be set to false when connecting
            # to an SAP HANA, express edition instance that uses a self-signed certificate.
        )

    @property
    def conn(self):
        return self.__conn
