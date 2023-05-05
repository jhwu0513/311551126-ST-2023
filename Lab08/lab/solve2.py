# Put bit vectors in th stack to find out the vallue that stack position need to 
# have to reach a rogram flow

import angr
import claripy
import sys

project = angr.Project('./src/prog', load_options={'auto_load_libs': False})

# Go to some address after the scanf where values have already being set in the stack
start_address = 0x8048697
initial_state = project.factory.blank_state(addr=start_address)

# Since we are starting after scanf, we are skipping this stack construction
# step. To make up for this, we need to construct the stack ourselves. Let us
# start by initializing ebp in the exact same way the program does.
initial_state.regs.ebp = initial_state.regs.esp

# In this case scanf("%u %u") is used, so 2 BVS are going to be needed
pwd = [claripy.BVS('password{i}', 32) for i in range(15)]


# Now, in the address were you have stopped, check were are the scanf values saved
# Then, substrack form the esp registry the needing padding to get to the
# part of the stack were the scanf values are being saved and push the BVS
# (see the image below to understan this -8)
padding_length_in_bytes = 15*4  # :integer
initial_state.regs.esp -= padding_length_in_bytes

for i in range(15):
    initial_state.stack_push(pwn[i])

simulation = project.factory.simgr(initial_state)

def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'WA!\n'.encode() in stdout_output

def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'AC!\n'.encode() in stdout_output

simulation.explore(find=is_successful, avoid=should_abort)

if simulation.found:
    solution_state = simulation.found[0]

    solution0 = solution_state.solver.eval(password0)
    solution1 = solution_state.solver.eval(password1)

    solution = ' '.join(map(str, [ solution0, solution1 ]))
    print(solution)
else:
    raise Exception('Could not find the solution')
