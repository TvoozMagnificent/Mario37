
import sys
try: source_file = sys.argv[1]
except: print('Mario37 is confused. ERROR'); sys.exit()
if '-d' in sys.argv: debug = True
else: debug = False
if '-d' in sys.argv and len(sys.argv)>3 or '-d' not in sys.argv and len(sys.argv)>2: print('Mario37 ate garbage. ERROR')

try:
    with open(source_file, 'r') as f: lines = f.read().lstrip('\n').rstrip().split('\n')
except: print('Mario37 cannot find his instructor. ERROR'); sys.exit()
source_code = [line.rstrip() for line in lines]
max_line_length = max(map(len,source_code))
filled_source_code = [line.ljust(max_line_length) for line in source_code]
matrix = [*map(list,filled_source_code)]

instruction_pointer = [0,0]
direction = 'right'
stack = []

def get_instruction(matrix, instruction_pointer):
    try: return matrix[instruction_pointer[1]][instruction_pointer[0]]
    except: return ' '

def add(array1,array2): return [array1[i]+array2[i] for i in range(len(array1))]

try:
    while -1<=instruction_pointer[0]<=len(matrix[0]) and 0<=instruction_pointer[1]<=len(matrix):
        instr = get_instruction(matrix,instruction_pointer)
        if instr == ' ': pass
        elif instr == '0': stack.append(37)
        elif instr == '+': stack.append(stack.pop()+stack.pop())
        elif instr == '-': stack.append(stack.pop()-stack.pop())
        elif instr == '*': stack.append(stack.pop()*stack.pop())
        elif instr == '/': stack.append(stack.pop()/stack.pop())
        elif instr == '%': stack.append(stack.pop()%stack.pop())
        elif instr == '^': stack.append(stack.pop()**stack.pop())
        elif instr == '!': stack.append(int(stack.pop()!=stack.pop()))
        elif instr == '<': stack.append(int(stack.pop()< stack.pop()))
        elif instr == '>': stack.append(int(stack.pop()> stack.pop()))
        elif instr == '=': stack.append(int(stack.pop()==stack.pop()))
        elif instr == 's': a=stack.pop(); b=stack.pop(); stack.append(a); stack.append(b)
        elif instr == 'v': stack=[stack.pop()]+stack
        elif instr == 'x': stack.pop()
        elif instr == 'd': a=stack.pop(); stack.append(a); stack.append(a)
        elif instr == 'c': stack.append(chr(int(stack.pop())))
        elif instr == 'o': stack.append(ord(stack.pop()))
        elif instr == 'z':
            for i in stack.pop()[::-1]: stack.append(i)
        elif instr == 'r': stack.append(stack.pop()[::-1])
        elif instr == 'i': stack.append(input('Mario37 needs your help. '))
        elif instr == 'p': print(stack.pop())
        elif instr == 'n': stack.append(int(input('Mario37 needs your assistance. ')))
        elif instr == '[': direction = 'left'
        elif instr == ']': direction = 'right'
        elif instr == 't': instruction_pointer = [instruction_pointer[0],-1]
        elif instr == 'a': stack.append(int(stack.pop()))
        elif instr == 'b': stack.append(str(stack.pop()))
        elif instr == 'e': stack.append(int(type(stack.pop())==int))
        elif instr == 'f':
            if stack.pop() == ' ': instruction_pointer = [instruction_pointer[0],-1]
            else: instruction_pointer = add(instruction_pointer, [1 if direction == 'right' else -1, 0]); continue
        elif instr == 'l': stack.append(len(stack.pop()))
        elif instr == '_': print('Mario37 suffocated. ERROR'); break
        else: print('Mario37 didn\'t know what to do. ERROR'); break
        if get_instruction(matrix,add(instruction_pointer,[0,1]))!='_': instruction_pointer = add(instruction_pointer,[0,1])
        else: instruction_pointer = add(instruction_pointer,[1 if direction=='right' else -1,0])
        if debug:print(instruction_pointer); print(stack)

except IndexError: print('Mario37 tried to generate something out of nothing. ERROR')
except KeyboardInterrupt: print('Mario37 was stopped by a villain. ERROR')
except TypeError: print('Mario37 tried to mix salad and sandwitches. ERROR')
except OverflowError: print('Mario37 filled up his backpack. ERROR')
except ValueError: print('Mario37 dealed with drugs. ERROR')
except ZeroDivisionError: print('Mario37 didn\'t learn math. ERROR')
except: print('Mario37 died. ERROR')

sys.exit()

