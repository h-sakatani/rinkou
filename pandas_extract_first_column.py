# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def extract_first_list(filename, newfilename):
    df = count_lines.read_file(filename)
    cities = df["city"].unique()
    with open(newfilename, mode="w") as f:
        f.write('\n'.join(cities))
    return cities

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="first_column_list.txt")

    args = parser.parse_args()

    filename = args.file
    newfilename = args.newfile

    cities = extract_first_list(filename, newfilename)
    print(cities)
    