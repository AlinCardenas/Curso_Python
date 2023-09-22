from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Order import Order
from computer import Computer

teclado = Keyboard('USB', 'Hp')
mouse = Mouse('USB', 'Samsung')
monitor = Monitor('VGA', '1')
computadora = Computer('Computadora', monitor, teclado, mouse)
teclado2 = Keyboard('USB', 'Samsung')
mouse2 = Mouse('USB', 'HP')
monitor2 = Monitor('VGA', '1')
computadora2 = Computer('Computadora', monitor2, teclado2, mouse2)
computadoras = computadora, computadora2
order = Order(computadoras)
print(order)