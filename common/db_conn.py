from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://mongo:SHBltFgfqJoMXTUcgOsZazZZQkuLqwVD@roundhouse.proxy.rlwy.net:26332')
database = client['pafcat-seguros']
