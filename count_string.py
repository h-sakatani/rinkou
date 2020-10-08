## python3 count_string.py address.txtで実行
## --newfile optionでファイル名の指定が可能
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import re
import count_lines

def count_string(strings):
    # 空の辞書型をつくってcityをkeyにカウントしていく
    dict_strings = {}

    for string in strings:
        if not string in dict_strings:
            dict_strings[str(string)] = 1
        else:
            dict_strings[str(string)] = dict_strings[str(string)] + 1
    
    return dict_strings


def count_cities(filename):
    df = count_lines.read_file(filename)
    cities = list(df["city"])
    dict_cities = count_string(cities)
    return dict_cities



# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="count city name")
    parser.add_argument("file", help="file path", type=str)

    args = parser.parse_args()
    
    filename = args.file
    dict_cities = count_cities(filename)

    for key, value in dict_cities.items():
        print (key+ ": count is " + str(value))
    
    
    
    
    
    ##  pandasを用いた文字列のカウント
    # vc = df["city"].value_counts()
    # print(vc)

            
    
    
    



