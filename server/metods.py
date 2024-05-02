import random
import redis

class NameServerService:
    def test(self, name):
        print("Hola " + name + " estoy en Test ")
        return('Connected')

class Service_Users:
    
    def search_user(self, id):
        valor = self.r.get(id)
        if valor is None:
            return (-1)
        else:
            return valor