class Node:

	def __init__(self,fila= "",col="",name="",tiempo=0,inicioTemprano=0,terminacionTemprana=0,inicioTardio=0,terminacionTardia=0,holgura=0,estado = 0):
		self.fila = str(fila)
		self.col = str(col)
		self.kernel = Kernel(name,tiempo,inicioTemprano,terminacionTemprana,inicioTardio,terminacionTardia,holgura,estado)

	def print(self):
		# print('['+self.name+','+str(self.estado)+']')
		print('('+self.fila+' , '+self.col+')',end="")

class Kernel:
	def __init__(self,name="",tiempo=0,inicioTemprano=0,terminacionTemprana=0,inicioTardio=0,terminacionTardia=0,holgura=0,estado = 0):
		self.name = str(name).replace(" ","") #quitando espacios en blanco
		self.tiempo = tiempo
		self.inicioTemprano = inicioTemprano
		self.terminacionTemprana = terminacionTemprana
		self.inicioTardio = inicioTardio
		self.terminacionTardia = terminacionTardia
		self.holgura = holgura
		self.estado = estado

	def equals(self,name):
		if self.name == name:
			return  True
		return  False

	def print(self):
		# print('['+self.name+','+str(self.estado)+','+str(self.tiempo)+']',end='')
		print('['+self.name+','+str(self.tiempo)+']',end='')



class NodeTemp:

	def __init__(self,activity:str,dependency:str,time:str):
		self.activity = activity
		self.dependency = dependency
		self.time  = int(time)

	def print(self):
		print('{'+self.activity+'|'+self.dependency+'|'+str(self.time)+'}',end='')


# if __name__ == "__main__":
# 	node1 = Node(name="esto es un id")
# 	node2 = node1
#
# 	print(node1.name)
# 	print(node2.name)
# 	node2.name = 'Cambiamos el nombre'
# 	print(node1.name)
# 	print(node2.name)
#
# 	if node1==node2:
# 		print('los Nodos son exactamente lo mismo')
# 	else:
# 		print('No son el mismo objeto')
#
