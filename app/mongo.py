from pymongo import MongoClient
from django.conf import settings

def get_mongoo_client():
    return MongoClient(
        settings.MONGO_URI,
        retryWrites=True,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
        readPreference="primary"
    )








































# (venv) PS C:\Users\HP\SharedAndInventory\ReservationService> mongosh
# Current Mongosh Log ID: 689c4755cddb7394b1eec4a8
# Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.6
# Using MongoDB:          8.0.11
# Using Mongosh:          2.5.6

# For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

# ------
#    The server generated these startup warnings when booting
#    2025-08-01T17:12:07.801+05:30: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
# ------

# test> use admin
# switched to db admin
# admin> db.createUser({
# ...   user: "appuser",
# ...   pwd: "password",
# ...   roles: [ { role: "readWrite", db: "invdb" } ]
# ... })
# { ok: 1 }