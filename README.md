# Sudoku Exchange "Puzzle Bank"

This repository contains several hundred thousand Sudoku puzzles that were
computer generated for use by the [Sudoku Exchange](https://sudokuexchange.com/)
web site.

The puzzles were generated using the
[QQWing Sudoku](https://github.com/stephenostermiller/qqwing) software, which
ensure that each puzzle has a unique solution.
The generated puzzles were then graded using
[Sukaku Explainer](https://github.com/SudokuMonster/SukakuExplainer) and
sorted into four 'buckets':

| Filename            | Difficulty Rating | Total Entries       |
| ------------------- | ----------------- | ------------------- |
| [1.2.txt](./1.2.txt) | 1.2 | 100000 |
| [1.5.txt](./1.5.txt) | 1.5 | 88643 |
| [1.7.txt](./1.7.txt) | 1.7 | 88000 |
| [2.0.txt](./2.0.txt) | 2.0 | 88000 |
| [2.3.txt](./2.3.txt) | 2.3 | 88000 |
| [2.5.txt](./2.5.txt) | 2.5 | 25000 |
| [2.6.txt](./2.6.txt) | 2.6 | 29116 |
| [2.8.txt](./2.8.txt) | 2.8 | 25000 |
| [3.0.txt](./3.0.txt) | 3.0 | 25000 |
| [3.2.txt](./3.2.txt) | 3.2 | 25000 |
| [3.4.txt](./3.4.txt) | 3.4 | 25000 |
| [3.6.txt](./3.6.txt) | 3.6 | 7511 |
| [3.8.txt](./3.8.txt) | 3.8 | 3320 |
| [4.0.txt](./4.0.txt) | 4.0 | 25000 |
| [4.1.txt](./4.1.txt) | 4.1 | 25000 |
| [4.2.txt](./4.2.txt) | 4.2 | 25000 |
| [4.3.txt](./4.3.txt) | 4.3 | 25000 |
| [4.4.txt](./4.4.txt) | 4.4 | 25000 |
| [4.5.txt](./4.5.txt) | 4.5 | 25000 |
| [4.6.txt](./4.6.txt) | 4.6 | 6095 |
| [4.7.txt](./4.7.txt) | 4.7 | 537 |
| [4.8.txt](./4.8.txt) | 4.8 | 13 |
| [5.0.txt](./5.0.txt) | 5.0 | 536 |
| [5.2.txt](./5.2.txt) | 5.2 | 391 |
| [5.4.txt](./5.4.txt) | 5.4 | 6000 |
| [5.5.txt](./5.5.txt) | 5.5 | 6000 |
| [5.6.txt](./5.6.txt) | 5.6 | 6000 |
| [5.7.txt](./5.7.txt) | 5.7 | 6000 |
| [5.8.txt](./5.8.txt) | 5.8 | 65 |
| [5.9.txt](./5.9.txt) | 5.9 | 37 |
| [6.0.txt](./6.0.txt) | 6.0 | 11 |
| [6.1.txt](./6.1.txt) | 6.1 | 2 |
| [6.2.txt](./6.2.txt) | 6.2 | 661 |
| [6.3.txt](./6.3.txt) | 6.3 | 6000 |
| [6.4.txt](./6.4.txt) | 6.4 | 6000 |
| [6.6.txt](./6.6.txt) | 6.6 | 5346 |
| [6.7.txt](./6.7.txt) | 6.7 | 6000 |
| [6.8.txt](./6.8.txt) | 6.8 | 6000 |
| [6.9.txt](./6.9.txt) | 6.9 | 6000 |
| [7.0.txt](./7.0.txt) | 7.0 | 4822 |
| [7.1.txt](./7.1.txt) | 7.1 | 9404 |
| [7.2.txt](./7.2.txt) | 7.2 | 8945 |
| [7.3.txt](./7.3.txt) | 7.3 | 6000 |
| [7.4.txt](./7.4.txt) | 7.4 | 1700 |
| [7.5.txt](./7.5.txt) | 7.5 | 575 |
| [7.7.txt](./7.7.txt) | 7.7 | 874 |
| [7.8.txt](./7.8.txt) | 7.8 | 2497 |
| [7.9.txt](./7.9.txt) | 7.9 | 732 |
| [8.0.txt](./8.0.txt) | 8.0 | 236 |
| [8.1.txt](./8.1.txt) | 8.1 | 10 |
| [8.2.txt](./8.2.txt) | 8.2 | 2030 |
| [8.3.txt](./8.3.txt) | 8.3 | 6000 |
| [8.4.txt](./8.4.txt) | 8.4 | 6000 |
| [8.5.txt](./8.5.txt) | 8.5 | 3701 |
| [8.6.txt](./8.6.txt) | 8.6 | 308 |
| [8.7.txt](./8.7.txt) | 8.7 | 49 |
| [8.8.txt](./8.8.txt) | 8.8 | 768 |
| [8.9.txt](./8.9.txt) | 8.9 | 2190 |
| [9.0.txt](./9.0.txt) | 9.0 | 1620 |
| [9.1.txt](./9.1.txt) | 9.1 | 150 |
| [9.2.txt](./9.2.txt) | 9.2 | 20 |
| [9.3.txt](./9.3.txt) | 9.3 | 1 |

Each text file has one puzzle per line, represented as three space-separated
fields and a Unix-style line-ending, for a total of 100 bytes per record:

     12 bytes of SHA1 hash of the digits string (for randomising order)
     81 bytes of puzzle digits
      4 bytes of rating (nn.n)
      3 bytes of white-space (including the linefeed);
    100 bytes total

### License

The data set is dedicated to the [public domain](LICENSE.txt).

