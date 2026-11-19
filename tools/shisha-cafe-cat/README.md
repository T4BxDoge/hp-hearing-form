# SHISHA cafe CAT の生成プログラム

`sites/shisha-cafe-cat/patterns/` の5パターン×4ページを作るプログラム。

| ファイル | 役割 |
|---|---|
| `content.py` | 全パターン共通の文章・ページ構成・ヘッダー・フッター。`BASE` はデモのURL |
| `patterns.py` | パターン1〜5の名前・説明・書体・トップの見せ方・CSS・トップの演出（canvas） |
| `base.css` | 全パターン共通のCSSの土台 |
| `core.js` | 全パターン共通のJS（`SITE` のお店情報、スクロール演出、メニュー、canvas描画の共通処理など） |
| `build.py` | 上を組み立てて `patterns/1〜5/` を作る |
| `ogp.py` | パターンごとのOGP画像と、比較ページ用のサムネイルを作る（Playwright） |
| `compare.py` | 比較ページ `patterns/index.html` を作る |

作り直す手順（リポジトリの一番上で）：

```
python3 tools/shisha-cafe-cat/build.py
python3 tools/shisha-cafe-cat/ogp.py      # 見た目を変えたとき（OGP画像とサムネイルを作り直す）
python3 tools/shisha-cafe-cat/compare.py
python3 tools/check_site.py sites/shisha-cafe-cat
```
