from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field,  ValidationError, validator

class Pembuangan(BaseModel):
    id: int = Field(..., unique=True)
    list_barang: List[int] = Field(...)
    alasan: List[str] = Field(...)
    status: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "list_barang": [1, 2, 3],
                "alasan": ["Expired", "Produk ganti"],
                "status": "Diproses"
            }
        }

class UpdatePembuanganModel(BaseModel):
    id: Optional[int] = Field(const=True)
    list_barang: Optional[List[int]] = Field(const=True)
    alasan: Optional[List[str]] = Field(const=True)
    status: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "list_barang": [1, 2, 3],
                "alasan": ["Expired", "Produk ganti"],
                "status": "Dibuang"
            }
        }