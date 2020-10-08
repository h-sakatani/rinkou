# 輪講 #

----

## お題1　ファイルの行数をカウントする(pandas使用) ##

例
 ``count_lines.py address.txt ``


## お題2　タブをスペースに置換したファイルを出力 ##

例
 ``tabs_to_spaces.py address.txt --newfile newfilename.txt``

オプションで`--newfile`を指定することでファイル名の指定が可能<br>
指定なしではnew.txtを出力


## お題3　自然数Nをコマンドライン引数にとり、入力のうち先頭のN行を出力 ##

例
``first_nrows.py address.txt 3 --newfile newfile.txt``

オプションで`--newfile`を指定することでファイル名の指定が可能<br>
defaltではfirst_nlines.txtを出力

## お題4　自然数Nをコマンドライン引数にとり、入力のうち末尾のN行を出力 ##

例
``last_nrows.py address.txt 5 --newfile newfile.txt``

オプションで`--newfile`を指定することでファイル名の指定が可能<br>
defaltではlast_nlines.txtを出力


## お題5　1列目の文字列を集計して標準出力する ##

例
``count_string.py address.txt``<br>


## お題6 自然数M,Nをコマンド引数にとり、入力のうちM行目からN行目までを出力する ##

例
``extract_mnraws.py　address.txt 5 10 --newfile.txt``

オプションで`--newfile`を指定することでファイル名の指定が可能<br>
defaltではlast_nlines.txtを出力


## お題7 1列目だけファイルに出力する ##

例
``extract_first_column.py address.txt``


## お題8　各行2列目の文字列の出現頻度を求めて、出現頻度の高い順にソートして標準出力する　

例
`caliculate_frequency.py address.txt`

###`pandas_`が記載されているスクリプトはpandasで書き換えたスクリプト###

## 参考 ##
https://github.com/icoxfog417/python_training
