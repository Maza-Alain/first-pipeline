import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_sumar(self):
        response = self.client.get('/sumar/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'La suma de 5 y 3 es: 8')

    def test_restar(self):
        response = self.client.get('/restar/10/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'La resta de 10 menos 4 es: 6')

    def test_multiplicar(self):
        response = self.client.get('/multiplicar/2/6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'El producto de 2 y 6 es: 12')

    def test_sumar_parametros_no_enteros(self):
        response = self.client.get('/sumar/a/b')
        self.assertEqual(response.status_code, 404)

    def test_ruta_invalida(self):
        response = self.client.get('/ruta_invalida')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
