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

## データの中身
```
genus_name	sp_epithet	subsp_epithet	reference	status	authors	address	risk_grp	nomenclatural_type	record_no	record_lnk
Abditibacterium	utsteinense		Oren A, Garrity GM. Validation list no. 184. List of new names and new combinations previously effectively, but not validly, published. Int J Syst Evol Microbiol 2018; 68:3379-3393.	VL; sp. nov.; validly published under the ICNP; correct name	Tahon et al. 2018	https://lpsn.dsmz.de/species/abditibacterium-utsteinense		DSM 105287; LMG 29911; R-68213	797965	
Abditibacterium			Oren A, Garrity GM. Validation list no. 184. List of new names and new combinations previously effectively, but not validly, published. Int J Syst Evol Microbiol 2018; 68:3379-3393.	VL; gen. nov.; validly published under the ICNP; correct name	Tahon et al. 2018	https://lpsn.dsmz.de/genus/abditibacterium		797965	520424	
Abiotrophia	adiacens		Kawamura Y, Hou XG, Sultana F, Liu S, Yamamoto H, Ezaki T. Transfer of Streptococcus adjacens and Streptococcus defectivus to Abiotrophia gen. nov. as Abiotrophia adiacens comb. nov. and Abiotrophia defectiva comb. nov., respectively. Int J Syst Bacteriol 1995; 45:798-803.	VP; comb. nov.; validly published under the ICNP; synonym	(Bouvet et al. 1989) Kawamura et al. 1995	https://lpsn.dsmz.de/species/abiotrophia-adiacens	2	ATCC 49175; CCUG 27637; CCUG 27637 A; CCUG 27809; CIP 103.243; DSM 9848; GaD; LMG 14496; NCTC 13000	772466	776611
Abiotrophia	balaenopterae		Lawson PA, Foster G, Falsen E, Sjoden B, Collins MD. Abiotrophia balaenopterae sp. nov., isolated from the minke whale (Balaenoptera acutorostrata). Int J Syst Bacteriol 1999; 49:503-506.	VP; sp. nov.; validly published under the ICNP; synonym	Lawson et al. 1999	https://lpsn.dsmz.de/species/abiotrophia-balaenopterae	2	ATCC 700813; CCUG 37380; CIP 105938; DSM 15827; M1975/96/1	772467	776612
Abiotrophia	defectiva		Kawamura Y, Hou XG, Sultana F, Liu S, Yamamoto H, Ezaki T. Transfer of Streptococcus adjacens and Streptococcus defectivus to Abiotrophia gen. nov. as Abiotrophia adiacens comb. nov. and Abiotrophia defectiva comb. nov., respectively. Int J Syst Bacteriol 1995; 45:798-803.	VP; comb. nov.; validly published under the ICNP; correct name	(Bouvet et al. 1989) Kawamura et al. 1995	https://lpsn.dsmz.de/species/abiotrophia-defectiva	2	ATCC 49176; CCUG 27639; CCUG 27804; CIP 103.242; DSM 9849; GIFU 12707; LMG 14740; SC 10	772468	
Abiotrophia	elegans		Anonymous. Validation list no. 68. Validation of publication of new names and new combinations previously effectively published outside the IJSB. Int J Syst Bacteriol 1999; 49:1-3.	VL; sp. nov.; validly published under the ICNP; synonym	Roggenkamp et al. 1999	https://lpsn.dsmz.de/species/abiotrophia-elegans	2	ATCC 700633; B 1333; CCUG 38949; CIP 105513; DSM 11693	772469	776613
Abiotrophia			Kawamura Y, Hou XG, Sultana F, Liu S, Yamamoto H, Ezaki T. Transfer of Streptococcus adjacens and Streptococcus defectivus to Abiotrophia gen. nov. as Abiotrophia adiacens comb. nov. and Abiotrophia defectiva comb. nov., respectively. Int J Syst Bacteriol 1995; 45:798-803.	VP; gen. nov.; validly published under the ICNP; correct name	Kawamura et al. 1995	https://lpsn.dsmz.de/genus/abiotrophia	2	772468	514986	
Absicoccus	porci		Shin Y, Paek J, Kim H, Kook JK, Kim JS, Kim SH, Chang YH. Absicoccus porci gen. nov., sp. nov., a member of the family Erysipelotrichaceae isolated from pig faeces. Int J Syst Evol Microbiol 2020; 70:732-737.	VP; sp. nov.; validly published under the ICNP; correct name	Shin et al. 2020	https://lpsn.dsmz.de/species/absicoccus-porci		JCM 32769; KCTC 15747; YH-panp20	5758	
Absicoccus			Shin Y, Paek J, Kim H, Kook JK, Kim JS, Kim SH, Chang YH. Absicoccus porci gen. nov., sp. nov., a member of the family Erysipelotrichaceae isolated from pig faeces. Int J Syst Evol Microbiol 2020; 70:732-737.	VP; gen. nov.; validly published under the ICNP; correct name	Shin et al. 2020	https://lpsn.dsmz.de/genus/absicoccus		5758	4948	
...
```

## API
- https://api.lpsn.dsmz.de/?pk_vid=0c1c9ad3794908d01733845731c387c3
- https://lpsn.dsmz.de/text/lpsn-api



