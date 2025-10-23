from  src.ejercicio_unitarias import Cliente

def test_validar_email_success():
    # Arrange
    email_valido = "email@test.com"

    #Llamada
    cliente_test = Cliente("Cecilia", email_valido)

    assert cliente_test.validar_email() is True