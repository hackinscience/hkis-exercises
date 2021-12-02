from unicodedata import name


import correction_helper as helper

helper.exclude_file_from_traceback(__file__)


def check():
    output = helper.run("solution.py")
    if output == "":
        helper.fail("You're printing nothing ☹")
    clean_output = output.replace(" ", "").replace("\n", "").replace(",", "")
    for char in clean_output:
        if "HEART" not in name(char, ""):
            charname = f"({name(char)})" if name(char, "") else ""
            helper.fail(
                f"Why are you printing `{char}` {charname}?",
                "It does not looks like a heart to me.",
                "Your code printed:",
                output,
            )
    some_hearts = "☙♡♥❣❤❥🎔💑💓💔💕💖💗💘💙💚💛💜💝💞💟🖤😍😻🧡"
    for heart in some_hearts:
        if heart not in output:
            helper.fail(
                "You've forgot some hearts characters.",
                "Here's your full output:",
                helper.code(output),
            )
    print(
        "I bet you'll find some nice unicode things "
        "for your next social media post with Python ☺",
        "Here's the hearts your code printed:",
        helper.code(output),
        sep="\n\n",
    )


if __name__ == "__main__":
    check()
