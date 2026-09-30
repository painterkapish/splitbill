from decimal import Decimal

import pytest

from splitbill import split_bill


def test_even_split_with_tip():
    assert split_bill(Decimal("120.00"), 3, Decimal("15")) == [Decimal("46.00")] * 3


def test_uneven_split_distributes_leftover_cents():
    shares = split_bill(Decimal("100.00"), 3)
    assert shares == [Decimal("33.34"), Decimal("33.33"), Decimal("33.33")]
    assert sum(shares) == Decimal("100.00")


def test_tip_rounded_to_cents():
    shares = split_bill(Decimal("10.00"), 1, Decimal("12.5"))
    assert shares == [Decimal("11.25")]


def test_zero_tip():
    assert split_bill(Decimal("90.00"), 3, Decimal("0")) == [Decimal("30.00")] * 3


def test_default_tip_is_zero():
    assert split_bill(Decimal("50.00"), 2) == [Decimal("25.00")] * 2


def test_zero_total():
    assert split_bill(Decimal("0"), 4, Decimal("20")) == [Decimal("0.00")] * 4


@pytest.mark.parametrize("people", [0, -1])
def test_people_less_than_one_rejected(people):
    with pytest.raises(ValueError, match="people"):
        split_bill(Decimal("10.00"), people)


def test_negative_total_rejected():
    with pytest.raises(ValueError, match="total"):
        split_bill(Decimal("-1.00"), 2)


def test_negative_tip_rejected():
    with pytest.raises(ValueError, match="tip"):
        split_bill(Decimal("10.00"), 2, Decimal("-5"))
