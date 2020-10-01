## python3 last_nrows.py address.txt 3(N数)で実行
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
    parser = argparse.ArgumentParser(description="extract last n lines")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("nrows", help="last n rows",type=int)
    parser.add_argument("--newfile", help="new file name", type=str, default="last_nlines.txt")

    args = parser.parse_args()

    filename = args.file
    nlines = args.nrows
    newfilename = args.newfile

    df = read_file(filename)
    city = list(df["city"])
    town = list(df["town"])
    newtext = open(newfilename, "w", encoding="utf-8")
    #  countでは最後から数えるのでマイナスを指定し、rangeは0からの範囲なので-1して後ろから数えるように指定
    for i in range(nlines):
        count = -(i+1)
        newtext.write(str(city[count])+" "+str(town[count])+"\n")
        print(str(city[count])+" "+str(town[count])+"\n")
    newtext.close()
    
    ## pandasを使用した末尾N行の取得
    # print(df.tail(nlines))
    # newtext.write(str(df.tail(nlines)))
    # newtext.close()