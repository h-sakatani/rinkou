## python3 caliculate_frequency.py address.txtで実行
# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines
import count_string

def cal_freq(filename, newfilename):
    df = count_lines.read_file(filename)
    towns = list(df["town"])
    dict_towns = count_string.count_string(towns)

    # カウント回数の大きいもの順にする
    sorted_dict_town = sorted(dict_towns.items(), reverse=True, key=lambda x: x[1])

    newfile = open(newfilename, "w", encoding="utf-8")
    total = len(towns)
    # print(total)
    for component in sorted_dict_town:
        frequency = component[1]/total
        print (component[0]+ ": frequency is " + str(frequency))
        newfile.write(component[0]+ ": frequency is " + str(frequency)+"\n")
    newfile.close()

    return newfile


# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract second column and caliculate frequency")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="second_column_frequency.txt")

    args = parser.parse_args()

    filename = args.file
    newfilename = args.newfile

    newfile = cal_freq(filename, newfilename)

    
    
    

    ## pandasを使用した頻度計算
    # value_countsはカウントの昇順を出力
    # vc = df["town"].value_counts()
    # total = len(df)
    
    # for i in range(len(vc)):
        # frequency = vc[i]/total
        # print(vc.index[i] + " :frequency is" + str(frequency))
    


