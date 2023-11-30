from typing import Optional, List
from pydantic import BaseModel, Field

class Pengiriman(BaseModel):
    order_id: int = Field(...)
    pengiriman_id: int = Field(...)
    nama_pemesan: str = Field(...)
    alamat_pemesan: str = Field(...)
    list_barang: List[int] = Field(...)
    status: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "order_id": 12,
                "pengiriman_id": 13,
                "nama_pemesan": "Arkan",
                "alamat_pemesan": "Jl. Buntu 1",
                "list_barang": [1, 2, 3],
                "status": "Siap dikirims"
            }
        }

class UpdatePengirimanModel(BaseModel):
    order_id: Optional[int] = Field(const=True)
    pengiriman_id: Optional[int] = Field(const=True)
    nama_pemesan: Optional[str] = Field(const=True)
    alamat_pemesan: Optional[str] = Field(const=True)
    list_barang: Optional[List[int]] = Field(const=True)
    status: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "status": "Dalam perjalanan"
            }
        }