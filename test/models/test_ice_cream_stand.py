import pytest
from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    """Utilizando setup para instanciar o objeto de ice_cream no qual vai ser utilizado em cada teste
       e também setando as variáveis restaurant_name e cuisine_type"""
    def setup_method(self):
        # SETUP
        self.restaurant_name = "SorveAçai"
        self.cuisine_type = "Sorveteria e Açai"
        self.flavors_list = ["Abacaxi", "Limão", "Nutella"]
        self.ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

    """Utilizando o Teardown para zerar o objeto de IceCreamStand"""
    def teardown_method(self):
        self.ice_cream = None
    def test_flavors_available_OK(self):
        """"Validando a listagem de sabores retornada pelo método flavors_available"""
        # Chamada
        result = self.ice_cream.flavors_available()

        # Validação
        assert result == self.flavors_list

    def test_flavors_available_out_of_stock(self):
        """"Validando retorno de mensagem sem estoque pelo método flavors_available"""
        # Setup
        flavors_list = []
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, flavors_list)
        message = "Estamos sem estoque atualmente!"

        # Chamada
        result = ice_cream.flavors_available()

        # Validação
        assert result == message
        assert ice_cream.flavors == flavors_list

    @pytest.mark.parametrize('search_flavor', ["Limão", "Nutella", "Abacaxi"])
    def test_find_flavor(self, search_flavor):
        """"Validando se o método Find_Flavor retorna sucesso ao pesquisar um sabor existente"""
        """"Foi utilizado a parametrização no qual valido todos os sabores do meu setup"""
        # Setup
        message = f"Temos no momento {search_flavor}!"

        # Chamada
        result = self.ice_cream.find_flavor(search_flavor)

        # Avaliação
        assert result == message

    def test_find_flavor_there_is_no_flavor(self):
        """"Validando se o método Find_Flavor está validando quando o sabor não existe na listagem"""
        # Setup
        search_flavor = "Cupuaçu"
        message = f"Não temos no momento {search_flavor}!"

        # Chamada
        result = self.ice_cream.find_flavor(search_flavor)

        # Avaliação
        assert result == message

    def test_find_flavor_out_of_stock(self):
        """"Validando se o método Find_Flavor está validando quando a listagem de sabores é vazio e um sabor é buscado"""
        # Setup
        flavors_list = []
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, flavors_list)
        search_flavor = "Cupuaçu"
        message = f"Não temos no momento {search_flavor}!"

        # Chamada
        result = ice_cream.find_flavor(search_flavor)

        # Avaliação
        assert result == message
        assert ice_cream.flavors == flavors_list

    def test_add_flavor(self):
        """"Validando se o método add_flavor está inserindo corretamente um novo sabor"""

        # Setup
        new_flavor = "Cupuaçu"
        message = f"{new_flavor} adicionado ao estoque!"

        # CHAMADA
        result = self.ice_cream.add_flavor(new_flavor)

        # AVALIACAO
        assert result == message
        assert self.ice_cream.flavors[3] == new_flavor

    def test_add_flavor_with_list_empty(self):
        """"Validando se o método add_flavor está inserindo corretamente um novo sabor em uma lista vazia"""

        # SETUP
        flavors_list = []
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, flavors_list)
        new_flavor = "Cupuaçu"
        message = f"{new_flavor} adicionado ao estoque!"

        # CHAMADA
        result = ice_cream.add_flavor(new_flavor)

        # AVALIACAO
        assert result == message
        assert ice_cream.flavors[0] == new_flavor

    def test_add_flavor_existing_flavor(self):
        # SETUP
        new_flavor_existing = "Limão"
        message = "Sabor já disponivel!"

        # CHAMADA
        result = self.ice_cream.add_flavor(new_flavor_existing)

        # AVALIACAO
        assert result == message

    def test_add_flavor_invalid_flavor(self):
        # SETUP
        new_flavor_existing = "33243"
        message = "Sabor Inválido"

        # CHAMADA
        result = self.ice_cream.add_flavor(new_flavor_existing)

        # AVALIACAO
        assert result == message

    @pytest.mark.parametrize('flavor, validate',
                             [("Nata", True), ("Nata22", False), (2.5, False),
                              (3, False), (["lista"], False), (True, False)])
    def test_validate_flavor(self, flavor, validate):
        # Chamada
        result = self.ice_cream.validate_flavor(flavor)

        # Validação
        assert result == validate
