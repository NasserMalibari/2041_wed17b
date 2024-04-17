
import sys
# "hello world foo" -> "[hello, world, foo]"
def qw(line):
    return line.split(' ')
    # alternatively use re.split(<regex>) to split in more 
    # complex cases

def die(message, exitStatus):
    print(message, file=sys.stderr)
    sys.exit(exitStatus)

def main():
    pass

if __name__ == "__main__":
    main()