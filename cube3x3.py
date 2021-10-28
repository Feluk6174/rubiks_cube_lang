import random

class cube():
	def __init__(self):
		self.colors = ["o", "w", "r", "y", "g", "b"]
		self.cube = {}
		for color in self.colors:
			self.cube[color] = {}
			self.cube[color]["edge"] = [color for i in range(4)]
			self.cube[color]["corner"] = [color for i in range(4)]
			self.cube[color]["face"] = [color for i in range(8)]
			
		self.moves = ["u", "u'", "u2", "r", "r'", "r2", "l", "l'", "l2", "d", "d'", "d2", "f", "f'", "f2", "b", "b'", "b2"]
			
		#self.cube["w"]["corner"] = [1, 3, 5, 7]
		#self.cube["w"]["edge"] = [2, 4, 6, 8]
			
	def __str__(self):
		return f"""      {self.cube["b"]["corner"][2]} {self.cube["b"]["edge"][2]} {self.cube["b"]["corner"][3]}
      {self.cube["b"]["edge"][1]} b {self.cube["b"]["edge"][3]}
      {self.cube["b"]["corner"][1]} {self.cube["b"]["edge"][0]} {self.cube["b"]["corner"][0]}
{self.cube["o"]["corner"][3]} {self.cube["o"]["edge"][3]} {self.cube["o"]["corner"][0]} {self.cube["w"]["corner"][0]} {self.cube["w"]["edge"][0]} {self.cube["w"]["corner"][1]} {self.cube["r"]["corner"][1]} {self.cube["r"]["edge"][1]} {self.cube["r"]["corner"][2]} {self.cube["y"]["corner"][2]} {self.cube["y"]["edge"][2]} {self.cube["y"]["corner"][3]} 
{self.cube["o"]["edge"][2]} o {self.cube["o"]["edge"][0]} {self.cube["w"]["edge"][3]} w {self.cube["w"]["edge"][1]} {self.cube["r"]["edge"][0]} r {self.cube["r"]["edge"][2]} {self.cube["y"]["edge"][1]} y {self.cube["y"]["edge"][3]}
{self.cube["o"]["corner"][2]} {self.cube["o"]["edge"][1]} {self.cube["o"]["corner"][1]} {self.cube["w"]["corner"][3]} {self.cube["w"]["edge"][2]} {self.cube["w"]["corner"][2]} {self.cube["r"]["corner"][0]} {self.cube["r"]["edge"][3]} {self.cube["r"]["corner"][3]} {self.cube["y"]["corner"][1]} {self.cube["y"]["edge"][0]} {self.cube["y"]["corner"][0]} 
      {self.cube["g"]["corner"][0]} {self.cube["g"]["edge"][0]} {self.cube["g"]["corner"][1]}
      {self.cube["g"]["edge"][3]} g {self.cube["g"]["edge"][1]}
      {self.cube["g"]["corner"][3]} {self.cube["g"]["edge"][2]} {self.cube["g"]["corner"][2]}
      """
			
	def turn_face(self, face:str):
		self.cube[face]["edge"] = [self.cube[face]["edge"][3], self.cube[face]["edge"][0], self.cube[face]["edge"][1], self.cube[face]["edge"][2]]
		self.cube[face]["corner"] = [self.cube[face]["corner"][3], self.cube[face]["corner"][0], self.cube[face]["corner"][1], self.cube[face]["corner"][2]]
							
							
	def turn_side(self, face:str, info:list):
		self.turn_face(face)
		
		temp1 = [self.cube[info[0]["color"]]["corner"][info[0]["nums"][0]], self.cube[info[0]["color"]]["edge"][info[0]["nums"][1]], self.cube[info[0]["color"]]["corner"][info[0]["nums"][2]]]
		
		temp2 = [self.cube[info[2]["color"]]["corner"][info[2]["nums"][0]], self.cube[info[2]["color"]]["edge"][info[2]["nums"][1]], self.cube[info[2]["color"]]["corner"][info[2]["nums"][2]]]
		
		
		self.cube[info[0]["color"]]["corner"][info[0]["nums"][0]] = self.cube[info[3]["color"]]["corner"][info[3]["nums"][0]]
		self.cube[info[0]["color"]]["edge"][info[0]["nums"][1]] = self.cube[info[3]["color"]]["edge"][info[3]["nums"][1]]
		self.cube[info[0]["color"]]["corner"][info[0]["nums"][2]] = self.cube[info[3]["color"]]["corner"][info[3]["nums"][2]]
		
		self.cube[info[2]["color"]]["corner"][info[2]["nums"][0]] = self.cube[info[1]["color"]]["corner"][info[1]["nums"][0]]
		self.cube[info[2]["color"]]["edge"][info[2]["nums"][1]] = self.cube[info[1]["color"]]["edge"][info[1]["nums"][1]]
		self.cube[info[2]["color"]]["corner"][info[2]["nums"][2]] = self.cube[info[1]["color"]]["corner"][info[1]["nums"][2]]
		
		self.cube[info[1]["color"]]["corner"][info[1]["nums"][0]] = temp1[0]
		self.cube[info[1]["color"]]["edge"][info[1]["nums"][1]] = temp1[1]
		self.cube[info[1]["color"]]["corner"][info[1]["nums"][2]] = temp1[2]
		
		self.cube[info[3]["color"]]["corner"][info[3]["nums"][0]] = temp2[0]
		self.cube[info[3]["color"]]["edge"][info[3]["nums"][1]] = temp2[1]
		self.cube[info[3]["color"]]["corner"][info[3]["nums"][2]] = temp2[2]
		
	
	def u(self):
		d = [{"color": "g", "nums": [0, 0, 1]}, {"color": "o", "nums": [0, 0, 1]}, {"color": "b", "nums": [0, 0, 1]}, {"color": "r", "nums": [0, 0, 1]}, ]
		
		self.turn_side("w", d)
		
		
	def f(self):
		d = [{"color": "w", "nums": [3, 2, 2]}, {"color": "r", "nums": [0, 3, 3]}, {"color": "y", "nums": [1, 0, 0]}, {"color": "o", "nums": [2, 1, 1]}, ]
		
		self.turn_side("g", d)
		
		
	def r(self):
		d = [{"color": "w", "nums": [2, 1, 1]}, {"color": "b", "nums": [0, 3, 3]}, {"color": "y", "nums": [2, 1, 1]}, {"color": "g", "nums": [2, 1, 1]}, ]
		
		self.turn_side("r", d)
		
	
	def d(self):
		d = [{"color": "g", "nums": [3, 2, 2]}, {"color": "r", "nums": [3, 2, 2]}, {"color": "b", "nums": [3, 2, 2]}, {"color": "o", "nums": [3, 2, 2]}, ]
		
		self.turn_side("y", d)
		

	def l(self):
		d = [{"color": "w", "nums": [0, 3, 3]}, {"color": "g", "nums": [0, 3, 3]}, {"color": "y", "nums": [0, 3, 3]}, {"color": "b", "nums": [2, 1, 1]}, ]
		
		self.turn_side("o", d)
		
		
	def b(self):
		d = [{"color": "w", "nums": [0, 0, 1]}, {"color": "o", "nums": [0, 3, 3]}, {"color": "y", "nums": [3, 2, 2]}, {"color": "r", "nums": [2, 1, 1]}, ]
		
		self.turn_side("b", d)

	
	def move(self, move):
		if move == "u":
			self.u()
		if move == "u'":
			self.u()
			self.u()
			self.u()
		if move == "u2":
			self.u()
			self.u()
		
		if move == "f":
			self.f()
		if move == "f'":
			self.f()
			self.f()
			self.f()
		if move == "f2":
			self.f()
			self.f()
			
		if move == "r":
			self.r()
		if move == "r'":
			self.r()
			self.r()
			self.r()
		if move == "r2":
			self.r()
			self.r()
			
		if move == "l":
			self.l()
		if move == "l'":
			self.l()
			self.l()
			self.l()
		if move == "l2":
			self.l()
			self.l()
		
		if move == "d":
			self.d()
		if move == "d'":
			self.d()
			self.d()
			self.d()
		if move == "d2":
			self.d()
			self.d()
		
		if move == "b":
			self.b()
		if move == "b'":
			self.b()
			self.b()
			self.b()
		if move == "b2":
			self.b()
			self.b()

	def scramble(self, scramble:str=""):
		if scramble != "":
			pass
		else:
			for i in range(40):
				x = random.randint(0,17)
				self.move(self.moves[x])
