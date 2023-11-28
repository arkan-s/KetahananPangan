from typing import Optional
from pydantic import BaseModel, Field, validator

class Pemesanan(BaseModel):
    order_id: int = Field(...)
    nama_pemesan: str = Field(...)
    alamat_pemesan: str = Field(...)
    list_barang: list = Field(...)
    total_harga: str = Field(...)
    status: bool = Field(...)
    @validator("status", pre=True, allow_reuse=True)
    def check_gudang_komoditas(cls, value):
        expected_keys = {"gudang_id", "nama", "kategori", "lokasi"}

        if not all(key in value for key in expected_keys):
            missing_keys = expected_keys - set(value.keys())
            raise ValueError(f"gudang_komoditas harus memiliki kunci-kunci berikut: {missing_keys}")
        
        return value
    
    class Config:
        schema_extra = {
            "example": {
                "order_id": 12,
                "nama_pemesan": "Arkan",
                "alamat_pemesan": "Jl. Buntu 1",
                "list_barang": [1, 2, 3],
                "total_harga": 12300,
                "status": "Menunggu pembayaran"
            }
        }

class UpdatePemesananModel(BaseModel):
    order_id: int = Field(const=True)
    nama_pemesan: str = Field(const=True)
    alamat_pemesan: str = Field(const=True)
    list_barang: list = Field(const=True)
    total_harga: str = Field(const=True)
    status: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "order_id": 12,
                "nama_pemesan": "Arkan",
                "alamat_pemesan": "Jl. Buntu 1",
                "list_barang": [1, 2, 3],
                "total_harga": 12300,
                "status": "Menunggu pembayaran"
            }
        }
