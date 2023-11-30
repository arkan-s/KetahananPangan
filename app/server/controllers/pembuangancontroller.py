from server.databases.db_main import database as db
from server.utils.utils import pembuangan_helper

pembuangan_collection = db.get_collection("pembuangan_collection")

async def retrieve_data_pembuangan(id: int)->dict:
    order = await pembuangan_collection.find_one({"id": id})
    if order:
        return pembuangan_helper(order)
    
async def add_pembuangan(order_data: dict):
    new_order = await pembuangan_collection.insert_one(order_data)
    new_data = await pembuangan_collection.find_one({"_id": new_order.inserted_id})
    return pembuangan_helper(new_data)

async def retrieve_list_pembuangan():
    orders = []
    async for order in pembuangan_collection.find():
        orders.append(pembuangan_helper(order))
    return orders