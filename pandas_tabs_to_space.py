## python3 pandas_tabs_to_spaces.py address.txtで実行

import os
import sys
import argparse
import pandas
import count_lines

def to_spaces(filename, filename_txt):
    ## pandasを使用したスペースへの置換
    df = pandas.read_csv(filename, header=None, delimiter='\t')
    newtext = df.to_csv(filename_txt, sep=' ', header=False, index=False)
    return newtext


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="replacecment tab to space")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="newfile.txt")

    args = parser.parse_args()
    
    filename = args.file
    filename_txt = args.newfile

    newtext = to_spaces(filename, filename_txt)
    
    