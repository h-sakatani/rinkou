## python3 caliculate.py address.txtで実行
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
    parser = argparse.ArgumentParser(description="extract second column and caliculate frequency")
    parser.add_argument("file", help="file path", type=str)
    #parser.add_argument("--newfile", help="new file name", type=str, default="first_column_list.txt")

    args = parser.parse_args()

    filename = args.file
    #newfilename = args.newfile

    df = read_file(filename)
    towns = list(df["town"])
    

    count = 0
    dict_town = {}
    for town in towns:
        if not town in dict_town:
            dict_town[str(town)] = 1
        else:
            dict_town[str(town)] = dict_town[str(town)] +1
    
    #newfile = open(newfilename, "w", encoding="utf-8")
    total = len(towns)
    # print(total)
    for key, value in dict_town.items():
        frequency = value/total
        print (key+ ": frequency is " + str(frequency))
        # newfile.write(key+ ": frequency is " + str(value/total)+"\n")
    #newfile.close()