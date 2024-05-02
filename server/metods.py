import random
import redis

class NameServerService:
    def test(self):
        response="¡Connection done!"
        return(response)

class Service_Users:
    
    def search_user(self, id):
        valor = self.r.get(id)
        if valor is None:
            return (-1)
        else:
            return valor