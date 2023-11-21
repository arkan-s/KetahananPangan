'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.deleteKomoditasKomoditas_id = function deleteKomoditasKomoditas_id (req, res, next, komoditas_id) {
  Default.deleteKomoditasKomoditas_id(komoditas_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteKomoditasPemesananOrder_id = function deleteKomoditasPemesananOrder_id (req, res, next, order_id) {
  Default.deleteKomoditasPemesananOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteKomoditasPengemasanOrder_id = function deleteKomoditasPengemasanOrder_id (req, res, next, order_id) {
  Default.deleteKomoditasPengemasanOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteKomoditasPengirimanOrder_id = function deleteKomoditasPengirimanOrder_id (req, res, next, order_id) {
  Default.deleteKomoditasPengirimanOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteUsersUserId = function deleteUsersUserId (req, res, next, userId) {
  Default.deleteUsersUserId(userId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditas = function getKomoditas (req, res, next) {
  Default.getKomoditas()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasKomoditas_id = function getKomoditasKomoditas_id (req, res, next, komoditas_id) {
  Default.getKomoditasKomoditas_id(komoditas_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPembuangan = function getKomoditasPembuangan (req, res, next) {
  Default.getKomoditasPembuangan()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPembuanganOrder_id = function getKomoditasPembuanganOrder_id (req, res, next, order_id) {
  Default.getKomoditasPembuanganOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPemesanan = function getKomoditasPemesanan (req, res, next) {
  Default.getKomoditasPemesanan()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPemesananOrder_id = function getKomoditasPemesananOrder_id (req, res, next, order_id) {
  Default.getKomoditasPemesananOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPengemasan = function getKomoditasPengemasan (req, res, next) {
  Default.getKomoditasPengemasan()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPengemasanOrder_id = function getKomoditasPengemasanOrder_id (req, res, next, order_id) {
  Default.getKomoditasPengemasanOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPengiriman = function getKomoditasPengiriman (req, res, next) {
  Default.getKomoditasPengiriman()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getKomoditasPengirimanOrder_id = function getKomoditasPengirimanOrder_id (req, res, next, order_id) {
  Default.getKomoditasPengirimanOrder_id(order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getUsers = function getUsers (req, res, next) {
  Default.getUsers()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getUsersUserId = function getUsersUserId (req, res, next, userId) {
  Default.getUsersUserId(userId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postKomoditas = function postKomoditas (req, res, next, body) {
  Default.postKomoditas(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postKomoditasPembuangan = function postKomoditasPembuangan (req, res, next, body) {
  Default.postKomoditasPembuangan(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postKomoditasPemesanan = function postKomoditasPemesanan (req, res, next, body) {
  Default.postKomoditasPemesanan(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postKomoditasPengemasan = function postKomoditasPengemasan (req, res, next, body) {
  Default.postKomoditasPengemasan(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postKomoditasPengiriman = function postKomoditasPengiriman (req, res, next, body) {
  Default.postKomoditasPengiriman(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postUsers = function postUsers (req, res, next, body) {
  Default.postUsers(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putKomoditasKomoditas_id = function putKomoditasKomoditas_id (req, res, next, body, komoditas_id) {
  Default.putKomoditasKomoditas_id(body, komoditas_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putKomoditasPemesananOrder_id = function putKomoditasPemesananOrder_id (req, res, next, body, order_id) {
  Default.putKomoditasPemesananOrder_id(body, order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putKomoditasPengemasanOrder_id = function putKomoditasPengemasanOrder_id (req, res, next, body, order_id) {
  Default.putKomoditasPengemasanOrder_id(body, order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putKomoditasPengirimanOrder_id = function putKomoditasPengirimanOrder_id (req, res, next, body, order_id) {
  Default.putKomoditasPengirimanOrder_id(body, order_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putUsersUserId = function putUsersUserId (req, res, next, body, userId) {
  Default.putUsersUserId(body, userId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
