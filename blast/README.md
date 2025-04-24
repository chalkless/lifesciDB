# BLAST

## インストール
### apt
- Ubuntu など

### conda
- 2025年4月現在 2.16が入るようだ
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
$ blastp -query query.fasta -db blast.db -num_threads 8 -max_target_seqs 3 -outfmt 6 | tee blast.rslt.tab
```
  - -max_target_seqs: いくつまでヒットを出力するか。1にするとトップヒットと思われていたがそうでもないらしい
  - -outfmt 6: タブ区切り

- タブ区切り
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
  - -hash_index: 高速化のためにindex作成
  - -parse_seqids: これをつけると配列名で検索できるようになる

- UniProtからの生物種を区切ったダウンロード
  - UniProtのページに行く https://www.uniprot.org/
  - 見たいデータベースのページへ（UniProt KBとか）
  - 左カラムに生物種を入れるフォームが。もしくはView byからTaxonomy
  - View byから行くと上から見慣れない分類名をたどることになるので、とりあえず見たい分類の下位の何かを入れて、結果の分類treeからそれなりのところを選ぶのがよさそう。

- 配列のサブセット作成
```
$ blastdbcmd -db blast.db -entry_batch target.ids.txt | tee target.fasta
```

- UniProt のヘッダから遺伝子名を抜き出すなど
```
[キモ]
    $name_out =~ s/ (SV|PE|GN|OX)=.*//g;
    $name_out =~ s/OS=(.*)//;
    $taxon = $1;
```

