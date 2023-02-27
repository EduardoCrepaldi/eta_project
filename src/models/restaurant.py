""""
Para  todos os metodos da classe foi removido o Print, e colocado o Return.
"""

class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # removendo o title, no qual coloca todas as primeiras letras
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # print(f"Esse restaturante chama {self.cuisine_type} e serve {self.cuisine_type}.") ## Primeira instancia errada
        # print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

        return f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}." \
               f"\nEsse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True  # Ajustando para TRUE pois o restaurante instancia como FALSE
            self.number_served = 0  # AJUSTANDO PARA 0, estava com -2
            return f"{self.restaurant_name} agora está aberto!"  # Removendo o print e colocando RETURN
        else:
            return f"{self.restaurant_name} já está aberto!"  # Removendo o print e colocando RETURN

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"  # Removendo o print e colocando RETURN
        else:
            return f"{self.restaurant_name} já está fechado!"  # Removendo o print e colocando RETURN

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.validate_int(total_customers) and self.open:
            self.number_served = total_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers  # self.number_served = self.number_served + more_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"

    def validate_int(self, value):
        """Método para validar se o valor passado é inteiro e maior que zero."""
        if type(value) == int and value > 0:
            return True
        return False
