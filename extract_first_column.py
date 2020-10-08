## python3 extract_first_column.py address.txtで実行
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def extract_first_column(filename, newfilename):
    df = count_lines.read_file(filename)
    city = list(df["city"])
    city_list = list(set(city)) #  重複を除く

    newtext = open(newfilename, "w", encoding="utf-8")

    for i in range(len(city_list)):
        newtext.write(str(city_list[i])+"\n")
        print(str(city_list[i])+"\n")
    newtext.close()

    return newtext


# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first column components")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="first_column_list.txt")

    args = parser.parse_args()

    filename = args.file
    newfilename = args.newfile

    newtext = extract_first_column(filename, newfilename)

    

    ## pandasを使用した1列目の重複無し文字列のファイル出力
    # cities = df["city"].unique()
    # with open(newfilename, mode="w") as f:
        # f.write('\n'.join(cities)) # 改行コードとjoinメソッドで書き込み