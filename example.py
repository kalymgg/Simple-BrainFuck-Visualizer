from bfMachine import bfMachine as machine

code = '>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++.'

machine = bfMachine(code, verbose = True, delay=0.05, clean = True)

machine.run()