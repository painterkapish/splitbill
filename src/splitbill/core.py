from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def split_bill(total: Decimal, people: int, tip_percent: Decimal = Decimal("0")) -> list[Decimal]:
    """Return each person's share, rounded to cents.

    Shares always sum to the rounded grand total; any leftover cents are
    assigned one each to the first people in the list.
    """
    if people < 1:
        raise ValueError("people must be at least 1")
    if total < 0:
        raise ValueError("total must not be negative")
    if tip_percent < 0:
        raise ValueError("tip must not be negative")

    grand_total = (total * (1 + tip_percent / 100)).quantize(CENT, rounding=ROUND_HALF_UP)
    cents = int(grand_total / CENT)
    base, remainder = divmod(cents, people)
    return [(base + (1 if i < remainder else 0)) * CENT for i in range(people)]
