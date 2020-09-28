## python3 tabs_to_spaces.py address.txtで実行
## --newfile optionでファイル名の指定が可能
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
    parser = argparse.ArgumentParser(description="replacecment tab to space")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="newfile.txt")

    args = parser.parse_args()
    
    filename = args.file
    filename_txt = args.newfile

    df = read_file(filename)
    city = list(df["city"])
    town = list(df["town"])
    newtext = open(filename_txt, "w", encoding="utf-8")
    
    #文字と文字の間をspaceにして新しいテキストに記載
    for i in range(len(df)):
        newtext.write(str(city[i])+" "+str(town[i])+"\n")
    newtext.close()

    
