from subprocess import run, PIPE
from correction_helper import code, congrats, fail, exclude_file_from_traceback

exclude_file_from_traceback(__file__)

gcc = run(
    ["gcc", "solution.c", "-o", "solution"], stderr=PIPE, stdout=PIPE, encoding="UTF-8"
)
if gcc.stderr:
    fail("Failed compiling your code:", code(gcc.stderr))

output = run(["./solution"], stdout=PIPE, stderr=PIPE, encoding="UTF-8")
if output.stdout == "Hello World\n":
    print(congrats())
    exit(0)

if output.stdout == "Hello World":
    fail("It would be better with a newline at the end, written as `\\n` in C.")

message = ["Naupe. Your code printed on `stdout`:", code(output.stdout)]
if output.stderr:
    message.extend(["And on `stderr`:", code(output.stderr)])
message.append("While I expected it to print: `Hello World\\n`")
fail(*message)
