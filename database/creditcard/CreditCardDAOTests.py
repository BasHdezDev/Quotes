
#Todas las prueba unitarias importan la biblioteca unittest
import unittest

import creditcardDAO 
import creditCardTableDTO 


class ControllerTest(unittest.TestCase):
    """
        Pruebas a la Clase Controlador de la aplicación
    """

    def testCreatetable(self):
        """
        Verifica que se crea una tabla en la base de datos correctamente
        """

        # 1. Create table 
        creditcardDAO.CreateTable()


    def testInsert1(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear un usuario

        card_test = creditCardTableDTO.creditCardTableDTO( "556677", "1010123456", "Comprador compulsivo", "Bancolombia", "31/12/2027", "VISA", "10", "24000","3.1") 

        try:
            self.assertRaises(Exception,creditcardDAO.Insertar, card_test)
        except:
            creditcardDAO.Insertar(card_test)

    def testInsert2(self):
        """ Verfica que no deje guardar las tarjetas que ya estén vencidas"""

        card_test = creditCardTableDTO.creditCardTableDTO( "442233", "1010123456", "Comprador compulsivo", "Popular", "31/12/2022", "Mastercard", "5", "34000","3.4") 

        creditcardDAO.is_expired(card_test)

    def testInsert3(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear un usuario

        card_test = creditCardTableDTO.creditCardTableDTO( "556677", "1020889955", "Estudiante Pelao", "Bancolombia", "31/12/2027", "VISA", "10", "24000","3.1") 

        try:
            self.assertRaises(Exception,creditcardDAO.Insertar, card_test)
            print("La tarjeta de crédito ya existe")
        except:
            creditcardDAO.Insertar(card_test)

# Este fragmento de codigo permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()