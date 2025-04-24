# BLAST

## インストール
### NCBIのサイトからダウンロード
- https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
- Win版、Mac版、Linux版、ソースなど
- 2025年4月現在 2.16.0

### apt
- Ubuntu など
- 2025年4月現在 2.12.0
```
$ apt install ncbi-blast+
```

### conda
- 2025年4月現在 2.16.0が入るようだ
```
# BLAST用に仮想環境をつくるなら
$ conda create -n blast
$ conda activate blast

# 実際のインストール（プロンプトの部分 (blast) $ は気にしなくていい）
(blast) $ conda install bioconda::blast

# 試しに動作確認
$ blastn
BLAST query/options error: Either a BLAST database or subject sequence(s) must be specified
Please refer to the BLAST+ user manual.
（ミスっていると コマンドが見つかりません と出てくる）
```


## BLASTの実行

```
$ blastp -query query.fasta -db blast.db -num_threads 8 -max_target_seqs 3 -outfmt 6 -out blast.rslt.tab
```
  - -query: BLASTしたい配列ファイル。普通はMultiFASTAファイル
  - -db: BLASTで当てたいデータベース。makeblastdb（後述）で作成。DB自体は拡張子が付いているが、ここでは拡張子をつけない。`db/bast.db`のように別ディレクトリ指定可能
  - -num_threads: （optional）利用スレッド数
  - -max_target_seqs: （optional）いくつまでヒットを出力するか。1にするとトップヒットと思われていたがそうでもないらしい
  - -outfmt 6: タブ区切り
  - -out: 結果ファイル名。これをつけずに`|tee blast.rslt.tab`とやって流れる画面を眺めてもいいし、さらにlessで受けてもいい（けど表示の分、時間はかかる）

### BLASTの結果：タブ区切り時
```
1. query acc.ver
2. subject acc.ver
3. % identity
4. alignment length
5. mismatches
6. gap opens
7. q. start
8. q. end
9. s. start
10. s. end
11. evalue, 
12. bit score
```

## BLASTのデータベース作成
```
$ makeblastdb -in original.fasta -out blast.dbname -dbtype [nucl|prot] -hash_index -parse_seqids
```
  - -in: DB化したいMultiFASTAファイル名
  - -out: 作成されるDB名。blastnとかで実際にBLASTするときにDB名として指定する。実際はこのDB名に拡張子がつけられたファイルが複数できる。
  - -dbtype: nucl（塩基）かprot（アミノ酸）か
  - -hash_index: 高速化のためにindex作成
  - -parse_seqids: これをつけると配列名で検索できるようになる（後述）

## サブセットの配列作成：BLASTデータベースの応用編
```
$ blastdbcmd -db blast.db -entry_batch target.ids.txt | tee target.fasta
```

```
（あるIDの配列を取得する場合）
$ blastdbcmd -db blast.db -entry id_name | tee id_name.fasta
```


