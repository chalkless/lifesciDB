# LPSN (List of Prokaryotic names with Standing in Nomenclature)
- https://www.bacterio.net/
- https://lpsn.dsmz.de/
- 原核生物の学名リスト

## データのダウンロード
- サイトの左カラムに Downloads とある
- ログイン画面が出る。Googleアカウントでログインできる
- https://lpsn.dsmz.de/downloads
- ファイルへのリンクがあるが、そのURLでwgetしてもログインしろと言われる
- 最新の日付でCSVとExcel形式（と称するもの）のファイルがある
  - lpsn_gss_2024-04-10.csv
  - lpsn_gss_2024-04-10.xls
- Excel形式のものは実は中身はタブ区切りファイルである。。。（まぁ不慣れな人はExcelで開くけどさ。それはCSVも同じか。。。）
```
$ file lpsn_gss_2024-04-08.csv
lpsn_gss_2024-04-08.csv: UTF-8 Unicode text, with very long lines
$ file lpsn_gss_2024-04-08.xls
lpsn_gss_2024-04-08.xls: UTF-8 Unicode text, with very long lines, with CRLF line terminators
```
- 人名が入っているので文字コードが特殊と伝説で言われているが、途中でExcelで開いたりして確認しているからかもしれない。

## API
- https://api.lpsn.dsmz.de/?pk_vid=0c1c9ad3794908d01733845731c387c3
- https://lpsn.dsmz.de/text/lpsn-api



