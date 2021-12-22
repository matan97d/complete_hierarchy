
import frida
import codecs
import sys
import Results_Filter


def run_frida_script(js, pid_pname):
    with codecs.open(js, 'r', 'utf-8') as script_file:
        source = script_file.read()

    usb_device = frida.get_usb_device()
    session = usb_device.attach(pid_pname)
    script = session.create_script(source)

    # Fire the script
    file = open(pid_pname + ".txt", "w", newline='')
    sys.stdout = file
    script.load()
    sys.stdout = sys.__stdout__


def main(argv):
    if "-m" in argv:
        argv.remove("-m")
        run_frida_script('complete_class_method_hierarchy.js', argv[0])
    else:
        run_frida_script('complete_class_hierarchy.js', argv[0])
    print("frida ended")
    Results_Filter.filter_tree(argv)


if __name__ == '__main__':
    main(sys.argv[1:])
