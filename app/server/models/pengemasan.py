from typing import Optional, List
from pydantic import BaseModel, Field

class Pengemasan(BaseModel):
    order_id: int = Field(...)
    nama_pemesan: str = Field(...)
    alamat_pemesan: str = Field(...)
    list_barang: List[int] = Field(...)
    status: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "order_id": 12,
                "nama_pemesan": "Arkan",
                "alamat_pemesan": "Jl. Buntu 1",
                "list_barang": [1, 2, 3],
                "total_harga": 12300,
                "status": "Sedang dikemas"
            }
        }

class UpdatePengemasanModel(BaseModel):
    order_id: Optional[int] = Field(const=True)
    nama_pemesan: Optional[str] = Field(const=True)
    alamat_pemesan: Optional[str] = Field(const=True)
    list_barang: Optional[List[int]] = Field(const=True)
    status: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "status": "Siap dikirim"
            }
        }