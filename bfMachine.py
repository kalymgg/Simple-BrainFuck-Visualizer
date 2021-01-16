from time import sleep
import os


class bfMachine(object):
	def __init__(self, codeTape, verbose = False, delay = 0, clean = False):
		self.tape = [0]
		self.codeTapePointer = 0
		self.cellPointer = 0
		self.loopStack = {}
		self.codeTape = codeTape
		self.verbose = verbose
		self.delay = delay
		self.input = ''
		self.output = ''
		self.clean = clean

	#converting [] loops into stack for further execution
	def compileloopStack(self):
		stackBuffer = []
		for position, command in enumerate(self.codeTape):
			if command == "[": 
				stackBuffer.append(position)
			if command == "]":
				start = stackBuffer.pop()
				self.loopStack[start] = position
				self.loopStack[position] = start
		return self.loopStack

	def cellIncrement(self):
		self.tape[self.cellPointer] = (self.tape[self.cellPointer] + 1)%256 #Incrementing cell value. Simulates 8 bit intager overflow

	def cellDecrement(self):
		self.tape[self.cellPointer] = (self.tape[self.cellPointer] - 1)%256 #Incrementing cell value. Simulates 8 bit intager overflow

	def cellPointerIncrement(self):
		self.cellPointer+=1 #Too obvious to explain

	def cellPointerDecrement(self):
		self.cellPointer=(self.cellPointer-1)%(self.cellPointer+1) #Same, but protected from turning negative. Why so complicated? Cause math rules and if statements suck

	def loopBegin(self):
		if self.tape[self.cellPointer] == 0: self.codeTapePointer = self.loopStack[self.codeTapePointer] #Ok, I know what it looks like, but I just couldn't avoid if statement here

	def loopEnd(self):
		if self.tape[self.cellPointer] != 0: self.codeTapePointer = self.loopStack[self.codeTapePointer] #And here

	def cellValueOutput(self):
		print(chr(self.tape[self.cellPointer]), end='')
		self.output+=chr(self.tape[self.cellPointer])

	def cellValueInput(self):
		self.tape[self.cellPointer] = ord(input())
		self.input+=f' {self.tape[self.cellPointer]}'

	def run(self):
		#Binding commands to functions. Lets me avoid A LOT of if statements
		self.commandDictionary = {'+': self.cellIncrement, '-': self.cellDecrement, '>': self.cellPointerIncrement, '<': self.cellPointerDecrement,
							 	  '.': self.cellValueOutput, ',': self.cellValueInput, '[': self.loopBegin, ']': self.loopEnd}

		self.loopStack = self.compileloopStack()
		while self.codeTapePointer < len(self.codeTape):

			#For visualizing purposes
			if self.delay:
				sleep(self.delay)
			
			if self.clean: os.system('cls' if os.name == 'nt' else 'clear')

			if self.verbose:
				print(f'Code: {self.codeTape}\n      {" "*self.codeTapePointer}^\nMemory: {self.tape}\n        {"    "*self.cellPointer+1*" "}^\nInput: {self.input}\nOutput: {self.output}')	
			#For visualizing purposes

			self.command = self.codeTape[self.codeTapePointer] #current command

			self.commandDictionary[self.command]() #Execute command
			
			self.tape.extend([0]*(self.cellPointer+1-len(self.tape))) #dynamically expanding storage when needed
		
			self.codeTapePointer += 1 #jump to the next command

		print('')



#here you can play around
if __name__ == '__main__':

	code = '++++++[>++++++<-]>.'
	
	machine = bfMachine(code, verbose = True, delay=0.05, clean = True)

	machine.run()