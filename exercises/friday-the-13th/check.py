import datetime
import gettext

import correction_helper as helper
from freezegun import freeze_time

_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext

helper.exclude_file_from_traceback(__file__)

with helper.student_code(print_prefix="When I imported your solution, it printed:"):
    from solution import friday_the_13th


def parse_date(some_date):
    if len(some_date) != len("YYYY-MM-DD"):
        # To catch dates like 2025-6-13 that would be accepted by strptime.
        raise ValueError("Date is not formatted properly")
    return datetime.datetime.strptime(some_date, "%Y-%m-%d").date()


def is_a_friday_the_13th(day):
    try:
        if isinstance(day, str):
            day = parse_date(day)
    except ValueError:
        return False
    return day.day == 13 and day.isoweekday() == 5


def compare(at, theirs, mine):
    if theirs == mine:
        return  # Success
    if is_a_friday_the_13th(at):
        message = _(
            "I am time traveling to a friday the 13th ({at}), just to check your code…"
        )

    else:
        message = _(
            "I am time traveling to random day ({at}), just to check your code…."
        )
    head = [
        message.format(at=at),
        "Now I call your `friday_the_13th` function from here…",
    ]
    if theirs is None:
        helper.fail(
            *head,
            "Your function is returning `None`, I expect it to `return` a string.",
        )
    printable_theirs = repr(theirs).replace("FakeDate", "datetime.date")
    tail = [
        _("Got:"),
        helper.code(printable_theirs),
    ]
    if not isinstance(theirs, str):
        helper.fail(
            *head,
            "Your function is expected to return a `str`, "
            "are you returning a `datetime` object instead?",
            *tail,
        )
    try:
        parse_date(theirs)
    except ValueError:
        helper.fail(
            *head,
            _(
                """Your function is expected to return a string of the following format:
YYYY-MM-DD."""
            ),
            *tail,
        )
    if is_a_friday_the_13th(at) and theirs != at and is_a_friday_the_13th(theirs):
        head.append(
            _(
                """In the case your function is executed during a friday the 13th,
it's expected to return the current friday the 13th, but you returned another one."""
            )
        )
    else:
        if is_a_friday_the_13th(theirs):
            head.append(
                _(
                    """Looks like you found a friday the 13th! But not the first one
right after {at} (which is {next})."""
                ).format(at=at, next=mine)
            )
        else:
            head.append(_("It does not looks like a friday the 13th!"))
    helper.fail(*head, *tail)


def main():
    with helper.student_code():
        friday_the_13th()
    for date, friday_13th in [
        ("2025-02-13", "2025-06-13"),
        ("2025-06-12", "2025-06-13"),
        ("2025-06-13", "2025-06-13"),
        ("2025-06-14", "2026-02-13"),
        ("2026-02-12", "2026-02-13"),
        ("2026-02-13", "2026-02-13"),
        ("2026-02-14", "2026-03-13"),
        ("2026-01-01", "2026-02-13"),
        ("2026-03-13", "2026-03-13"),
        ("2026-11-13", "2026-11-13"),
        ("2027-08-13", "2027-08-13"),
        ("2028-10-13", "2028-10-13"),
        ("2029-04-13", "2029-04-13"),
        ("2029-07-13", "2029-07-13"),
        ("2030-09-13", "2030-09-13"),
        ("2030-12-13", "2030-12-13"),
        ("2031-06-13", "2031-06-13"),
        ("2032-02-13", "2032-02-13"),
        ("2032-08-13", "2032-08-13"),
    ]:
        with freeze_time(date):
            with helper.student_code():
                theirs = friday_the_13th()
            compare(str(datetime.date.today()), theirs, friday_13th)

    today = datetime.date.today()
    if today.day == 13 and today.isoweekday() == 5:
        print(_("What a chance, you're doing this exercise on a friday the 13th ☺"))
    print(helper.congrats())


if __name__ == "__main__":
    main()
