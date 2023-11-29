from server.databases.db_main import database as db
from server.utils.utils import pemesanan_helper

pemesanan_collection = db.get_collection("pemesanan_collection")

async def retrieve_pemesanan(id: int)->dict:
    order = await pemesanan_collection.find_one({"order_id": id})
    if order:
        return pemesanan_helper(order)
    
async def add_pemesanan(order_data: dict):
    new_order = await pemesanan_collection.insert_one(order_data)
    new_data = await pemesanan_collection.find_one({"_id": new_order.inserted_id})
    return pemesanan_helper(new_data)

async def retrieve_list_pemesanan():
    orders = []
    async for order in pemesanan_collection.find():
        orders.append(pemesanan_helper(order))
    return orders

async def update_order(id: int, data: dict):
    if len(data)<1:
        return "No data is sent"
    order = await pemesanan_collection.find_one({"order_id": id})
    if order:
        updated_order = await pemesanan_collection.update_one(
            {"order_id": id}, {"$set": data}
        )
        if updated_order:
            return await retrieve_pemesanan(id)

async def delete_order_data(id: int):
    order = await pemesanan_collection.find_one({"order_id": id})
    if order:
        await pemesanan_collection.delete_one({"order_id": id})
        return {"Data": "Data deleted"}