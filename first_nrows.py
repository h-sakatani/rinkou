## python3 first_nrows.py address.txt 3(N数)で実行
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
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("nrows", help="first n rows",type=int)
    # 引数でファイル名を指定しない場合はデフォルトでファイル名を指定
    parser.add_argument("--newfile", help="new file name", type=str, default="first_nlines.txt")

    args = parser.parse_args()

    filename = args.file
    nlines = args.nrows
    newfilename = args.newfile

    df = read_file(filename)
    city = list(df["city"])
    town = list(df["town"])
    newtext = open(newfilename, "w", encoding="utf-8")
    
    # n番目までのデータを表示して新しいテキストに書き込む
    for i in range(nlines):
        newtext.write(str(city[i])+" "+str(town[i])+"\n")
        print(str(city[i])+" "+str(town[i])+"\n")
    newtext.close()
    
    ## pandasを利用して先頭N行を出力
    # print(df.head(nlines))