# HMMER
- タンパク質ドメインに関する検索を行うプログラム
- 隠れマルコフモデル（Hidden Markov Model: HMM）を利用している

## インストール
### ソースから
- 本家サイトから
- http://hmmer.org/download.html
### apt
```
sudo apt install hmmer
```
- `apt search hmmer`するとhmmer2があるが、こちらは古い。2025年現在の最新バージョンは3.2。
### conda
```
conda install hmmer
```

## 自分でドメインを作成する
### 下準備（最初だけ）
- マルチプルアライメントをとるのでそのためのソフトが必要。今風なのはmafft。もし入ってなければ以下で
```
apt install mafft
```

### 実際の作成
- アミノ酸配列のマルチFASTAファイルを用意する
- マルチプルアライメントを取る
```
mafft input.fasta > aligned.fasta
```
- 独自ドメインを作成する
```
hmmbuild my_domain.hmm aligned.fasta
```
