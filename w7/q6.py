import sys

n_lines = 10

if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    n_lines = int(sys.argv.pop(1)[1:])

if len(sys.argv) == 1:
    sys.argv.append("-")


for filename in sys.argv[1:]:
    with open(filename) as f:
        print(f"==> {filename} <===.")
        for line_num, line in enumerate(f):
            if (line_num == n_lines):
                break
            print(line, end="")
            





















# for filename in sys.argv[1:]:
#     with open(filename) as f:
#         for num, line in enumerate(f):
#             if (num == n_lines):
#                 break
#             print(line.strip()) 