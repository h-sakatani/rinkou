# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def count_string(filename):
    df = count_lines.read_file(filename)
    vc = df["city"].value_counts()
    return vc

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    
    
    args = parser.parse_args()

    filename = args.file
    
    vc = count_string(filename)
    print(vc)
    