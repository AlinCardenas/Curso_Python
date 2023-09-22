from computer import *
class Order:
    countOrders = 0
    def __init__(self, computers):
        Order.countOrders += 1
        self._idOrder = Order.countOrders
        self._computers = list(computers)
    @property
    def computers(self):
        return self._computers
    @computers.setter
    def computers(self,computers):
        self._computers = computers

    def add_computer(self, computer):
        self._computers.append(computer)

    def __str__(self):
        computers_str = ''
        for computer in self.computers:
            computers_str += computer.__str__()
        return  f'Orden:{self._idOrder} \n Computadoras: {computers_str}'
