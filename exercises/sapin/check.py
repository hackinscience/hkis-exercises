from collections import Counter

import correction_helper as helper

helper.exclude_file_from_traceback(__file__)


def describe_line(line):
    line = Counter(line)

    def describe_letter(letter, qty):
        if letter == "*":
            return "star" + ("s" if qty > 1 else "")
        elif letter == " ":
            return "space" + ("s" if qty > 1 else "")
        else:
            return "`" + repr(letter) + "`"

    return ", ".join(
        [f"{qty} {describe_letter(letter, qty)}" for letter, qty in line.items()]
    )


CHECKS = {
    0: "",
    1: (
        "   *   \n"  # fmt: skip
        "  ***  \n"
        " ***** \n"
        "*******\n"
        "   |   \n"
    ),
    2: (
        "      *      \n"
        "     ***     \n"
        "    *****    \n"
        "   *******   \n"
        "    *****    \n"
        "   *******   \n"
        "  *********  \n"
        " *********** \n"
        "*************\n"
        "     |||     \n"
        "     |||     \n"
    ),
    3: (
        "          *          \n"
        "         ***         \n"
        "        *****        \n"
        "       *******       \n"
        "        *****        \n"
        "       *******       \n"
        "      *********      \n"
        "     ***********     \n"
        "    *************    \n"
        "     ***********     \n"
        "    *************    \n"
        "   ***************   \n"
        "  *****************  \n"
        " ******************* \n"
        "*********************\n"
        "         |||         \n"
        "         |||         \n"
        "         |||         \n"
    ),
    4: (
        "              *              \n"
        "             ***             \n"
        "            *****            \n"
        "           *******           \n"
        "            *****            \n"
        "           *******           \n"
        "          *********          \n"
        "         ***********         \n"
        "        *************        \n"
        "         ***********         \n"
        "        *************        \n"
        "       ***************       \n"
        "      *****************      \n"
        "     *******************     \n"
        "    *********************    \n"
        "      *****************      \n"
        "     *******************     \n"
        "    *********************    \n"
        "   ***********************   \n"
        "  *************************  \n"
        " *************************** \n"
        "*****************************\n"
        "            |||||            \n"
        "            |||||            \n"
        "            |||||            \n"
        "            |||||            \n"
    ),
    5: (
        "                   *                   \n"
        "                  ***                  \n"
        "                 *****                 \n"
        "                *******                \n"
        "                 *****                 \n"
        "                *******                \n"
        "               *********               \n"
        "              ***********              \n"
        "             *************             \n"
        "              ***********              \n"
        "             *************             \n"
        "            ***************            \n"
        "           *****************           \n"
        "          *******************          \n"
        "         *********************         \n"
        "           *****************           \n"
        "          *******************          \n"
        "         *********************         \n"
        "        ***********************        \n"
        "       *************************       \n"
        "      ***************************      \n"
        "     *****************************     \n"
        "       *************************       \n"
        "      ***************************      \n"
        "     *****************************     \n"
        "    *******************************    \n"
        "   *********************************   \n"
        "  ***********************************  \n"
        " ************************************* \n"
        "***************************************\n"
        "                 |||||                 \n"
        "                 |||||                 \n"
        "                 |||||                 \n"
        "                 |||||                 \n"
        "                 |||||                 \n"
    ),
    6: (
        "                        *                        \n"
        "                       ***                       \n"
        "                      *****                      \n"
        "                     *******                     \n"
        "                      *****                      \n"
        "                     *******                     \n"
        "                    *********                    \n"
        "                   ***********                   \n"
        "                  *************                  \n"
        "                   ***********                   \n"
        "                  *************                  \n"
        "                 ***************                 \n"
        "                *****************                \n"
        "               *******************               \n"
        "              *********************              \n"
        "                *****************                \n"
        "               *******************               \n"
        "              *********************              \n"
        "             ***********************             \n"
        "            *************************            \n"
        "           ***************************           \n"
        "          *****************************          \n"
        "            *************************            \n"
        "           ***************************           \n"
        "          *****************************          \n"
        "         *******************************         \n"
        "        *********************************        \n"
        "       ***********************************       \n"
        "      *************************************      \n"
        "     ***************************************     \n"
        "        *********************************        \n"
        "       ***********************************       \n"
        "      *************************************      \n"
        "     ***************************************     \n"
        "    *****************************************    \n"
        "   *******************************************   \n"
        "  *********************************************  \n"
        " *********************************************** \n"
        "*************************************************\n"
        "                     |||||||                     \n"
        "                     |||||||                     \n"
        "                     |||||||                     \n"
        "                     |||||||                     \n"
        "                     |||||||                     \n"
        "                     |||||||                     \n"
    ),
    7: (
        "                              *                              \n"
        "                             ***                             \n"
        "                            *****                            \n"
        "                           *******                           \n"
        "                            *****                            \n"
        "                           *******                           \n"
        "                          *********                          \n"
        "                         ***********                         \n"
        "                        *************                        \n"
        "                         ***********                         \n"
        "                        *************                        \n"
        "                       ***************                       \n"
        "                      *****************                      \n"
        "                     *******************                     \n"
        "                    *********************                    \n"
        "                      *****************                      \n"
        "                     *******************                     \n"
        "                    *********************                    \n"
        "                   ***********************                   \n"
        "                  *************************                  \n"
        "                 ***************************                 \n"
        "                *****************************                \n"
        "                  *************************                  \n"
        "                 ***************************                 \n"
        "                *****************************                \n"
        "               *******************************               \n"
        "              *********************************              \n"
        "             ***********************************             \n"
        "            *************************************            \n"
        "           ***************************************           \n"
        "              *********************************              \n"
        "             ***********************************             \n"
        "            *************************************            \n"
        "           ***************************************           \n"
        "          *****************************************          \n"
        "         *******************************************         \n"
        "        *********************************************        \n"
        "       ***********************************************       \n"
        "      *************************************************      \n"
        "         *******************************************         \n"
        "        *********************************************        \n"
        "       ***********************************************       \n"
        "      *************************************************      \n"
        "     ***************************************************     \n"
        "    *****************************************************    \n"
        "   *******************************************************   \n"
        "  *********************************************************  \n"
        " *********************************************************** \n"
        "*************************************************************\n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
        "                           |||||||                           \n"
    ),
    8: (
        "                                    *                                    \n"
        "                                   ***                                   \n"
        "                                  *****                                  \n"
        "                                 *******                                 \n"
        "                                  *****                                  \n"
        "                                 *******                                 \n"
        "                                *********                                \n"
        "                               ***********                               \n"
        "                              *************                              \n"
        "                               ***********                               \n"
        "                              *************                              \n"
        "                             ***************                             \n"
        "                            *****************                            \n"
        "                           *******************                           \n"
        "                          *********************                          \n"
        "                            *****************                            \n"
        "                           *******************                           \n"
        "                          *********************                          \n"
        "                         ***********************                         \n"
        "                        *************************                        \n"
        "                       ***************************                       \n"
        "                      *****************************                      \n"
        "                        *************************                        \n"
        "                       ***************************                       \n"
        "                      *****************************                      \n"
        "                     *******************************                     \n"
        "                    *********************************                    \n"
        "                   ***********************************                   \n"
        "                  *************************************                  \n"
        "                 ***************************************                 \n"
        "                    *********************************                    \n"
        "                   ***********************************                   \n"
        "                  *************************************                  \n"
        "                 ***************************************                 \n"
        "                *****************************************                \n"
        "               *******************************************               \n"
        "              *********************************************              \n"
        "             ***********************************************             \n"
        "            *************************************************            \n"
        "               *******************************************               \n"
        "              *********************************************              \n"
        "             ***********************************************             \n"
        "            *************************************************            \n"
        "           ***************************************************           \n"
        "          *****************************************************          \n"
        "         *******************************************************         \n"
        "        *********************************************************        \n"
        "       ***********************************************************       \n"
        "      *************************************************************      \n"
        "          *****************************************************          \n"
        "         *******************************************************         \n"
        "        *********************************************************        \n"
        "       ***********************************************************       \n"
        "      *************************************************************      \n"
        "     ***************************************************************     \n"
        "    *****************************************************************    \n"
        "   *******************************************************************   \n"
        "  *********************************************************************  \n"
        " *********************************************************************** \n"
        "*************************************************************************\n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
        "                                |||||||||                                \n"
    ),
}


def test_fir(i, expected):
    got = helper.run("solution.py", str(i))
    got = "\n".join(line.rstrip() for line in got.split("\n")).rstrip()
    expected = "\n".join(line.rstrip() for line in expected.split("\n")).rstrip()
    if got == expected:
        return  # Yeah!
    if got == "":
        helper.fail(
            f"I expected your fir tree (of size {i}) to look like this, "
            "but you printed nothing:",
            helper.code(expected.replace(" ", ".")),
            "(I replaced spaces with dots for readability only, " "don't use dots!)",
        )
    if expected == "":
        helper.fail(
            "A fir tree of size 0 should be literaly nothing, but you printed:",
            helper.code(got),
        )
    helper.print_stderr(f"Your sapin of width {i} is wrong:")
    for lineno, (gotline, expectedline) in enumerate(
        zip(got.split("\n"), expected.split("\n"))
    ):
        if gotline != expectedline:
            helper.print_stderr(
                f"""On line {lineno}, got {describe_line(gotline)},
    expected {describe_line(expectedline)}:"""
            )
            break
    helper.fail(
        "Here what's your program printed:",
        helper.code(got),
        "Here's what I expected:",
        expected,
    )


def main():
    for i, expected in CHECKS.items():
        test_fir(i, expected)
    print(helper.congrats())


if __name__ == "__main__":
    main()
