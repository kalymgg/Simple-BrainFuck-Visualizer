# Simple BrainFuck Visualizer

Try out simple "Hello World!":

```bash
python3 bfMachine.py
```


## Usage

```python
from bfMachine import bfMachine as machine

code = '++++++[>++++++<-]>.'     #Your BF code

machine = bfMachine(code, 
verbose = True,     #True - visualize, False - execute with basic IO
delay=0.05,    #Delay between steps (in seconds)
clean = True)    #Clean screen after each step

machine.run()   #Execute
```