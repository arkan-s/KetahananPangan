from server.databases.db_main import database as db
from server.utils.utils import pengiriman_helper

pengiriman_collection = db.get_collection("pengiriman_collection")

async def retrieve_pengiriman(id: int)->dict:
    order = await pengiriman_collection.find_one({"pengiriman_id": id})
    if order:
        return pengiriman_helper(order)
    
async def add_pengiriman(order_data: dict):
    new_order = await pengiriman_collection.insert_one(order_data)
    new_data = await pengiriman_collection.find_one({"_id": new_order.inserted_id})
    return pengiriman_helper(new_data)

async def retrieve_list_pengiriman():
    orders = []
    async for order in pengiriman_collection.find():
        orders.append(pengiriman_helper(order))
    return orders

async def update_pengiriman(id: int, data: dict):
    if len(data)<1:
        return "No data is sent"
    order = await pengiriman_collection.find_one({"pengiriman_id": id})
    if order:
        updated_order = await pengiriman_collection.update_one(
            {"pengiriman_id": id}, {"$set": data}
        )
        if updated_order:
            return await retrieve_pengiriman(id)

async def delete_pengiriman(id: int):
    order = await pengiriman_collection.find_one({"pengiriman_id": id})
    if order:
        await pengiriman_collection.delete_one({"pengiriman_id": id})
        return {"Data": "Data deleted"}