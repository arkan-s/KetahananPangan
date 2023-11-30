from fastapi import FastAPI
from server.routes.pembuangan import pembuanganAPI
from server.routes.pengiriman import pengirimanAPI
from server.routes.pengemasan import pengemasanAPI
from server.routes.pemesanan import pemesananAPI
from server.routes.komoditas import komoditasAPI
from server.routes.user import userAPI
from server.routes.root import root_route

app = FastAPI()

app.include_router(root_route, tags=["root"])
app.include_router(userAPI, tags=["user"], prefix="/user")
app.include_router(komoditasAPI, tags=["komoditas"], prefix="/komoditas")
app.include_router(pemesananAPI, tags=["order"], prefix="/komoditas/pemesanan")
app.include_router(pengemasanAPI, tags=["pengemasan"], prefix="/komoditas/pengemasan")
app.include_router(pengirimanAPI, tags=["pengiriman"], prefix="/komoditas/pengiriman")
app.include_router(pembuanganAPI, tags=["pembuangan"], prefix="/komoditas/pembuangan")