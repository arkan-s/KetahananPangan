from server.databases.db_main import database as db
from server.utils.utils import pengemasan_helper

pengemasan_collection = db.get_collection("pengemasan_collection")

async def retrieve_pengemasan(id: int)->dict:
    order = await pengemasan_collection.find_one({"order_id": id})
    if order:
        return pengemasan_helper(order)
    
async def add_pengemasan(order_data: dict):
    new_order = await pengemasan_collection.insert_one(order_data)
    new_data = await pengemasan_collection.find_one({"_id": new_order.inserted_id})
    return pengemasan_helper(new_data)

async def retrieve_list_pengemasan():
    orders = []
    async for order in pengemasan_collection.find():
        orders.append(pengemasan_helper(order))
    return orders

async def update_order(id: int, data: dict):
    if len(data)<1:
        return "No data is sent"
    order = await pengemasan_collection.find_one({"order_id": id})
    if order:
        updated_order = await pengemasan_collection.update_one(
            {"order_id": id}, {"$set": data}
        )
        if updated_order:
            return await retrieve_pengemasan(id)

async def delete_order_data(id: int):
    order = await pengemasan_collection.find_one({"order_id": id})
    if order:
        await pengemasan_collection.delete_one({"order_id": id})
        return {"Data": "Data deleted"}