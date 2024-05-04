import random
import redis

class NameServerService:
    def __init__(self):
        self.status = 1

    def test(self):
        print(f"¡Hola estoy en Test!")
        return("Connected")

metods=NameServerService()     
