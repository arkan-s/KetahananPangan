from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from server.controllers.usercontroller import (add_user, update_user, retrieve_user, retrieve_users, delete_user)
from server.models.user import (UpdateUserModel, User)
from server.utils.utils import user_helper
from server.models.responses import (ResponseModel, ErrorResponseModel)

userAPI = APIRouter()

@userAPI.get("/", response_description="Get List of Users from Database")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Retrieved success")
    return ResponseModel(users, "Users is empty")

@userAPI.post("/", response_description="Add New User Data to Database")
async def add_user_data(user: User = Body(...)):
    user_ = jsonable_encoder(user)
    new_user = await add_user(user_)
    return  ResponseModel(new_user, "New User Data Created")

@userAPI.get("/{id}", response_description="Get A User by ID")
async def get_user(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "Retrieved user {} success".format(id))
    return ResponseModel(user, "No Matching User ID")

@userAPI.put("/{id}", response_description="Update User Data to Database")
async def update_user_data(id, user: UpdateUserModel = Body(...)):
    user_dict = user.dict(exclude_none=True)
    user_ = jsonable_encoder(user_dict)
    new_user = await update_user(id, user_)
    return  ResponseModel(new_user, "New User Data Updated")

@userAPI.delete("/{id}", response_description="Delete User Data")
async def delete_user_data(id):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
    )
