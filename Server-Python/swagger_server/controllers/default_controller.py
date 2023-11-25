import connexion
import six

from swagger_server.models.komoditas import Komoditas  # noqa: E501
from swagger_server.models.pembuangan import Pembuangan  # noqa: E501
from swagger_server.models.pemesanan import Pemesanan  # noqa: E501
from swagger_server.models.pengemasan import Pengemasan  # noqa: E501
from swagger_server.models.pengguna import Pengguna  # noqa: E501
from swagger_server.models.pengiriman import Pengiriman  # noqa: E501
from swagger_server import util


def delete_komoditas_komoditas_id(komoditas_id):  # noqa: E501
    """delete_komoditas_komoditas_id

    Delete a komoditas # noqa: E501

    :param komoditas_id: 
    :type komoditas_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_komoditas_pemesanan_order_id(order_id):  # noqa: E501
    """delete_komoditas_pemesanan_order_id

    Delete a pemesanan # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_komoditas_pengemasan_order_id(order_id):  # noqa: E501
    """delete_komoditas_pengemasan_order_id

    Delete a pengemasan # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_komoditas_pengiriman_order_id(order_id):  # noqa: E501
    """delete_komoditas_pengiriman_order_id

    Delete a pengiriman # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_users_user_id(user_id):  # noqa: E501
    """delete_users_user_id

    Delete a user # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_komoditas():  # noqa: E501
    """Your GET endpoint

    Get list of komoditas # noqa: E501


    :rtype: List[Komoditas]
    """
    return 'do some magic!'


def get_komoditas_komoditas_id(komoditas_id):  # noqa: E501
    """Your GET endpoint

    Get komoditas by ID # noqa: E501

    :param komoditas_id: 
    :type komoditas_id: str

    :rtype: Komoditas
    """
    return 'do some magic!'


def get_komoditas_pembuangan():  # noqa: E501
    """Your GET endpoint

    Get list of pembuangan # noqa: E501


    :rtype: List[Pembuangan]
    """
    return 'do some magic!'


def get_komoditas_pembuangan_order_id(order_id):  # noqa: E501
    """Your GET endpoint

    Get a pembuangan by ID # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: Pembuangan
    """
    return 'do some magic!'


def get_komoditas_pemesanan():  # noqa: E501
    """Your GET endpoint

    Get list of pemesanan # noqa: E501


    :rtype: List[Pemesanan]
    """
    return 'do some magic!'


def get_komoditas_pemesanan_order_id(order_id):  # noqa: E501
    """Your GET endpoint

    Get pemesanan by ID # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: Pemesanan
    """
    return 'do some magic!'


def get_komoditas_pengemasan():  # noqa: E501
    """Your GET endpoint

    Get list of pengemasan # noqa: E501


    :rtype: List[Pengemasan]
    """
    return 'do some magic!'


def get_komoditas_pengemasan_order_id(order_id):  # noqa: E501
    """Your GET endpoint

    Get pengemasan by ID # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: Pengemasan
    """
    return 'do some magic!'


def get_komoditas_pengiriman():  # noqa: E501
    """Your GET endpoint

    Get list of pengiriman # noqa: E501


    :rtype: List[Pengiriman]
    """
    return 'do some magic!'


def get_komoditas_pengiriman_order_id(order_id):  # noqa: E501
    """Your GET endpoint

    Get pengiriman by ID # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: Pengiriman
    """
    return 'do some magic!'


def get_users():  # noqa: E501
    """Your GET endpoint

    Get list of users # noqa: E501


    :rtype: List[Pengguna]
    """
    return 'do some magic!'


def get_users_user_id(user_id):  # noqa: E501
    """Your GET endpoint

    Get a user by ID # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: Pengguna
    """
    return 'do some magic!'


def post_komoditas(body=None):  # noqa: E501
    """post_komoditas

    Create komoditas (s) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Komoditas.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_komoditas_pembuangan(body=None):  # noqa: E501
    """post_komoditas_pembuangan

    Create pembuangan (s) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pembuangan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_komoditas_pemesanan(body=None):  # noqa: E501
    """post_komoditas_pemesanan

    Create pemesanan (s) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pemesanan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_komoditas_pengemasan(body=None):  # noqa: E501
    """post_komoditas_pengemasan

    Create pengemasan (s) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengemasan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_komoditas_pengiriman(body=None):  # noqa: E501
    """post_komoditas_pengiriman

    Create pengiriman (s) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengiriman.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_users(body=None):  # noqa: E501
    """post_users

    Create new users data # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengguna.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_komoditas_komoditas_id(komoditas_id, body=None):  # noqa: E501
    """put_komoditas_komoditas_id

    Update a komoditas by ID # noqa: E501

    :param komoditas_id: 
    :type komoditas_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Komoditas.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_komoditas_pemesanan_order_id(order_id, body=None):  # noqa: E501
    """put_komoditas_pemesanan_order_id

    Update a pemesanan by ID # noqa: E501

    :param order_id: 
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pemesanan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_komoditas_pengemasan_order_id(order_id, body=None):  # noqa: E501
    """put_komoditas_pengemasan_order_id

    Update a pengemasan by ID # noqa: E501

    :param order_id: 
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengemasan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_komoditas_pengiriman_order_id(order_id, body=None):  # noqa: E501
    """put_komoditas_pengiriman_order_id

    Update a pengiriman by ID # noqa: E501

    :param order_id: 
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengiriman.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_users_user_id(user_id, body=None):  # noqa: E501
    """put_users_user_id

    Update a user by ID # noqa: E501

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pengguna.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
