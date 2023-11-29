from bson.objectid import ObjectId
from server.databases.db_main import database as db
from server.utils.utils import komoditas_helper

komoditas_collection = db.get_collection("komoditas_collection")

async def retrieve_komoditass():
    komoditass = []
    async for komoditas in komoditas_collection.find():
        komoditass.append(komoditas_helper(komoditas))
    return komoditass

async def add_komoditas(komoditas_data: dict)->dict:
    data = await komoditas_collection.insert_one(komoditas_data)
    new_data = await komoditas_collection.find_one({"_id": data.inserted_id})
    return komoditas_helper(new_data)

async def retrieve_komoditas(id: int)->dict:
    komoditas = await komoditas_collection.find_one({"komoditas_id": id})
    if komoditas:
        return komoditas_helper(komoditas)

async def update_komoditas(id: int, data: dict):
    if len(data) < 1:
        return {"Data": "Null"}
    komoditas = await komoditas_collection.find_one({"komoditas_id": id})
    if komoditas:
        updated_komoditas = await komoditas_collection.update_one(
            {"komoditas_id": id}, {"$set": data}
        )
        if updated_komoditas:
            return await retrieve_komoditas(id)
        return {"Data": "Data not found"}

async def delete_komoditas(id:int):
    data = await komoditas_collection.find_one({"komoditas_id": id})
    if data:
        await komoditas_collection.delete_one({"komoditas_id": id})
        return {"Data": "Data deleted"}
