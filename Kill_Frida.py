
import sys
import time
import os
import signal
import psutil


def get_frida_process():
    ppid = os.getppid()
    proc = psutil.Process(pid=int(ppid))
    children = proc.children()
    for child in children:
        if child.name() == 'frida.exe':
            return child.pid


def wait_for(path, condition):
    while True:
        try:
            file = open(path, "r")
            contents = file.read()
            if condition in contents:
                return
            time.sleep(0.5)
        except:
            pass


def kill(pid):
    # try:
    #     os.kill(int(pid), signal.SIGKILL)
    # except:
    #     print("Error Encountered while running script")
    os.kill(int(pid), signal.SIGILL)


def main(argv):
    wait_for(argv[0], "]->")
    pid = get_frida_process()
    print("killing frida: " + str(pid))
    # need to kill the frida process
    kill(pid)


if __name__ == '__main__':
    main(sys.argv[1:])
