from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://mongo:SHBltFgfqJoMXTUcgOsZazZZQkuLqwVD@roundhouse.proxy.rlwy.net:46930')
database = client['pafcat-seguros']
