import pytest

from splitbill.cli import main


def test_cli_normal_split(capsys):
    assert main(["--total", "120.00", "--people", "3", "--tip", "15"]) == 0
    assert capsys.readouterr().out.splitlines() == [
        "Person 1: $46.00",
        "Person 2: $46.00",
        "Person 3: $46.00",
    ]


def test_cli_zero_tip(capsys):
    assert main(["--total", "100", "--people", "3", "--tip", "0"]) == 0
    assert capsys.readouterr().out.splitlines() == [
        "Person 1: $33.34",
        "Person 2: $33.33",
        "Person 3: $33.33",
    ]


@pytest.mark.parametrize(
    ("argv", "message"),
    [
        (["--total", "120", "--people", "0"], "people must be at least 1"),
        (["--total", "-5", "--people", "2"], "total must not be negative"),
        (["--total", "abc", "--people", "2"], "invalid number"),
        (["--total", "nan", "--people", "2"], "invalid number"),
        (["--total", "10", "--people", "two"], "invalid int value"),
        (["--people", "2"], "required"),
    ],
)
def test_cli_invalid_input(argv, message, capsys):
    with pytest.raises(SystemExit) as exc:
        main(argv)
    assert exc.value.code == 2
    assert message in capsys.readouterr().err
