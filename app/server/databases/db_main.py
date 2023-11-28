import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.KetPang

# Menginisiasi collection(table)
# komoditas_coll = database.get_collection("komoditas_collection")