## python3 pandas_last_nrows.py address.txt 3(N数)で実行
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def extract_lines(filename, fromnline):
    df = count_lines.read_file(filename)
    nrows = df.tail(fromnline)
    return nrows

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("nrows", help="first n rows",type=int)
    
    args = parser.parse_args()

    filename = args.file
    fromnline = args.nrows

    nrows = extract_lines(filename, fromnline)
    print(nrows)
    