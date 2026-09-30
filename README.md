# splitbill

Split a bill (plus tip) evenly between people, rounded to cents. Standard library only; requires Python 3.11+.

## Install

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install .            # or: pip install -e '.[test]' for development
```

## Usage

```sh
$ splitbill --total 120.00 --people 3 --tip 15
Person 1: $46.00
Person 2: $46.00
Person 3: $46.00
```

- `--total` (required): bill amount before tip; must not be negative.
- `--people` (required): number of people; must be at least 1.
- `--tip` (optional, default `0`): tip percentage.

Shares always add up to the rounded grand total; leftover cents go to the first people listed:

```sh
$ splitbill --total 100 --people 3
Person 1: $33.34
Person 2: $33.33
Person 3: $33.33
```

You can also run it as `python -m splitbill ...`.

## Tests

```sh
pip install -e '.[test]'
pytest
```
