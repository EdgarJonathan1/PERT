from Node import NodeTemp
from Node import Node
from Node import Kernel

class Graph:
	def __init__(self, content):
		# self.matrix = self.build(content)
		self.fin:int
		# self.nodoFin:Node
		self.matriz:Node
		self.size:int
		self.build(content)
		self.calcRuta()

	def calcRuta(self):
		self.recorrerGrafoIda(0,0)
		self.recorrerGrafoVuelta(self.size-1,self.fin)
		self.tourHolgura(0)

	def tourHolgura(self,fila:int):
		for col in range(self.size):
			pos = self.pos(fila,col)
			estado = self.matriz[pos].kernel.estado
			if estado == 1:
				self.calcHolgura(self.matriz[pos])
				self.tourHolgura(col)


	def calcHolgura(self,node:Node):
		inicioTemprano = node.kernel.inicioTemprano
		inicioTardio = node.kernel.inicioTardio
		holgura = inicioTardio - inicioTemprano
		node.kernel.holgura = holgura

	def recorrerGrafoVuelta(self,col,fin):
		for fila in range(self.size):
			pos = self.pos(fila,col)
			estado = self.matriz[pos].kernel.estado
			if estado == 1:
				self.calcCostoVuelta(self.matriz[pos],fin)
				inicioTardio = self.matriz[pos].kernel.inicioTardio
				self.recorrerGrafoVuelta(fila,inicioTardio)

	def calcCostoVuelta(selfi,node:Node,fin:int):
		finTardioActual = node.kernel.terminacionTardia
		if fin <= finTardioActual or finTardioActual == 0:
			inicioTardioActual = fin - node.kernel.tiempo
			node.kernel.inicioTardio = inicioTardioActual
			node.kernel.terminacionTardia =fin

	def recorrerGrafoIda(self,fila,inicio):
		for col in range(self.size):
			pos = self.pos(fila,col)
			estado = self.matriz[pos].kernel.estado
			if estado == 1:
				self.calcCostoIda(self.matriz[pos],inicio)
				terminacion = self.matriz[pos].kernel.terminacionTemprana
				self.recorrerGrafoIda(col,terminacion)

	def calcCostoIda(self, node:Node,inicio:int):
		inicioTempranoActual = node.kernel.inicioTemprano
		if inicio >= inicioTempranoActual :
			finTempranoActual = inicio + node.kernel.tiempo

			node.kernel.inicioTemprano = inicio
			node.kernel.terminacionTemprana = finTempranoActual

			self.fin = finTempranoActual
			# self.nodoFin = node


	def  pos(self,fila,col):
		return self.size*fila+col

	def getRowAndCol(self, name):
		for i in range(self.size):
			for j in range(self.size):
				fila = self.matriz[self.pos(i, j)].fila
				if fila == name:
					return i
		# return None

		pass
	def createMatriz(self,listNodeTemp):
		matriz = []
		for i in range(self.size):
			for j in range(self.size):
				fila_ = listNodeTemp[i].activity
				col_ = listNodeTemp[j].activity
				matriz.append(Node(fila=fila_,col=col_))

		return matriz

	def build(self,content:str):
		#Creamos una lista temporal para agrupar los datos
		listNodeTemp = self.fillListNodeTemp(content)
		# self.printTempListNode(listNodeTemp)

		#Creando la matriz que nos servira para el grafo
		self.size = len(listNodeTemp)
		self.matriz = self.createMatriz(listNodeTemp)
		# self.printNode()
		#Insertamos las intersecciones en la matriz
		self.setInterseccion(listNodeTemp)
		# self.printKernel()

	def fillListNodeTemp(self,content):
		listNodeTemp = []
		rows = content.split('\n')
		# quitamos el ultimo enter del archivo csv
		del rows[-1]

		# Creando la lista temporal
		for i in range(1, len(rows)):
			row = rows[i].split(';')
			listNodeTemp.append(NodeTemp(activity=row[0], dependency=row[1], time=row[2]))
		return  listNodeTemp

	def setInterseccion(self,listNodeTemp):
		for comp in listNodeTemp:
			dependencys = comp.dependency.split(',')
			for depend in dependencys:
				pos = self.getPos(depend, comp.activity)
				if pos != -1:
					self.matriz[pos].kernel.estado = 1
					self.matriz[pos].kernel.tiempo = comp.time

					#Busca si ya existe un kernel con el mismo nombre no crea uno nuevo si no que solo lo asigna
					kernel = self.searchKernel(comp.activity)
					if kernel != None:
							self.matriz[pos].kernel = kernel
					else:
						self.matriz[pos].kernel.name = comp.activity

	def searchKernel(self,name):
		for i in range(self.size):
			for j in range(self.size):
				kernel = self.matriz[self.pos(i, j)].kernel
				temp  = kernel.equals(name)
				if temp == True:
					return kernel
		# return None

	def getPos(self, fila_:str, col_:str):
		for i in range(self.size):
			for j in range(self.size):
				fila = self.matriz[self.pos(i, j)].fila
				col = self.matriz[self.pos(i, j)].col
				if fila_==fila and col_==col:
					return self.pos(i,j)
		return -1

	def printTempListNode(self,listNodeTemp):
		for x in listNodeTemp:
			x.print()
		print('')

	def printKernel(self):
		for i in range(self.size):
			for j in range(self.size):
				self.matriz[self.pos(i,j)].kernel.print()
			print("")



	def printNode(self):
		for i in range(self.size):
			for j in range(self.size):
				self.matriz[self.pos(i,j)].print()
			print("")

