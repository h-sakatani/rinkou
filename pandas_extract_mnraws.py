# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas
import count_lines

def extract_lines(filename, fromline, toline):
    df = count_lines.read_file(filename)
    print(df[fromline:toline])
    extractlines = df[fromline:toline] 
    return extractlines

def write_lines(filename, fromline, toline, newfilename):
    lines = extract_lines(filename, fromline, toline)
    newtext = lines.to_csv(newfilename)
    return(newtext)

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract first n rows")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("mrows", help="from m rows",type=int)
    parser.add_argument("nrows", help="to n rows",type=int)
    parser.add_argument("--newfile", help="new file name", type=str, default="mn_extract.txt")
    
    args = parser.parse_args()

    filename = args.file
    fromline = args.mrows
    toline = args.nrows
    newfilename = args.newfile

    newtext = write_lines(filename, fromline, toline, newfilename)
   

