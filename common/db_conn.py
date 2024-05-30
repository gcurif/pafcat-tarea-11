from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://mongo:ijqsJiTujRpsFlBGwiPFjfhrAmlAEmce@monorail.proxy.rlwy.net:46930')
database = client['pafcat-seguros']
