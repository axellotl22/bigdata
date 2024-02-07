
import base64
import struct

from pymongo.mongo_client import MongoClient
from bson.binary import Binary



base64_data= "MC4yNzk2MjEzOTMwMzE1NTcz"
    #'new BinData(0, "MC4yNzk2MjEzOTMwMzE1NTcz")'
bin_data= float(base64.b64decode(base64_data))
print(bin_data)
