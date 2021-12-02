"""Test all exercises solutions.py, ok-*.py (and check if they
succeed) and ko-*.py (and check if it fail).
"""

from pathlib import Path
from collections import defaultdict
from tempfile import TemporaryDirectory
import json
from shutil import copy
from subprocess import run, PIPE, CompletedProcess
import warnings

import requests
import pytest


def run_answer(exercise: Path, answer: str) -> CompletedProcess:
    """Run the given answer for the given exercise."""
    with TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        (tmp_path / "solution").write_text(answer, encoding="UTF-8")
        copy(exercise / "check.py", tmp_path)
        if (exercise / "pre_check.py").exists():
            copy(exercise / "pre_check.py", tmp_path)
            run(
                ["python3", "pre_check.py"],
                cwd=tmp_path,
                stdout=PIPE,
                stderr=PIPE,
                text=True,
                check=True,
            )
        return run(
            ["python3", "check.py"],
            cwd=tmp_path,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            check=False,
        )


def get_safe_answers(is_valid: bool) -> list:
    auth = tuple(
        (Path.home() / ".hkis")
        .read_text(encoding="UTF-8")
        .rstrip()
        .split(":", maxsplit=1)
    )
    answers = []
    url = "https://www.hackinscience.org/api/answers/"
    while url:
        response = requests.get(
            url,
            params={"is_safe": True, "is_valid": is_valid},
            auth=auth,
        ).json()
        answers.extend(response["results"])
        url = response.get("next")
    return answers


def generate_tests(is_valid: bool):
    tests = []
    answers = get_safe_answers(is_valid)
    by_exercise = defaultdict(list)
    for answer in answers:
        by_exercise[answer["exercise"]].append(answer)
    for exercise_meta_file in Path(".").glob("*/*/meta"):
        exercise_path = exercise_meta_file.parent
        exercise = json.loads(exercise_meta_file.read_text(encoding="UTF-8"))
        exercise_answers = by_exercise[exercise["url"]]
        if not exercise_answers:
            warnings.warn(
                f"No answers with is_safe=True and is_valid={is_valid} "
                f"to test {exercise['title']} ({exercise['url']})."
            )
        for answer in exercise_answers:
            tests.append((str(exercise_path), answer))
    return tests


@pytest.mark.parametrize("exercise_path,answer", generate_tests(is_valid=True))
def test_exercise_shall_pass(exercise_path, answer):
    result = run_answer(Path(exercise_path), answer["source_code"])
    assert result.returncode == 0, result


@pytest.mark.parametrize("exercise_path,answer", generate_tests(is_valid=False))
def test_exercise_shall_not_pass(exercise_path, answer):
    result = run_answer(Path(exercise_path), answer["source_code"])
    assert result.returncode != 0, result


@pytest.mark.parametrize("check_path", [str(p) for p in Path(".").glob("*/*/check.py")])
def test_checker_exclude_itself_from_tracebacks(check_path):
    check_path = Path(check_path)
    assert "exclude_file_from_traceback(__file__)" in check_path.read_text(
        encoding="UTF-8"
    )
