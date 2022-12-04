import sys
import os
import json

from hana_ml.dataframe import ConnectionContext
with open(os.path.join(os.getcwd(), 'env_cloud.json')) as f:
    hana_env_c = json.load(f)
    port_c = hana_env_c['port']
    user_c = hana_env_c['user']
    url_c  = hana_env_c['url']
    pwd_c  = hana_env_c['pwd']

cc = ConnectionContext(url_c, port_c, user_c, pwd_c)
print(cc.hana_version())
print(cc.get_current_schema())
