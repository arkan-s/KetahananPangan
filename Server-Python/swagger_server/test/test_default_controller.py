# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.komoditas import Komoditas  # noqa: E501
from swagger_server.models.pembuangan import Pembuangan  # noqa: E501
from swagger_server.models.pemesanan import Pemesanan  # noqa: E501
from swagger_server.models.pengemasan import Pengemasan  # noqa: E501
from swagger_server.models.pengguna import Pengguna  # noqa: E501
from swagger_server.models.pengiriman import Pengiriman  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_delete_komoditas_komoditas_id(self):
        """Test case for delete_komoditas_komoditas_id

        
        """
        response = self.client.open(
            '/komoditas/{komoditas_id}'.format(komoditas_id='komoditas_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_komoditas_pemesanan_order_id(self):
        """Test case for delete_komoditas_pemesanan_order_id

        
        """
        response = self.client.open(
            '/komoditas/pemesanan/{order_id}'.format(order_id='order_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_komoditas_pengemasan_order_id(self):
        """Test case for delete_komoditas_pengemasan_order_id

        
        """
        response = self.client.open(
            '/komoditas/pengemasan/{order_id}'.format(order_id='order_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_komoditas_pengiriman_order_id(self):
        """Test case for delete_komoditas_pengiriman_order_id

        
        """
        response = self.client.open(
            '/komoditas/pengiriman/{order_id}'.format(order_id='order_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_users_user_id(self):
        """Test case for delete_users_user_id

        
        """
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas(self):
        """Test case for get_komoditas

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_komoditas_id(self):
        """Test case for get_komoditas_komoditas_id

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/{komoditas_id}'.format(komoditas_id='komoditas_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pembuangan(self):
        """Test case for get_komoditas_pembuangan

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pembuangan',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pembuangan_order_id(self):
        """Test case for get_komoditas_pembuangan_order_id

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pembuangan/{order_id}'.format(order_id='order_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pemesanan(self):
        """Test case for get_komoditas_pemesanan

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pemesanan',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pemesanan_order_id(self):
        """Test case for get_komoditas_pemesanan_order_id

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pemesanan/{order_id}'.format(order_id='order_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pengemasan(self):
        """Test case for get_komoditas_pengemasan

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pengemasan',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pengemasan_order_id(self):
        """Test case for get_komoditas_pengemasan_order_id

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pengemasan/{order_id}'.format(order_id='order_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pengiriman(self):
        """Test case for get_komoditas_pengiriman

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pengiriman',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_komoditas_pengiriman_order_id(self):
        """Test case for get_komoditas_pengiriman_order_id

        Your GET endpoint
        """
        response = self.client.open(
            '/komoditas/pengiriman/{order_id}'.format(order_id='order_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        Your GET endpoint
        """
        response = self.client.open(
            '/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_user_id(self):
        """Test case for get_users_user_id

        Your GET endpoint
        """
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_komoditas(self):
        """Test case for post_komoditas

        
        """
        body = Komoditas()
        response = self.client.open(
            '/komoditas',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_komoditas_pembuangan(self):
        """Test case for post_komoditas_pembuangan

        
        """
        body = Pembuangan()
        response = self.client.open(
            '/komoditas/pembuangan',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_komoditas_pemesanan(self):
        """Test case for post_komoditas_pemesanan

        
        """
        body = Pemesanan()
        response = self.client.open(
            '/komoditas/pemesanan',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_komoditas_pengemasan(self):
        """Test case for post_komoditas_pengemasan

        
        """
        body = Pengemasan()
        response = self.client.open(
            '/komoditas/pengemasan',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_komoditas_pengiriman(self):
        """Test case for post_komoditas_pengiriman

        
        """
        body = Pengiriman()
        response = self.client.open(
            '/komoditas/pengiriman',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_users(self):
        """Test case for post_users

        
        """
        body = Pengguna()
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_komoditas_komoditas_id(self):
        """Test case for put_komoditas_komoditas_id

        
        """
        body = Komoditas()
        response = self.client.open(
            '/komoditas/{komoditas_id}'.format(komoditas_id='komoditas_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_komoditas_pemesanan_order_id(self):
        """Test case for put_komoditas_pemesanan_order_id

        
        """
        body = Pemesanan()
        response = self.client.open(
            '/komoditas/pemesanan/{order_id}'.format(order_id='order_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_komoditas_pengemasan_order_id(self):
        """Test case for put_komoditas_pengemasan_order_id

        
        """
        body = Pengemasan()
        response = self.client.open(
            '/komoditas/pengemasan/{order_id}'.format(order_id='order_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_komoditas_pengiriman_order_id(self):
        """Test case for put_komoditas_pengiriman_order_id

        
        """
        body = Pengiriman()
        response = self.client.open(
            '/komoditas/pengiriman/{order_id}'.format(order_id='order_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_users_user_id(self):
        """Test case for put_users_user_id

        
        """
        body = Pengguna()
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
