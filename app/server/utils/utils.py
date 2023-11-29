# ser ---> cli
def user_helper(user)->dict:
    return {
        "_id": str(user["_id"]),
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "dateOfBirth": user["dateOfBirth"],
        "email": user["email"],
        "password": user["password"],
        "emailVerified": user["emailVerified"],
        "createDate": user["createDate"]
        }

def komoditas_helper(komoditas)->dict:
    return {
        "komoditas_id": komoditas["komoditas_id"],
        "nama": komoditas["nama"],
        "kategori": komoditas["kategori"],
        "deskripsi": komoditas["deskripsi"],
        "gudang_komoditas": gudang_helper(komoditas["gudang_komoditas"]),
        "stok": komoditas["stok"],
        "nilai_pasar": komoditas["nilai_pasar"]
    }

def gudang_helper(gudang)->dict:
    return {
        "gudang_id": gudang["gudang_id"],
        "nama": gudang["nama"],
        "kategori": gudang["kategori"],
        "lokasi": gudang["lokasi"]
    }

def pemesanan_helper(pemesanan)->dict:
    return {
        "order_id": pemesanan["order_id"],
        "nama_pemesan": pemesanan["nama_pemesan"],
        "alamat_pemesan": pemesanan["alamat_pemesan"],
        "list_barang": pemesanan["list_barang"],
        "total_harga": pemesanan["total_harga"],
        "status": pemesanan["status"]
    }