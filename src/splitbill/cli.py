import argparse
import sys
from decimal import Decimal, InvalidOperation

from splitbill.core import split_bill


def _decimal(value: str) -> Decimal:
    try:
        result = Decimal(value)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"invalid number: {value!r}") from None
    if not result.is_finite():
        raise argparse.ArgumentTypeError(f"invalid number: {value!r}")
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="splitbill",
        description="Split a bill (plus tip) evenly between people.",
    )
    parser.add_argument("--total", type=_decimal, required=True, help="bill total before tip, e.g. 120.00")
    parser.add_argument("--people", type=int, required=True, help="number of people splitting the bill (>= 1)")
    parser.add_argument("--tip", type=_decimal, default=Decimal("0"), help="tip percentage, e.g. 15 (default: 0)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        shares = split_bill(args.total, args.people, args.tip)
    except ValueError as exc:
        parser.error(str(exc))
    for i, share in enumerate(shares, start=1):
        print(f"Person {i}: ${share:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
