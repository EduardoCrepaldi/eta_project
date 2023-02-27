import pytest
from src.models.restaurant import Restaurant


class TestRestaurant:
    def setup_method(self):
        """Utilizando setup para instanciar o objeto de restaurant no qual vai ser utilizado em cada teste
        e também setando as variáveis restaurant_name e cuisine_type"""
        self.restaurant_name = "Restaurante do Zé"
        self.cuisine_type = "Self-Service"
        self.restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

    def teardown_method(self):
        """Utilizando o Teardown para zerar o objeto de IceCreamStand"""
        self.restaurant = None
        self.cuisine_type = None
        self.restaurant_name = None

    def test_describe_restaurant(self):
        # SETUP
        number_served = 0
        message = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.\nEsse restaurante está servindo {number_served} consumidores desde que está aberto."

        # CHAMADA
        result = self.restaurant.describe_restaurant()

        # AVALIACAO
        assert result == message

    def test_open_restaurant(self):
        # SETUP
        message = f"{self.restaurant_name} agora está aberto!"

        # CHAMADA
        result = self.restaurant.open_restaurant()

        # AVALIACAO
        assert self.restaurant.open is True
        assert result == message
        assert self.restaurant.number_served == 0

    def test_open_restaurant_is_open(self):
        # SETUP
        message = f"{self.restaurant_name} já está aberto!"

        # CHAMADA
        self.restaurant.open_restaurant()
        result = self.restaurant.open_restaurant()

        # AVALIACAO
        assert self.restaurant.open is True
        assert result == message

    def test_close_restaurant(self):
        # SETUP
        message = f"{self.restaurant_name} agora está fechado!"

        # CHAMADA
        self.restaurant.open_restaurant()  # Abrindo restaurante
        result = self.restaurant.close_restaurant()

        # AVALIACAO
        assert result == message
        assert self.restaurant.open is False
        assert self.restaurant.number_served == 0

    def test_close_restaurant_is_closed(self):
        # SETUP
        message = f"{self.restaurant_name} já está fechado!"

        # CHAMADA
        self.restaurant.open_restaurant()  # Abrindo restaurante
        self.restaurant.close_restaurant()
        result = self.restaurant.close_restaurant()

        # AVALIACAO
        assert result == message
        assert self.restaurant.open is False
        assert self.restaurant.number_served == 0

    def test_set_number_served(self):
        # SETUP
        number_served = 123
        self.restaurant.open_restaurant()  # Abrindo restaurante

        # CHAMADA
        result = self.restaurant.set_number_served(number_served)

        # AVALIACAO
        assert result == number_served

    def test_set_number_served_is_restaurant_closed(self):
        # SETUP
        number_served = 123
        message = f"{self.restaurant_name} está fechado!"
        # CHAMADA
        result = self.restaurant.set_number_served(number_served)

        # AVALIACAO
        assert result == message
        assert self.restaurant.number_served == 0

    def test_increment_number_served(self):
        # SETUP
        consumidores = 123
        increment = 10
        message = consumidores + increment
        self.restaurant.open_restaurant()  # Abrindo restaurante
        self.restaurant.set_number_served(consumidores)

        # CHAMADA
        result = self.restaurant.increment_number_served(increment)

        # AVALIACAO
        assert result == message

    def test_increment_number_served_is_restaurant_closed(self):
        # SETUP
        increment = 12
        message = f"{self.restaurant_name} está fechado!"
        self.restaurant.open_restaurant()
        self.restaurant.set_number_served(15)
        self.restaurant.increment_number_served(10)
        self.restaurant.close_restaurant()

        # Chamada
        result = self.restaurant.increment_number_served(increment)

        # Avaliação
        assert result == message

    @pytest.mark.parametrize('value, message', [(1, True), ("Edu", False), (-3, False), (3.25, False)])
    def test_validate_int(self, value, message):
        # Chamada
        result = self.restaurant.validate_int(value)

        # Avaliação
        assert result is message
