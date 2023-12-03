# Readme

A quick and dirty script to convert files from the [open Lichess database](https://database.lichess.org/) to `.csv` files with the relevant information. Example output file provided in `2013-01_lichess.csv`.

## Usage

```sh
zstdcat filename.pgn.zst | python path/to/LichessParser/src/main.py output_file.csv
```
