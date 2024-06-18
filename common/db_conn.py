from pymongo import MongoClient

# Conectar a la base de datos MongoDB con un timeout aumentado
client = MongoClient(
    'mongodb://mongo:PXHKuTyUmPTGYnXcuTQeDbmiKKxXERux@monorail.proxy.rlwy.net:34963',
    socketTimeoutMS=180000  # 60 segundos
)
database = client['pafcat-seguros']

