# 作業の手順書

ユーザーは iPad のブラウザだけで作業する。ユーザーに作業をお願いするときは、ここの手順を元に、ボタン名まで具体的に1つずつ伝える。

## A. ヒアリング回答からサイトを作る
1. ユーザーがスプシA列の文章（「以下はホームページ制作のヒアリング回答です…」）を貼る
2. CLAUDE.md のルールどおり、`sites/<slug>/patterns/1〜5/` に5パターン作る（ページ構成の回答に合わせて複数ページ）
   - 5パターン×複数ページは量が多いので、SHISHA cafe CAT と同じく「共通の文章（content.py）＋パターンごとのCSS・演出（patterns.py）＋組み立て（build.py）」の生成プログラムを `tools/<slug>/` に作ると速くて揃う。`tools/shisha-cafe-cat/` をひな形にしてよい
3. 比較ページ `patterns/index.html`（サムネイル付き）と、パターンごとの OGP画像を作る
4. `python3 tools/check_site.py sites/<slug> --shots /tmp/shots` で全ページをチェックし、スクショを見る。「ALL OK」になってから push
5. `sites/index.html` の一覧に追加し、`sites/.assetsignore` は触らない（デモは公開したいので）
6. ユーザーに比較ページのURLと、5パターンの違いを1行ずつ伝える。ヒアリングから気づいた注意点（法律上の表示など）があれば一緒に伝える

## B. 公開中・デモのサイトを直す
- 営業時間・電話・住所・SNS・LINEなど：各サイトの `script.js` 先頭の `SITE` を直す（全ページに反映される）
- タイトル・説明文・OGP：各HTMLの `<head>` を直す
- SHISHA cafe CAT のように生成プログラムがある案件で、全パターン・全ページに関わる変更は `tools/<slug>/` を直して `python3 tools/<slug>/build.py` で作り直す。1か所だけの小さな修正なら、生成されたファイルを直接直してもよい（その場合、生成プログラムにも同じ修正を入れておく）
- 直したら `tools/check_site.py` でチェックしてから push。本番サイトは push すると Cloudflare に自動で反映される（数分）

## C. ヒアリングフォームを直す
- 質問・見た目：`index.html` の `Q` 配列を直して push するだけ（GASがGitHubから読み込む。数分で反映）
  - 質問には列名 `c`（2つ入力の質問は `col`）を付ける。スプシの列は自動で増える
  - 使える仕組み：`type`（radio / check / text / text2 / multi / textarea）、`req`（必須）、`hint`、`other`（その他の入力欄）、`when`（条件付き表示）、`upload`（添付）、`price`（料金表）、`estimate`（費用の目安）
- 保存のしかた（`gas/Code.gs`）を変えたとき：ユーザーにお願いする
  1. Apps Script の `コード.gs` を全部入れ替えて保存（コードは全文をコードブロックで渡す。iPadではファイルを開けない）
  2. 「デプロイ」→「デプロイを管理」→ 鉛筆アイコン → バージョン「新バージョン」→「デプロイ」（URLは変わらない。「新しいデプロイ」を選ぶとURLが変わるので注意）
  3. 新しい権限が必要なときは、関数 `doGet` を一度「実行」して許可（「詳細」→「〜に移動」→「許可」）

## D. 本番公開（独自ドメイン）
1. ドメインを決める（ヒアリングの希望ドメイン）。.com などは Cloudflare Registrar で取れる。.jp／.co.jp は Cloudflare では取れない
2. ユーザーが Cloudflare（会社のアカウントに切り替えて）「ドメインの登録」→「ドメインを登録」で取得。登録期間1年・自動更新オン・登録者は先方の会社
   - 購入後、登録者のメールに届く確認メールのリンクを15日以内に押してもらう（押さないとドメインが止まる）
3. 選ばれたパターンを `sites/<slug>/` 直下にコピー。`wrangler.jsonc`（`name` はプロジェクト名）と `.assetsignore`（`wrangler.jsonc`・`.assetsignore`・`patterns`）を置く
4. ユーザーが Cloudflare で「コンピュート」→「Workers & Pages」→「アプリケーションを作成」→ Gitに接続 → `hp-hearing-form` を選び、次の設定でデプロイ
   - プロジェクト名：`wrangler.jsonc` の `name` と同じ／ビルドコマンド：空欄／デプロイコマンド：`npx wrangler deploy`（そのまま）／プレビュービルド：オフ／詳細設定のパス：`/sites/<slug>`／変数：なし
5. プロジェクトの「ドメイン」タブ →「ドメインを追加」で `ドメイン` と `www.ドメイン` を追加
6. canonical・og:url・og:image・`SITE.url` を本番ドメインに書き換え、`sitemap.xml` と `robots.txt` を置いて push。`sites/.assetsignore` に `/<slug>/` を追加（デモ用URLに本番サイトを出さないため）
7. ユーザーが Google Search Console で「ドメイン」プロパティを追加 → Cloudflare 連携で所有権確認（エラー画面が出てもDNSにTXTが入っていれば「確認」で通る）→ サイトマップ送信 → トップのURLで「インデックス登録をリクエスト」→ 設定から会社のアカウントをオーナーに追加
   - DNSに追加された `google-site-verification` のTXTレコードは消さない

## E. デモ共有用URL（Cloudflare の demo プロジェクト）
- `sites/wrangler.jsonc`（`name: demo`）と `sites/.assetsignore`（一覧・本番・テストを除外）は用意済み
- ユーザー側の作業：会社アカウントで workers.dev のサブドメインを中立的な名前に変更 → `demo` プロジェクトをルート `/sites` で登録
- URLが決まったら：生成プログラムの `BASE` などデモ内の絶対URL（OGP）と CLAUDE.md のデモURLを書き換える

## 注意点（つまずいたところ）
- Cloudflare：メールアドレスの認証が終わるまでメンバーを招待できない。確認メールは期限切れになることがあり、「マイプロフィール」から再送できる
- Cloudflare：Administrator だけではドメインを買えない（Billing が必要）
- 独自ドメインを追加した直後は、iPadが「存在しない」と覚えてしまって開けないことがある → 数分待つ・プライベートタブ・機内モードのオンオフ
- GAS：「このアプリはGoogleで確認されていません」は自分で作ったスクリプトなので「詳細」→「〜に移動」で進んでよい
- 先方のカード情報はLINEで送ってもらわない。先方に直接入力してもらう
