import sys
from correction_helper import exclude_file_from_traceback

exclude_file_from_traceback(__file__)

print(
    "This is not really an exercise, it has no check, "
    "#sry, there's just no way to « do » it."
)
print()
print(
    "Or maybe if you write a new exercise, or donate, "
    "I can make the effort of logging into the admin zone and "
    "manually validate it for you, if you care :D"
)

sys.exit(1)
