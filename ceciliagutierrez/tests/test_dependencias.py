from unittest.mock import Mock

from dependencias.di_01 import ServicioPedidos, RepositorioBD

def test_crear_pedido_llama_guardar():

    mock_repo = Mock(spec=RepositorioBD)
    servicio = ServicioPedidos(mock_repo)
    servicio.crear_pedido("Hamburguesa")
    mock_repo.guardar.assert_called_once_with("Hamburguesa")