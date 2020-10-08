## python3 count_lines.py address.txtで実行

import os
import sys
import argparse
import pandas

def read_file(path):
    # textファイル1列目がcity,2列目がtownと指定
    df = pandas.read_table(path, names=["city", "town"])
    return df

def count_rows(filename):
    df = read_file(filename)
    countrows = len(df)
    return countrows

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="count lines of file using Pandas")
    parser.add_argument("file", help="file path", type=str)
    
    args = parser.parse_args()

    filename = args.file
    
    countrows = count_rows(filename)

    
    print('file: %s' % filename)
    #dfの行数を表示
    print('Number of lines is {}'.format(countrows))
