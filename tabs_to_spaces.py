## python3 tabs_to_spaces.py address.txtで実行
## --newfile optionでファイル名の指定が可能
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
# 自作関数使用のためのimport
import count_lines

def to_space(filename, filename_txt):
    df = count_lines.read_file(filename)
    city = list(df["city"])
    town = list(df["town"])
    newtext = open(filename_txt, "w", encoding="utf-8")
    
    # 文字と文字の間をspaceにして新しいテキストに記載
    for i in range(len(df)):
         newtext.write(str(city[i]) + " " + str(town[i]) + "\n")
    newtext.close()

    return newtext


# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="replacecment tab to space")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="newfile.txt")

    args = parser.parse_args()
    
    filename = args.file
    filename_txt = args.newfile

    
    newtext = to_space(filename, filename_txt)
    
    ## pandasを使用したスペースへの置換
    # df = pandas.read_csv(filename, header=None, delimiter='\t')
    # df.to_csv(filename_txt, sep=' ', header=False, index=False)
    
    
