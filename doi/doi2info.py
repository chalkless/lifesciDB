import csv
import time
import requests

# --- 設定項目 ---
INPUT_FILE = "dois.txt"  # 入力ファイル名（1行に1 DOI）
OUTPUT_FILE = "output.tsv"  # 出力ファイル名（タブ区切り）
EMAIL = "your_email@example.com"  # API利用マナー用の連絡先メールアドレス
SLEEP_TIME = 0.2  # 1件ごとの待機時間（秒）。アクセス制限防止


def clean_text(text) -> str:
  """タブ区切り形式が崩れないよう、改行やタブをスペースに置換する"""
  if text is None:
    return ""
  return (
      str(text)
      .replace("\t", " ")
      .replace("\n", " ")
      .replace("\r", "")
      .strip()
  )


def get_paper_metadata(doi: str) -> dict:
  """DOIから書誌情報とPMID・PMCIDを取得する"""
  # URLプレフィックス等が付いている場合は除去して純粋なDOIにする
  clean_doi = (
      doi.replace("https://doi.org", "")
      .replace("http://doi.org", "")
      .replace("doi:", "")
      .strip()
  )

  result = {
      "doi": clean_doi,
      "title": "",
      "publisher": "",
      "year": "",
      "pmid": "",
      "pmcid": "",
  }

  headers = {"User-Agent": f"MetadataFetcher/1.0 (mailto:{EMAIL})"}

  # 1. Crossref REST API からタイトル・出版社・発行年を取得
  crossref_url = f"https://crossref.org{clean_doi}"
  try:
    res = requests.get(crossref_url, headers=headers, timeout=10)
    if res.status_code == 200:
      data = res.json().get("message", {})

      titles = data.get("title", [])
      result["title"] = clean_text(titles[0]) if titles else ""
      result["publisher"] = clean_text(data.get("publisher"))

      published = (
          data.get("published")
          or data.get("published-print")
          or data.get("published-online")
      )
      if published and "date-parts" in published:
        # date-parts は [[2020, 8, 26]] のような2次元リストのため先頭の「年」を取得
        result["year"] = str(published["date-parts"][0][0])
  except requests.RequestException as e:
    print(f"[Crossref エラー] {clean_doi}: {e}")

  # 2. NCBI ID Converter API から PMID と PMCID を取得
  ncbi_url = "https://nih.gov"
  params = {
      "ids": clean_doi,
      "format": "json",
      "tool": "my_python_script",
      "email": EMAIL,
  }
  try:
    res = requests.get(ncbi_url, params=params, timeout=10)
    if res.status_code == 200:
      records = res.json().get("records", [])
      if records and "errmsg" not in records[0]:
        result["pmid"] = str(records[0].get("pmid", ""))
        result["pmcid"] = str(records[0].get("pmcid", ""))
  except requests.RequestException as e:
    print(f"[NCBI エラー] {clean_doi}: {e}")

  return result


def main():
  # 入力ファイルの読み込み（空行はスキップ）
  try:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
      dois = [line.strip() for line in f if line.strip()]
  except FileNotFoundError:
    print(f"エラー: 入力ファイル '{INPUT_FILE}' が見つかりません。")
    return

  total = len(dois)
  print(f"全 {total} 件のDOIを処理します...")

  # タブ区切り（TSV）で出力
  with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    # ヘッダー行の書き込み
    writer.writerow(["DOI", "論文タイトル", "出版社", "発行年", "PMID", "PMCID"])

    for idx, doi in enumerate(dois, start=1):
      print(f"[{idx}/{total}] 取得中: {doi}")
      info = get_paper_metadata(doi)
      writer.writerow([
          info["doi"],
          info["title"],
          info["publisher"],
          info["year"],
          info["pmid"],
          info["pmcid"],
      ])
      # APIサーバーへの負荷軽減のため待機
      time.sleep(SLEEP_TIME)

  print(f"完了しました！結果は '{OUTPUT_FILE}' に保存されています。")


if __name__ == "__main__":
  main()
