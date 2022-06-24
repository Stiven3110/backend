class carro ():

	def __init__(marca, serie, modelo):
		self.marca = marca
		self.serie = serie
		self.modelo = modelo

class camion ():
	def __init__(marca, serie, modelo, ejes):
		self.marca = marca
		self.serie = serie
		self.modelo = modelo
		self.ejes = ejes

class camion (carro):
	def __init__(ejes):
		self.ejes = ejes