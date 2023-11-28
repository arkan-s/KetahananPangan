from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from server.controllers.komoditascontroller import (retrieve_komoditas, retrieve_komoditass, add_komoditas, update_komoditas, delete_komoditas)
from server.models.komoditas import (UpdateKomoditasModel, Komoditas)
from server.utils.utils import komoditas_helper
from server.models.responses import (ResponseModel, ErrorResponseModel)

komoditasAPI = APIRouter()

@komoditasAPI.get("/", response_description="Get List of Komoditas from Database")
async def get_all_komoditas():
    allkomoditas = await retrieve_komoditass()
    if allkomoditas:
        return ResponseModel(allkomoditas, "Retrieved success")
    return ResponseModel(allkomoditas, "No Komoditas Found")

@komoditasAPI.post("/", response_description="Add New Komoditas Data to Database")
async def add_komoditas_data(komoditas: Komoditas = Body(...)):
    komoditas = jsonable_encoder(komoditas)
    new_komoditas = await add_komoditas(komoditas)
    return ResponseModel(new_komoditas, "New Komoditas Data Created")

@komoditasAPI.get("/{id}", response_description="Get A Komooditas Data from Database")
async def get_one_komoditas(id: int):
    komoditas = await retrieve_komoditas(id)
    if komoditas:
        return ResponseModel(komoditas, "Komoditas {} successfully retrieved".format(komoditas["nama"]))
    return ResponseModel(komoditas,"Komoditas is not found")

@komoditasAPI.put("/{id}", response_description="Update komoditas data from Database")
async def update_a_komoditas(id:int, data: UpdateKomoditasModel = Body(...)):
    data_dict = data.dict(exclude_none=True)
    komoditas_ = jsonable_encoder(data_dict)
    new_data = await update_komoditas(id, komoditas_)
    return  ResponseModel(new_data, "New Komoditas Data Updated")

@komoditasAPI.delete("/{id}", response_description="Delete komoditas data from Database")
async def remove_komoditas(id: int):
    deleted_komoditas = delete_komoditas(id)
    if deleted_komoditas:
        return ResponseModel(
            "Komodoitas with ID: {} removed".format(id), "Komodoitas deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Komodoitas with id {0} doesn't exist".format(id)
    )