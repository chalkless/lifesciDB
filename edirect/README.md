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

## 使う前に
- 基本的には esearch | efetch （実際は引数がつく）のようにパイプでつなぐが、最高のパフォーマンスを得るにはNCBI_API_KEYを取得して.bash_profileや.zshrcに設定しておく（ https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/README より）
```
export NCBI_API_KEY=unique_api_key
```
- NCBI_API_KEYの取得法： https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/
- NCBI account にログインする。アカウントがないときはORCIDでもGoogleでもログインできる
- My NCBIが開く。左上の自分の名前をクリックしてAccount Settings
- 500　internal server error が出ることもあるが、しばらくして再度トライする
- NCBI Account Settingのページの一番下にAPI Key Managementのセクションがあり、Create an API Key というボタンが出る。クリックするとAPI_KEYが作られる
- 参考までにeutilsで`api_key=XXX`をつけると１秒間に3回のリクエストが10回まで拡張される
  - BioPythonで指定するとき：https://github.com/chalkless/biopython_my/blob/master/biopyPubmed.md

## 使い方
### PubMedからの文献のダウンロード
```
# 検索語を入れてその文献をXMLでダウンロード
$ esearch -db pubmed -query "opsin gene conversion" | efetch -format xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE PubmedArticleSet PUBLIC "-//NLM//DTD PubMedArticle, 1st January 2023//EN" "https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_230101.dtd">
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation Status="MEDLINE" Owner="NLM" IndexingMethod="Curated">
      <PMID Version="1">36707759</PMID>
      <DateCompleted>
        <Year>2023</Year>
        <Month>02</Month>
        <Day>03</Day>
      </DateCompleted>
      ...
      <PublicationStatus>ppublish</PublicationStatus>
      <ArticleIdList>
        <ArticleId IdType="pubmed">3270843</ArticleId>
      </ArticleIdList>
    </PubmedData>
  </PubmedArticle>
</PubmedArticleSet>
```
