from bson.objectid import ObjectId
from server.databases.db_main import database as db
from server.utils.utils import user_helper

users_collection = db.get_collection("users_collection")

# Retrieve all users present in the database /users["GET"]
async def retrieve_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users

# Add a new user into to the database /users["POST"]  Auth/JWT
async def add_user(user_data: dict) -> dict:
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve a user with a matching ID /user/{id}["GET"]
async def retrieve_user(id: str) -> dict:
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)
    
# Update a user with a matching ID /user/{id}["PUT"] auth/JWT
async def update_user(id, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return "No data is sent"
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return "No data is updated"

# Delete a user from the database /user/{id}["DELETE"] auth/JWT
async def delete_user(id: str):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        await users_collection.delete_one({"_id": ObjectId(id)})
        return True