import gettext
from itertools import combinations_with_replacement
from random import choice, randint
from string import ascii_letters

import correction_helper as helper

helper.exclude_file_from_traceback(__file__)

gettext = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


messages = [
    ("a", b"1:a"),
    ("abcdef", b"6:abcdef"),
    ([], b"le"),
    ({}, b"de"),
    ([1, 2, 3], b"li1ei2ei3ee"),
    (["a", "b", "c"], b"l1:a1:b1:ce"),
    ({"a": "boo"}, b"d1:a3:booe"),
    ({"outter": {"inner": "hello"}}, b"d6:outterd5:inner5:helloee"),
    (
        {"outter": {"inner1": "hello", "inner2": "world"}},
        b"d6:outterd6:inner15:hello6:inner25:worldee",
    ),
    (
        {"outter1": {"inner": "hello"}, "outter2": "world"},
        b"d7:outter1d5:inner5:helloe7:outter25:worlde",
    ),
    (
        {"t": "aa", "y": "q", "q": "ping", "a": {"id": "01234567890897653412"}},
        b"d1:ad2:id20:01234567890897653412e1:q4:ping1:t2:aa1:y1:qe",
    ),
    (
        {"zoo": ["poo", {"fo": "fa"}], "bah": "pouf"},
        b"d3:bah4:pouf3:zool3:pood2:fo2:faeee",
    ),
    ([1, 2, 3, 4, 5, 6], b"li1ei2ei3ei4ei5ei6ee"),
    (["a", 2, "b", 3, "c", 4], b"l1:ai2e1:bi3e1:ci4ee"),
    ([[[]]], b"llleee"),
    (
        ["a", 2, "b", 3, ["a", "b", "c"], 4, {"a": "boo", "4": [[[]]]}],
        b"l1:ai2e1:bi3el1:a1:b1:cei4ed1:4llleee1:a3:booee",
    ),
    (
        ["gR", "mL", "qq", "hv", "dx", "oV", "vE", "pI", "eT"],
        b"l2:gR2:mL2:qq2:hv2:dx2:oV2:vE2:pI2:eTe",
    ),
    ("my", b"2:my"),
    ("rW", b"2:rW"),
    ("IV", b"2:IV"),
    (
        {
            "FS": "kA",
            "jm": "QV",
            "aa": "vP",
            "wz": "FQ",
            "qB": "nB",
            "lG": "AQ",
            "iI": "xy",
            "qG": "pL",
        },
        b"d2:FS2:kA2:aa2:vP2:iI2:xy2:jm2:QV2:lG2:AQ2:qB2:nB2:qG2:pL2:wz2:FQe",
    ),
]

print("Trying your encode function…\n")

with helper.student_code():
    from solution import bencode

for message, expected in messages:
    with helper.student_code(
        prefix=[
            "While calling your function as:",
            helper.code("bencode({message!r})", "python"),
        ]
    ):
        got = bencode(message)
    if expected != got:
        message = [
            gettext("Wrong answer while testing `{thing}`").format(
                thing=f"bencode({message!r})"
            ),
            gettext("Got:"),
            helper.code(got),
            gettext("Expected:"),
            helper.code(expected),
        ]
        if type(got) != bytes:
            message.append(f"Expected a `bytes` instance, got a `{type(got)}`.")
        try:
            if len(expected) == len(got):
                message.append(
                    gettext(
                        "Beware: bencoded dicts keys should be "
                        "lexicographically ordered."
                    )
                )
        except TypeError:
            pass
        helper.fail(*message)


print("Trying your decode function…\n")

with helper.student_code():
    from solution import bdecode

for expected, message in messages:
    with helper.student_code(
        too_slow_message="I think I found an infinite loop in your code: "
        "`bdecode({!r})` took more than 1s.".format(message)
    ):
        got = bdecode(message)
    if expected != got:
        message = gettext("Wrong answer while testing `{thing}`").format(
            thing=f"bdecode({message!r})"
        )
        helper.fail(
            message,
            gettext("Got:"),
            helper.code(got),
            gettext("Expected:"),
            helper.code(expected),
        )

seeds = [
    left + right for left, right in combinations_with_replacement(ascii_letters, 2)
]

for _ in range(100):
    messages.append(([choice(seeds) for _ in range(randint(1, 10))], ""))
    messages.append((choice(seeds), ""))
    messages.append(({choice(seeds): choice(seeds) for _ in range(randint(1, 10))}, ""))


for message, _ in messages:
    with helper.student_code():
        result = bdecode(bencode(message))
    if message != result:
        helper.fail(
            gettext("Wrong answer while testing `{thing}`").format(
                thing=f"decode(encode({repr(message)}))"
            ),
            gettext("Got:"),
            helper.code(result),
            gettext("Expected:"),
            helper.code(message),
        )


print(gettext("`bencode`/`bdecode` is not an easy one, but you owned it, congrats!"))
