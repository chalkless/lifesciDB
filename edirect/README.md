# NCBI Entrez Direct
- NCBIはデータベースにアクセスするためのAPIであるeutilsを公開しているが、もっと大規模にデータベースからダウンロードなどを行うためのコマンドであるEntrez Directを提供している。
- Document: https://www.ncbi.nlm.nih.gov/books/NBK179288/
- ファイル群： https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/
  - 整理されていないのであまり見ない方がいい
  - たとえば、edirect-install.sh と install-edirect.sh の両方があったり。どっちやねん

## インストール
### Ubuntuの場合
```
$ sudo apt install ncbi-entrez-direct
```

### 自分でインストールする場合
- ドキュメントには以下のように書いてある
```
# example 1
$ sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```
```
# example 2
$ sh -c "$(wget -q https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -O -)"
```
- 普通にcurlとかwgetでいいんじゃねーかとか思ったのだが、そのまま試してみたらインストールプログラムが走り始めて`echo "export PATH=/home/XXX/edirect:\${PATH}" >> ${HOME}/.bashrc`とか言いやがった。
- プログラム114個もあるし
- 試しにwgetしてみる（wgetに関して言えば、−qは画面出力しないquietのオプションなので、この辺はまったくつけずにwget [url]でOK）
- install-edirect.shを見たところ、`cd ~`がハードコードされていたのでここを書き換えて自分の好みのディレクトリにインストールされるようにする（ここで指定したディレクトリにedirectのディレクトリが作られてそこにインストールされる）
- pathを通すか訊いてくるので、そこは素直にお任せすることとする


