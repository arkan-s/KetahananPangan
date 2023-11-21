'use strict';


/**
 * Delete a komoditas
 *
 * komoditas_id String 
 * no response value expected for this operation
 **/
exports.deleteKomoditasKomoditas_id = function(komoditas_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Delete a pemesanan
 *
 * order_id String 
 * no response value expected for this operation
 **/
exports.deleteKomoditasPemesananOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Delete a pengemasan
 *
 * order_id String 
 * no response value expected for this operation
 **/
exports.deleteKomoditasPengemasanOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Delete a pengiriman
 *
 * order_id String 
 * no response value expected for this operation
 **/
exports.deleteKomoditasPengirimanOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Delete a user
 *
 * userId String 
 * no response value expected for this operation
 **/
exports.deleteUsersUserId = function(userId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Your GET endpoint
 * Get list of komoditas
 *
 * returns List
 **/
exports.getKomoditas = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "komoditas_id" : 0,
  "nama" : "nama",
  "kategori" : "kategori",
  "gudang_komoditas" : {
    "Kategori" : "Kategori",
    "Lokasi" : "Lokasi",
    "gudang_id" : 6,
    "Nama" : "Nama"
  },
  "nilai_pasar" : 5,
  "deskripsi" : "deskripsi",
  "stok" : 1
}, {
  "komoditas_id" : 0,
  "nama" : "nama",
  "kategori" : "kategori",
  "gudang_komoditas" : {
    "Kategori" : "Kategori",
    "Lokasi" : "Lokasi",
    "gudang_id" : 6,
    "Nama" : "Nama"
  },
  "nilai_pasar" : 5,
  "deskripsi" : "deskripsi",
  "stok" : 1
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get komoditas by ID
 *
 * komoditas_id String 
 * returns Komoditas
 **/
exports.getKomoditasKomoditas_id = function(komoditas_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "komoditas_id" : 0,
  "nama" : "nama",
  "kategori" : "kategori",
  "gudang_komoditas" : {
    "Kategori" : "Kategori",
    "Lokasi" : "Lokasi",
    "gudang_id" : 6,
    "Nama" : "Nama"
  },
  "nilai_pasar" : 5,
  "deskripsi" : "deskripsi",
  "stok" : 1
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get list of pembuangan
 *
 * returns List
 **/
exports.getKomoditasPembuangan = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "list_barang" : [ 6, 6 ],
  "id" : 0,
  "alasan" : [ "alasan", "alasan" ],
  "status" : "status"
}, {
  "list_barang" : [ 6, 6 ],
  "id" : 0,
  "alasan" : [ "alasan", "alasan" ],
  "status" : "status"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get a pembuangan by ID
 *
 * order_id String 
 * returns Pembuangan
 **/
exports.getKomoditasPembuanganOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "list_barang" : [ 6, 6 ],
  "id" : 0,
  "alasan" : [ "alasan", "alasan" ],
  "status" : "status"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get list of pemesanan
 *
 * returns List
 **/
exports.getKomoditasPemesanan = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "total_harga" : 1,
  "order_id" : 0,
  "status" : "status"
}, {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "total_harga" : 1,
  "order_id" : 0,
  "status" : "status"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get pemesanan by ID
 *
 * order_id String 
 * returns Pemesanan
 **/
exports.getKomoditasPemesananOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "total_harga" : 1,
  "order_id" : 0,
  "status" : "status"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get list of pengemasan
 *
 * returns List
 **/
exports.getKomoditasPengemasan = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
}, {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get pengemasan by ID
 *
 * order_id String 
 * returns Pengemasan
 **/
exports.getKomoditasPengemasanOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "list_barang" : [ 6, 6 ],
  "alamat_pemesan" : "alamat_pemesan",
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get list of pengiriman
 *
 * returns List
 **/
exports.getKomoditasPengiriman = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "list_barang" : [ 1, 1 ],
  "alamat_pemesan" : "alamat_pemesan",
  "pengiriman_id" : 6,
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
}, {
  "list_barang" : [ 1, 1 ],
  "alamat_pemesan" : "alamat_pemesan",
  "pengiriman_id" : 6,
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get pengiriman by ID
 *
 * order_id String 
 * returns Pengiriman
 **/
exports.getKomoditasPengirimanOrder_id = function(order_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "list_barang" : [ 1, 1 ],
  "alamat_pemesan" : "alamat_pemesan",
  "pengiriman_id" : 6,
  "nama_pemesan" : "nama_pemesan",
  "order_id" : 0,
  "status" : "status"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get list of users
 *
 * returns List
 **/
exports.getUsers = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "firstName" : "firstName",
  "lastName" : "lastName",
  "emailVerified" : true,
  "dateOfBirth" : "1997-10-31T00:00:00.000+00:00",
  "id" : 0,
  "email" : "",
  "createDate" : "2000-01-23"
}, {
  "firstName" : "firstName",
  "lastName" : "lastName",
  "emailVerified" : true,
  "dateOfBirth" : "1997-10-31T00:00:00.000+00:00",
  "id" : 0,
  "email" : "",
  "createDate" : "2000-01-23"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Your GET endpoint
 * Get a user by ID
 *
 * userId String 
 * returns Pengguna
 **/
exports.getUsersUserId = function(userId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "firstName" : "firstName",
  "lastName" : "lastName",
  "emailVerified" : true,
  "dateOfBirth" : "1997-10-31T00:00:00.000+00:00",
  "id" : 0,
  "email" : "",
  "createDate" : "2000-01-23"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Create komoditas (s)
 *
 * body Komoditas  (optional)
 * no response value expected for this operation
 **/
exports.postKomoditas = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Create pembuangan (s)
 *
 * body Pembuangan  (optional)
 * no response value expected for this operation
 **/
exports.postKomoditasPembuangan = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Create pemesanan (s)
 *
 * body Pemesanan  (optional)
 * no response value expected for this operation
 **/
exports.postKomoditasPemesanan = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Create pengemasan (s)
 *
 * body Pengemasan  (optional)
 * no response value expected for this operation
 **/
exports.postKomoditasPengemasan = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Create pengiriman (s)
 *
 * body Pengiriman  (optional)
 * no response value expected for this operation
 **/
exports.postKomoditasPengiriman = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Create new users data
 *
 * body Pengguna  (optional)
 * no response value expected for this operation
 **/
exports.postUsers = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update a komoditas by ID
 *
 * body Komoditas  (optional)
 * komoditas_id String 
 * no response value expected for this operation
 **/
exports.putKomoditasKomoditas_id = function(body,komoditas_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update a pemesanan by ID
 *
 * body Pemesanan  (optional)
 * order_id String 
 * no response value expected for this operation
 **/
exports.putKomoditasPemesananOrder_id = function(body,order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update a pengemasan by ID
 *
 * body Pengemasan  (optional)
 * order_id String 
 * no response value expected for this operation
 **/
exports.putKomoditasPengemasanOrder_id = function(body,order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update a pengiriman by ID
 *
 * body Pengiriman  (optional)
 * order_id String 
 * no response value expected for this operation
 **/
exports.putKomoditasPengirimanOrder_id = function(body,order_id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update a user by ID
 *
 * body Pengguna  (optional)
 * userId String 
 * no response value expected for this operation
 **/
exports.putUsersUserId = function(body,userId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

