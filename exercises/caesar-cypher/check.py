from operator import add, sub
from string import ascii_lowercase

from correction_helper import (
    code,
    exclude_file_from_traceback,
    fail,
    student_code,
    congrats,
)

exclude_file_from_traceback(__file__)

letters = list(ascii_lowercase)
forward = add
backward = sub


CHECKS = {
    ("Two empty halves of coconuts", 1): "Uxp fnquz ibmwft pg dpdpovut",
    ("Two empty halves of coconuts", 2): "Vyq gorva jcnxgu qh eqeqpwvu",
    ("Two empty halves of coconuts", 13): "Gjb rzcgl unyirf bs pbpbahgf",
    ("Two empty halves of coconuts", 20): "Nqi ygjns bufpym iz wiwihonm",
    ("We are the knights who say NIII", 1): "Xf bsf uif lojhiut xip tbz OJJJ",
    ("We are the knights who say NIII", 2): "Yg ctg vjg mpkijvu yjq uca PKKK",
    ("We are the knights who say NIII", 13): "Jr ner gur xavtugf jub fnl AVVV",
    ("We are the knights who say NIII", 20): "Qy uly nby ehcabnm qbi mus HCCC",
    ("We want A SHRUBBERY!!!", 1): "Xf xbou B TISVCCFSZ!!!",
    ("We want A SHRUBBERY!!!", 2): "Yg ycpv C UJTWDDGTA!!!",
    ("We want A SHRUBBERY!!!", 13): "Jr jnag N FUEHOOREL!!!",
    ("We want A SHRUBBERY!!!", 20): "Qy quhn U MBLOVVYLS!!!",
    ("None shall pass!", 1): "Opof tibmm qbtt!",
    ("None shall pass!", 2): "Pqpg ujcnn rcuu!",
    ("None shall pass!", 13): "Abar funyy cnff!",
    ("None shall pass!", 20): "Hihy mbuff jumm!",
    ("It is I Arthur", 1): "Ju jt J Bsuivs",
    ("It is I Arthur", 2): "Kv ku K Ctvjwt",
    ("It is I Arthur", 13): "Vg vf V Neguhe",
    ("It is I Arthur", 20): "Cn cm C Ulnbol",
}


def check():
    with student_code(prefix="While importing your module:"):
        from solution import caesar_cypher_encrypt, caesar_cypher_decrypt
    for (cleartext, rotation), ciphertext in CHECKS.items():
        with student_code(
            prefix=[
                "While testing your function as:",
                code(f"caesar_cypher_encrypt({cleartext!r}, {rotation!r})", "python"),
            ]
        ):
            theirs = caesar_cypher_encrypt(cleartext, rotation)
        if theirs != ciphertext:
            fail(
                f"Error while encoding `{cleartext!r}` with a rotation "
                f"of `{rotation}`, got:",
                code(theirs),
                "expected:",
                code(ciphertext),
            )
        with student_code(
            prefix="While testing `caesar_cypher_decrypt({ciphertext!r}, {rotation})`:"
        ):
            theirs = caesar_cypher_decrypt(ciphertext, rotation)
        if cleartext != theirs:
            fail(
                f"Error while decoding `{ciphertext!r}` with a rotation "
                f"of `{rotation}`, got:",
                code(theirs),
                "expected:",
                code(cleartext),
            )
    print(congrats())


if __name__ == "__main__":
    check()
