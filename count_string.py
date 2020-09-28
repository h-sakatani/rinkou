## python3 tabs_to_spaces.py address.txtで実行
## --newfile optionでファイル名の指定が可能
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import re

def read_file(path):
    # textファイル1列目がcity,2列目がtownと指定
    df = pandas.read_table(path, names=["city", "town"])
    return df


# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="count city name")
    parser.add_argument("file", help="file path", type=str)

    args = parser.parse_args()
    
    filename = args.file
    
    # 重複の無いcity名前のリストを作成
    df = read_file(filename)
    cities = list(df["city"])
    
    # 空の辞書型をつくってcityをkeyにカウントしていく
    count = 0
    dict_city = {}
    for city in cities:
        if not city in dict_city:
            dict_city[str(city)] = 1
        else:
            dict_city[str(city)] = dict_city[str(city)] +1
    
    for key, value in dict_city.items():
        print (key+ ": count is " + str(value))

            
    
    
    



