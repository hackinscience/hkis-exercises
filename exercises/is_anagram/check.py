from itertools import permutations, product
from random import shuffle

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)

KNOWN_ANAGRAMS = [
    ["evil", "vile"],
    ["Madam Curie", "Radium came"],
    ["New York Times", "monkeys write"],
    ["Church of Scientology", "rich-chosen goofy cult"],
    ["McDonald's restaurants", "Uncle Sam's standard rot"],
    ["a gentleman", "elegant man"],
    ["eleven plus two", "twelve plus one"],
    ["restful", "fluster"],
    ["funeral", "real fun"],
    ["adultery", "true lady"],
    ["forty five", "over fifty"],
    ["Santa", "Satan"],
    ["William Shakespeare", "I am a weakish speller"],
    ["George Bush", "He bugs Gore"],
    [
        "manoir",
        "minora",
        "romain",
        "romani",
        "marino",
        "Mirano",
        "Romina",
        "Marion",
        "Maroni",
        "Armino",
    ],
    [
        "nectar",
        "carnet",
        "encart",
        "canter",
        "cranté",
        "tancer",
        "encrât",
        "cernât",
        "crénât",
        "créant",
        "trance",
    ],
    [
        "argent",
        "gérant",
        "grenat",
        "garent",
        "ragent",
        "Tanger",
        "gréant",
        "régnât",
        "ganter",
        "Garten",
    ],
    [
        "crâne",
        "crâné",
        "écran",
        "nacre",
        "carné",
        "rance",
        "ancré",
        "caner",
        "encra",
        "cerna",
        "créna",
        "cenar",
        "nacer",
        "Acren",
    ],
    ["casser", "crases", "crasse", "césars", "ressac", "sacres", "séracs"],
    ["aléseur", "laurées", "resalue", "râleuse", "Suarlée"],
    [
        "carte",
        "écart",
        "acter",
        "caret",
        "cérat",
        "trace",
        "créât",
        "recta",
        "react",
        "tacer",
    ],
    ["poutres", "posture", "troupes", "stupore"],
    ["bestial", "bétails", "baliste", "établis"],
    ["sortie", "rôties", "toiser", "sorite", "seroit", "Tories"],
    [
        "entrais",
        "insérât",
        "riantes",
        "serinât",
        "sentira",
        "sériant",
        "tarsien",
        "traines",
        "transie",
        "tsarine",
    ],
    ["ralentis", "salirent", "latrines", "relisant"],
    ["juste", "sujet", "jutes"],
    ["naturel", "Laurent", "Renault", "Lautner", "neutral"],
    ["platine", "patelin", "plainte", "épilant", "pliante"],
    ["adonner", "donnera", "redonna"],
    ["engager", "grenage", "regagne", "rengage"],
    ["pirate", "paître", "parité", "patrie", "partie", "prêtai", "repaît", "étripa"],
    ["carie", "acier", "créai", "craie", "Icare", "Caire"],
    ["néo", "Noé", "Eno", "Eon", "one"],
    ["coréen", "cornée", "encore", "écorne"],
    ["chien", "niche", "chine", "Chine"],
    ["tare", "rate", "âtre", "réât", "Arte"],
    ["croupie", "poucier", "copieur"],
    [
        "entrait",
        "tartiné",
        "tintera",
        "traient",
        "étirant",
        "itérant",
        "nattier",
        "nitrate",
    ],
    ["ordre", "rôder", "dorer"],
    ["crabe", "berça", "cabre"],
    ["câble", "bâcle", "Caleb"],
    ["trêve", "verte", "revêt", "Evert"],
    ["imaginer", "migraine", "germinai"],
]


with ch.student_code():
    from solution import is_anagram


def main():
    shuffle(KNOWN_ANAGRAMS)
    with ch.student_code():
        response = is_anagram("ab", "aba")
    if response:
        ch.fail(
            "`ab` and `aba` are **not** anagrams, quoting Wikipedia:",
            "> An anagram is a word or phrase formed by rearranging the letters "
            "of a different word or phrase, typically using all the original "
            "letters exactly once.",
        )
    with ch.student_code():
        response = is_anagram("xxy", "xyy")
    if response:
        ch.fail(
            "`xxy` and `xyy` are **not** anagrams, quoting Wikipedia:",
            "> An anagram is a word or phrase formed by rearranging the letters "
            "of a different word or phrase, typically using all the original "
            "letters exactly once.",
        )
    for anagrams in KNOWN_ANAGRAMS:
        for a, b in permutations(anagrams, 2):
            with ch.student_code(
                prefix=[
                    "While running your function as:",
                    ch.code(f"is_anagram({a!r}, {b!r})", "python"),
                ]
            ):
                response = is_anagram(a, b)
            if not response:
                ch.fail(
                    f"`{a}` and `{b}` are anagrams, "
                    f"your function think they're not (it returned `{response!r}`)."
                )

    for list_a, list_b in zip(KNOWN_ANAGRAMS, KNOWN_ANAGRAMS[1:]):
        for a, b in product(list_a, list_b):
            with ch.student_code(
                prefix=[
                    "While running your function as:",
                    ch.code(f"is_anagram({a!r}, {b!r})", "python"),
                ]
            ):
                response = is_anagram(a, b)
            if response:
                ch.fail(
                    (
                        "`{}` and `{}` are **not** anagrams, "
                        "your function think they are."
                    ).format(a, b)
                )


if __name__ == "__main__":
    main()
