import angr
import sys

main_addr = 0x4011a9
find_addr = 0x401371
avoid_addr = 0x40134d

def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'AC!\n'.encode() in stdout_output

def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'WA!\n'.encode() in stdout_output

class my_scanf(angr.SimProcedure):
    def run(self, format, s):
        # we're reading from stdin so the region is the file's content
        simfd = self.state.posix.get_fd(0)
        data, ret_size = simfd.read_data(0x04)

        self.state.memory.store(s, data)
        return ret_size

proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
proj.hook_symbol('__isoc99_scanf', my_scanf(), replace=True)

state = proj.factory.blank_state(addr=main_addr)


simgr = proj.factory.simulation_manager(state)
simgr.explore(find=is_successful, avoid=should_abort)

if simgr.found:
    print(simgr.found[0].posix.dumps(sys.stdin.fileno()))
    ANSWER = []
    for i in range(15):
        data = simgr.found[0].posix.dumps(sys.stdin.fileno())[0x04*i:0x04*(i+1)]
        ANSWER.append(data)
        print(int.from_bytes(data, byteorder='little', signed=True))
    with open('answer_input', 'w') as f:
        for a in ANSWER:
            f.write(str(a)+'\n')
else:
    print('Failed')
