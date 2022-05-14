from bfMachine import bfMachine as machine

code = '>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++.'

machine = machine(code, verbose = True, delay=0.05, clean = True)

machine.run()
