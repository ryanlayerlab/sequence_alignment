# Global and local sequence aligment

## Usage

### Needleman-Wunsh
```
usage: nw.py [-h] --A A --B B [--gap GAP] [--miss MISS] [--match MATCH]

optional arguments:
  -h, --help     show this help message and exit
  --A A          Sequence A
  --B B          Sequence B
  --gap GAP      Gap penalty (default: -2)
  --miss MISS    Mismatch penalty (default: -1)
  --match MATCH  Match score (default: 1)
```

### Smith-Waterman
```
usage: sw.py [-h] --A A --B B [--gap GAP] [--miss MISS] [--match MATCH]

optional arguments:
  -h, --help     show this help message and exit
  --A A          Sequence A
  --B B          Sequence B
  --gap GAP      Gap penalty (default: -2)
  --miss MISS    Mismatch penalty (default: -1)
  --match MATCH  Match score (default: 1)
```

## Examles
### Needleman-Wunsh
```
python src/nw.py --B CCTGTACC --A ATGATACCCT
-ATGATACCCT
CCTG-TA-CC-
Score: -3
```
### Smith-Waterman
```
python sw.py --B CCTGTACC --A ATGATACCCT
TACC
TACC
Score: 4
```
