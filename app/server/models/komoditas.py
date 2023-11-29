from typing import Optional
from datetime import date
from pydantic import BaseModel, Field,  ValidationError, validator

class Komoditas(BaseModel):
    komoditas_id: int = Field(..., unique=True)
    nama: str = Field(...)
    kategori: str = Field(...)
    deskripsi: str = Field(...)
    gudang_komoditas: dict
    stok: int = Field(...)
    nilai_pasar: int = Field(...)
    '''@validator("gudang_komoditas", pre=True, allow_reuse=True)
    def check_gudang_komoditas(cls, value):
        expected_keys = {"gudang_id", "nama", "kategori", "lokasi"}

        if not all(key in value for key in expected_keys):
            missing_keys = expected_keys - set(value.keys())
            raise ValueError(f"gudang_komoditas harus memiliki kunci-kunci berikut: {missing_keys}")
        
        return value'''
    
    class Config:
        schema_extra = {
            "example": {
                "komoditas_id": 1,
                "nama": "Padi",
                "kategori": "Bahan Pokok",
                "deskripsi": "Beras jenis padi",
                "gudang_komoditas": {
                    "gudang_id": 101,
                    "nama": "Gudang ABC",
                    "kategori": "Gudang Pangan",
                    "lokasi": "Jakarta"
                },
                "stok": 1000,
                "nilai_pasar": 50000
            }
        }

class UpdateKomoditasModel(BaseModel):
    komoditas_id: Optional[int]
    nama: Optional[str] 
    kategori: Optional[str]
    deskripsi: Optional[str]
    gudang_komoditas: Optional[dict]
    stok: Optional[int]
    nilai_pasar: Optional[int]
    '''
    @validator("gudang_komoditas", pre=True, allow_reuse=True)
    def check_gudang_komoditas(cls, value):
        expected_keys = {"gudang_id", "nama", "kategori", "lokasi"}

        if not all(key in value for key in expected_keys):
            missing_keys = expected_keys - set(value.keys())
            raise ValueError(f"gudang_komoditas harus memiliki kunci-kunci berikut: {missing_keys}")
        
        return value
    '''

