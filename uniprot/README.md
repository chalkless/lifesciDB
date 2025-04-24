# UniProt
## 生物種を区切ったダウンロード
- UniProtのページに行く https://www.uniprot.org/
- Proteins 欄のReviewedなどを選ぶ
- 左カラムでFilter by taxonomy
- 生物名を入れる。候補リストでサジェストされるので選択
- 全部? 圧縮する? など聞かれる。Top 10を見ることもできる
- Download でデータがダウンロードされる

## UniProt のヘッダから遺伝子名を抜き出すなど
```
[キモ]
    $name_out =~ s/ (SV|PE|GN|OX)=.*//g;
    $name_out =~ s/OS=(.*)//;
    $taxon = $1;
```

