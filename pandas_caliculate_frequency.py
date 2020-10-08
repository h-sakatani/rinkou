# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def frequency(filename, newfilename):
    df = count_lines.read_file(filename)
    vc = df["town"].value_counts()
    total = len(vc)

    text = open(newfilename, "w", encoding="utf-8")

    for i in range(total):
        frequency = vc[i]/total
        print(vc.index[i] + " :frequency is" + str(frequency))
        text.write(vc.index[i]+ ": frequency is " + str(frequency)+"\n")
    text.close()

    return text




# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("--newfile", help="new file name", type=str, default="first_column_list.txt")

    args = parser.parse_args()

    filename = args.file
    newfilename = args.newfile
    
    newtext = frequency(filename, newfilename)
    
    