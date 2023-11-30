from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from server.controllers.pengemasancontroller import (retrieve_pengemasan, retrieve_list_pengemasan, add_pengemasan, update_order, delete_order_data)
from server.models.pemesanan import (Pemesanan, UpdatePemesananModel)
from server.utils.utils import pengemasan_helper
from server.models.responses import (ResponseModel, ErrorResponseModel)

pengemasanAPI = APIRouter()

@pengemasanAPI.get("/", response_description="Get List of Orders from Database")
async def get_all_orders():
    allorders = await retrieve_list_pengemasan()
    if allorders:
        return ResponseModel(allorders, "Retrieved success")
    return ResponseModel(allorders, "No Order Found")

@pengemasanAPI.post("/", response_description="Add new order to the database")
async def add_order(data: Pemesanan):
    order = jsonable_encoder(data)
    new_order = await add_pengemasan(order)
    return ResponseModel(new_order, "New order created")

@pengemasanAPI.get("/{id}", response_description="Get an order data")
async def get_one_order(id: int):
    order = await retrieve_pengemasan(id)
    if order:
        return ResponseModel(order, "Success")
    return ResponseModel(order, "Order not found")

@pengemasanAPI.put("/{id}", response_description="Update a data in database")
async def update_a_order(id:int, data: UpdatePemesananModel = Body(...)):
    try:
        data_dict = data.dict(exclude_none=True)
        #order = jsonable_encoder(data_dict)
        new_data = await update_order(id, data_dict)
        return ResponseModel(new_data, "Order data updated")
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error updating Order data: {e}")
        # Return an HTTPException with a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal Server Error")

@pengemasanAPI.delete("/{id}", response_description="Delete an order")
async def hapus_order(id: int):
    deleted_order = await delete_order_data(id)
    if deleted_order:
        return ResponseModel(
            "Order with ID: {} removed".format(id), "Order deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Order with id {0} doesn't exist".format(id)
    )