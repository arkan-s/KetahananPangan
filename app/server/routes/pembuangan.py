from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from server.controllers.pembuangancontroller import (retrieve_data_pembuangan, retrieve_list_pembuangan, add_pembuangan)
from server.models.pembuangan import (Pembuangan, UpdatePembuanganModel)
from server.utils.utils import pembuangan_helper
from server.models.responses import (ResponseModel, ErrorResponseModel)

pembuanganAPI = APIRouter()

@pembuanganAPI.get("/", response_description="Retrieve list of pembuangan database")
async def get_pembuangan():
    allpembuangan = await retrieve_list_pembuangan()
    if allpembuangan:
        return ResponseModel(allpembuangan, "Retrieved success")
    return ResponseModel(allpembuangan, "No Order Found")

@pembuanganAPI.post("/", response_description="Add new pembuangan to the database")
async def tambah_pembuangan(data: Pembuangan):
    trash = jsonable_encoder(data)
    new_trash = await add_pembuangan(trash)
    return ResponseModel(new_trash, "New order created")

@pembuanganAPI.get("/{id}", response_description="Get a pembuangan data")
async def get_one_order(id: int):
    pembuangan = await retrieve_data_pembuangan(id)
    if pembuangan:
        return ResponseModel(pembuangan, "Success")
    return ResponseModel(pembuangan, "Order not found")