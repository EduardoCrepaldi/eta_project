from src.models.restaurant import Restaurant

""""
Para  todos os metodos da classe foi removido o Print, e colocado o Return.
"""


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """ Percorra a lista de sabores disponíveis e imprima."""
        """ Foi removido o FOR que printava e colocado o return da lista"""
        if self.flavors:
            return self.flavors
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """ Verifica se o sabor informado está disponível."""
        """ Foi removido o IF que verificava se tem Estoque, pois a ideia do método é verificar se existe o sabor pesquisado"""
        if flavor in self.flavors:
            return f"Temos no momento {flavor}!"  # Deveria ser flavor
        else:
            return f"Não temos no momento {flavor}!"  # Deveria ser flavor

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        """Inseri um novo IF para validar se o sabor passado é uma string e que não contém nenhum número"""
        if self.validate_flavor(flavor):
            if flavor in self.flavors:
                return "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Sabor Inválido"

    def validate_flavor(self, flavor):
        """Esse método tem como objetivo validar se o nome do sabor é string e também não tem nenhum número"""
        if type(flavor) == str and flavor.isalpha():
            return True
        return False
