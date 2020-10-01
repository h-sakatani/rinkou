## python3 extract_mnmarkers.py address.txt 3(M数) 5(N数)で実行
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
    parser = argparse.ArgumentParser(description="extract from M lines to N lines")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("mrows", help="from m rows",type=int)
    parser.add_argument("nrows", help="to n rows",type=int)
    parser.add_argument("--newfile", help="new file name", type=str, default="mn_extract.txt")


    args = parser.parse_args()

    filename = args.file
    # rangeやpandasの行番号指定は最後のN行が含まれないため1を足す
    mlines = args.mrows 
    nlines = args.nrows +1
    newfilename = args.newfile

    df = read_file(filename)
    city = list(df["city"])
    town = list(df["town"])
    newtext = open(newfilename, "w", encoding="utf-8")

    for i in range(mlines, nlines):
        newtext.write(str(city[i])+" "+str(i)+"\n")
        print(str(city[i])+" "+str(town[i])+"\n")
    newtext.close()

    ## pandasを使用したM行目からN行目の抽出
    # print(df[mlines:nlines])