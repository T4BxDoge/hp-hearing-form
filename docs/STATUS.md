# 現在の状況（作業のたびに更新する）

最終更新：2026-11-19（claude.ai のチャットから Claude Code へ移行）

## 案件ごとの状況

### 株式会社RE.sense — 本番公開済み
- 本番URL：https://resense-inc.com （www付きも可）
- ファイル：`sites/re-sense/`（1ページ完結、問い合わせはLINEのみ）
- 公開：Cloudflare Workers の `resense` プロジェクト（ルート `/sites/re-sense`）
- ドメイン：resense-inc.com（Cloudflare Registrar、RE.sense会社名義、自動更新オン）
- Google Search Console：登録済み（DNSのTXTレコードは消さない）、サイトマップ送信済み
- 公式LINE：https://lin.ee/yh5nDKW （`script.js` の `SITE.lineUrl`）
- 残っていること
  - [ ] PC用のLINE友だち追加QR画像（`sites/re-sense/images/line-qr.png`）。LINE公式アカウントの管理画面からダウンロードしたものを受け取ったら置くだけで、PCではQRが出るようになる
  - [ ] サービスの説明文は制作時の仮の文章のまま（先方の確認待ち）
  - [ ] Googleアナリティクスは未設定（`SITE.gaId` に測定IDを入れれば動く）

### SHISHA cafe CAT — テスト用の案件（5パターンのデモ作成済み）
- 比較ページ（今の確認用URL）：https://t4bxdoge.github.io/hp-hearing-form/sites/shisha-cafe-cat/patterns/
- ファイル：`sites/shisha-cafe-cat/patterns/1〜5/`（各4ページ：トップ・メニュー・料金表・採用情報）
- 生成プログラム：`tools/shisha-cafe-cat/`（文章や構成をまとめて直すときはこれを直して作り直す）
- 残っていること
  - [ ] **デモ共有用URLの設定（作業途中）**：Cloudflare（会社アカウント）で workers.dev のサブドメインを中立的な名前に変更 → `demo` プロジェクト（ルート `/sites`）を登録。ユーザーからURL（`https://demo.〇〇〇.workers.dev`）をもらったら、`tools/shisha-cafe-cat/content.py` の `BASE` と CLAUDE.md のデモURLを書き換えて作り直す
  - [ ] 猫カフェは動物取扱業の登録と、サイトへの登録番号などの表示が必要な可能性がある。先方・保健所への確認待ち（フッターに仮の表示欄あり）

## ヒアリングフォーム
- 稼働中（GASのウェブアプリ。画面はGitHubの `index.html` を毎回読み込む）
- 回答はスプレッドシート「回答」シートに1社1行。A列に Claude に貼る用の文章、写真・ロゴは Googleドライブ「HPヒアリング添付」
- `gas/Code.gs` の最新版は「行の高さを固定」版。ユーザーがApps Scriptに貼り直したかは未確認（スプシのメニュー「ヒアリング」に「行の高さをそろえる」があれば貼り直し済み）

## 保留中のアイデア（ユーザーが「今はいい」と判断したもの）
- お客さんが自分で更新したい場合の「HTML＋スプレッドシートで更新」の仕組み（ヒアリングで「自分で更新したい内容」を聞くところまでは実装済み）
- 公開版サイトのお問い合わせフォームをGASでお店ごとのスプシに送る仕組み（`SITE.formEndpoint` を入れれば送信する作りまでは実装済み）
- `gas/Code.gs` の反映とデプロイの自動化（GitHub Actions＋clasp）：設定が重いので保留。今は手動で貼り直し
