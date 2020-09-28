## python3 count_row.py address.txtで実行
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas

def read_file(path):
    # textファイル1列目がcity,2列目がtownと指定
    df = pandas.read_table(path, names=["city", "town"])
    return df

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="count lines of file using Pandas")
    parser.add_argument("file", help="file path", type=str)
    
    args = parser.parse_args()

    filename = args.file
    df = read_file(filename)
    
    print('file: %s' % filename)
    #dfの行数を表示
    print('Number of lines is {}'.format(len(df)))
