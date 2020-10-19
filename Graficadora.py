from graphviz import Digraph
from Graph import Graph
from pathlib import Path
import os

class Graficadora:

	def __init__(self, grafo:Graph):
		self.dot = Digraph(comment='Mesa redonda', engine='dot', format='svg'
						   , graph_attr={'rankdir': 'LR','splines':'ortho'}  #'splines': 'ortho'
						   , node_attr={'shape': 'plaintext'}
						   , edge_attr={'arrowhead': 'none', 'color': 'maroon','arrowsize':'.5','weight':'2.'}

						   )
		self.grafo = grafo
		self.NodosVisitados:list = []
		self.flechas:list = []

		self.directory = "ReporteGrafo"
		self.basedir = Path(__file__).resolve().parent.parent
		pass

	def graficar(self):
		matriz = self.grafo.matriz
		nodeinit = matriz[0]
		self.dot.node(nodeinit.fila,self.newNode(nameNode=nodeinit.fila))
		self.recorrerGrafo(0)
		direccion =  os.path.join(self.basedir,self.directory)+"/Pert.gv"
		print(direccion)
		self.dot.render(direccion, view=True)


	def recorrerGrafo(self,fila):
		matriz = self.grafo.matriz
		size = self.grafo.size
		for j in range(size):
			pos = self.grafo.pos(fila,j)
			estado = matriz[pos].kernel.estado
			if estado == 1:
				self.createNode(matriz[pos])
				self.recorrerGrafo(j)

	def createNode(self,node):
		# print(self.dot.source)

		checkNode = node.col in self.NodosVisitados
		checkFlecha = node.fila+node.col in self.flechas
		if checkNode == False:
			self.NodosVisitados.append(node.col)

			self.dot.node(node.col,label=self.newNode(
				nameNode=node.kernel.name,
				tiempo = node.kernel.tiempo,
				inicioTemprano = node.kernel.inicioTemprano,
				terminacionTemprana = node.kernel.terminacionTemprana,
				inicioTardio = node.kernel.inicioTardio,
				terminacionTardia = node.kernel.terminacionTardia,
				holgura = node.kernel.holgura
			))

		if checkFlecha == False:

			self.flechas.append(node.fila+node.col)
			if node.kernel.holgura == 0:
				self.dot.edge(node.fila, node.col,color='green')
			else:
				self.dot.edge(node.fila, node.col)

	def newNode(self, nameNode='', tiempo=0, inicioTemprano=0, terminacionTemprana=0, inicioTardio=0,
				terminacionTardia=0, holgura=0):

		return f'''<<TABLE border='0' cellborder='1' cellspacing='0'> 
      		<tr>
        	<td align='left'><b>{inicioTemprano}</b></td>
        	<td align='left'><b>{tiempo}</b></td>
        	<td align='left'><b>{terminacionTemprana}</b></td>
      		</tr>
      		<tr>
        	<td align='center' colspan='3' BGCOLOR='gray'>{nameNode}</td>
      		</tr>
      		<tr>
        	<td align='left'><font color='darkgreen'>{inicioTardio}</font></td>
        	<td align='left' BGCOLOR='cyan'><font color='darkgreen'>{holgura}</font></td>
        	<td align='left'><font color='darkgreen'>{terminacionTardia}</font></td>
      		</tr> 
  			</TABLE>>'''