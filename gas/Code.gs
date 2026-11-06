// ホームページ制作ヒアリング — GAS本体
// フォームの画面（index.html）はGitHubから毎回読み込むので、
// 質問や見た目の修正はGitHub側を直すだけで反映されます。
// このファイルを変えたときだけ、Apps Scriptに貼り直してください。

const SHEET_NAME = '回答';
const ROOT_FOLDER_NAME = 'HPヒアリング添付';
const FORM_URL = 'https://raw.githubusercontent.com/T4BxDoge/hp-hearing-form/main/index.html';

const HEADERS = [
  '送信日時', '会社名', '担当者名',
  'Q2 目的', 'Q3 見てほしい人', 'Q4 年代', 'Q5 雰囲気', 'Q6 色',
  'Q7 ロゴ', 'Q8 写真', 'Q9 載せたいページ', 'Q10 機能', 'Q11 更新担当',
  'Q12 スマホ/PC', 'Q13 参考サイト', 'Q14 公開時期', 'Q15 予算',
  '写真フォルダ'
];

// フォームの画面を表示（GitHubの最新版 → 読めなければ直前の版 → Apps Script内の index）
function doGet() {
  const html = loadFormHtml_();
  const out = html
    ? HtmlService.createHtmlOutput(html)
    : HtmlService.createHtmlOutputFromFile('index');
  return out
    .setTitle('ホームページ制作ヒアリング')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover');
}

function loadFormHtml_() {
  const cache = CacheService.getScriptCache();
  try {
    // 1分ごとに変わるクエリを付けて、GitHub側の古いキャッシュを避ける
    const bust = Math.floor(Date.now() / 60000);
    const res = UrlFetchApp.fetch(FORM_URL + '?v=' + bust, { muteHttpExceptions: true });
    if (res.getResponseCode() === 200) {
      const text = res.getContentText('UTF-8');
      if (text.indexOf('<form') !== -1) {
        if (text.length < 95000) cache.put('form_html', text, 21600);
        return text;
      }
    }
  } catch (e) {
    console.warn('GitHubから読み込めませんでした: ' + e);
  }
  return cache.get('form_html');
}

// フォームから呼ばれる：写真を1枚ずつ保存
function uploadFile(folderKey, name, mimeType, base64) {
  if (!/^image\//.test(mimeType)) throw new Error('画像ファイルのみ送信できます');
  const bytes = Utilities.base64Decode(base64);
  if (bytes.length > 15 * 1024 * 1024) throw new Error('ファイルが大きすぎます（15MBまで）');
  const folder = getSubmissionFolder_(folderKey);
  const blob = Utilities.newBlob(bytes, mimeType, String(name).slice(0, 100));
  folder.createFile(blob);
  return true;
}

// フォームから呼ばれる：1回答を1行追加
function submitAnswer(data) {
  if (!data || !data.company || !Array.isArray(data.answers)) {
    throw new Error('回答の形式が正しくありません');
  }
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const sheet = getSheet_();
    let folderUrl = '';
    if (data.folderKey) {
      const it = getRootFolder_().getFoldersByName(cleanKey_(data.folderKey));
      if (it.hasNext()) folderUrl = it.next().getUrl();
    }
    const answers = data.answers.slice(0, 14);
    while (answers.length < 14) answers.push('');
    const row = [new Date(), data.company, data.name || '']
      .concat(answers)
      .map(v => safe_(v))
      .concat([folderUrl]);
    sheet.appendRow(row);
  } finally {
    lock.releaseLock();
  }
  return true;
}

// 「回答」シートがなければ作る。見出しが足りなければ付け直す
function getSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  if (sheet.getLastColumn() < HEADERS.length) {
    sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function getRootFolder_() {
  const it = DriveApp.getFoldersByName(ROOT_FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(ROOT_FOLDER_NAME);
}

function getSubmissionFolder_(key) {
  const root = getRootFolder_();
  const name = cleanKey_(key);
  const it = root.getFoldersByName(name);
  return it.hasNext() ? it.next() : root.createFolder(name);
}

function cleanKey_(key) {
  return String(key || '').replace(/[\\\/:*?"<>|]/g, '').slice(0, 80) || '名称未設定';
}

// = や + で始まる入力が数式として動かないようにする
function safe_(v) {
  if (v instanceof Date) return v;
  const s = String(v == null ? '' : v).slice(0, 2000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
