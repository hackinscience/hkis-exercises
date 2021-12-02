from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    file = Path("words.txt")
    check_string = "♥ Hello world! ♥"
    output = run("solution.py")
    if output == check_string:
        return  # Success
    if file.read_text().strip() != check_string.strip():
        fail("Have you modified my file? Please don't write to it, just read.")
    solution = Path("solution.py").read_text()
    if "d:\u005c" in solution.lower() or "c:\u005c" in solution.lower():
        fail(
            "Don't use absolute paths:",
            "I put the file in the same directory as your code, "
            "so just open `words.txt`.",
        )
    if "Words.txt" in solution:
        fail("The file is named `words.txt` (lowercased), not `Words.txt`.")
    if "words.txt" not in solution:
        fail(
            "Just read the 'words.txt' file, I'm providing it in the current directory."
        )
    if "built-in method read of" in output:
        fail("You forgot to call the read function, call is using parenthesis.")
    if "TextIOWrapper" in output:
        fail("You opened the file, but forgot to read its contents")
    if output == "\n".join(list(check_string)):
        fail("Looks like you're writing a single character per line.")
    fail(
        "Are you sure? I wrote:",
        code(check_string),
        "in the file, and you printed:",
        code(output),
    )


if __name__ == "__main__":
    try:
        check()
    finally:
        import os
        from contextlib import suppress

        with suppress(Exception):
            os.unlink("words.txt")
