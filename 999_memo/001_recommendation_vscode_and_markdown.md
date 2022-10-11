# Visual Studio Code & Markdown で快適な業務環境を整えよう！
- [Visual Studio Code & Markdown で快適な業務環境を整えよう！](#visual-studio-code--markdown-で快適な業務環境を整えよう)
  - [結論: ひとことで言うと](#結論-ひとことで言うと)
  - [背景](#背景)
  - [想定読者](#想定読者)
  - [前提](#前提)
    - [Visual Studio Codeとは？](#visual-studio-codeとは)
    - [Markdownとは？](#markdownとは)
  - [なぜVScodeか](#なぜvscodeか)
  - [なぜMarkdownか](#なぜmarkdownか)
  - [基本編: 書き方 & 操作](#基本編-書き方--操作)
    - [書き方](#書き方)
    - [操作](#操作)
  - [基本編: 拡張機能](#基本編-拡張機能)
      - [Markdown All in One](#markdown-all-in-one)
      - [Markdown Preview Github Styles](#markdown-preview-github-styles)
      - [Insert Date String](#insert-date-string)
      - [Markdown PDF](#markdown-pdf)
  - [応用編: よくある議論 --全て拡張機能で解決--](#応用編-よくある議論---全て拡張機能で解決--)
    - [表の成形が手間じゃない？](#表の成形が手間じゃない)
      - [Text Tables](#text-tables)
      - [Edit csv](#edit-csv)
    - [表計算ができないじゃないか](#表計算ができないじゃないか)
      - [Excel to Markdown table](#excel-to-markdown-table)
    - [図をつくるのにはパワポとかExcel要るんじゃない？](#図をつくるのにはパワポとかexcel要るんじゃない)
      - [Draw.io Integration](#drawio-integration)
      - [Markdown Preview Mermaid Support](#markdown-preview-mermaid-support)
      - [PlantUML](#plantuml)
    - [スライドは?](#スライドは)
      - [Marp for VS Code](#marp-for-vs-code)
  - [結論](#結論)
  - [参考リンク](#参考リンク)
<br><br>

## 結論: ひとことで言うと
Visual Studio Codeとmarkdown形式ファイルを使おう
<br><br>

## 背景
- 筆者はSIerに所属してシステム開発やそのドキュメント作成業務に従事している。
- 業務の中で扱うExcel方眼紙の仕様書フォーマットが嫌すぎてmarkdownについて調べ始めた。
- 調べた結果、思いのほかいろいろなことができるとわかった。
- 有益なので共有する。
<br><br>

## 想定読者
- メモ作成や資料作成がめんどくさいと感じる人
- Excel方眼紙から逃れたい人

## 前提

### Visual Studio Codeとは？
  - 主にプログラム開発に使うテキストエディタ。Microsoftが作っている。
  - 用途や好みに合わせて拡張機能を追加できるようになっている。
  - プログラム開発以外にもいろいろできる。


### Markdownとは？
  - マークアップ言語。つまり、ファイルの書き方のルール。
  - 「めっちゃ簡単なhtml」みたいなコンセプトで作られたらしい。

<br>詳しくはweb検索してね。  
<br><br>


<br>

## なぜVScodeか
- 以下の機能が充実している。活用することで編集効率が高くなる。  
  - ショートカットキー
  - コマンドパレット
  - OSのターミナル(bashやpowershell)
  - 拡張機能

<br>

## なぜMarkdownか  
Markdownファイルはテキストファイルであることから、以下の特長がある。  
- 軽い
- バージョン管理が楽(Gitを使える)
  - 「仕様書_20221001_最終版_修正後ver_修正02.xlsx」みたいなファイル名を付けずに済む。
  - 修正箇所を赤字にしたりする必要がない。
- 書式設定に気を配る必要がない
  - 「フォントがこの部分だけ違う」が発生しない。
  - 「罫線が切れてる」が発生しない。
  - 「オブジェクトの位置や大きさがちょっとズレてる」が発生しない。
<br><br>

## 基本編: 書き方 & 操作
### 書き方
- 見出しは行のはじめに`# `を入力する。記号の後の半角スペースを忘れないように注意。
- 箇条書きは行のはじめを`- `で入力する。記号の後の半角スペースを忘れないように注意。
- 改行は半角スペース2つ、または`<br>`を入力する。
- ファイル名の拡張子は`.md`とする。
### 操作
- `ctrl + shift + v` : プレビューを表示
- `ctrl + k`の後で`v` : プレビューを編集画面と並べて表示  

<br><br>
本当は初級編で覚えるべきことはもっとあるが、とりあえずこれだけ覚えて慣れるのがオススメ。  
<br><br>

## 基本編: 拡張機能
markdownを使い始めたら、まずは箇条書きメモとかを作るといいと思う。  
その際に役立つ拡張機能は以下の通り。  
#### Markdown All in One
- 自動補完してくれる。
- 目次を作れる。
#### Markdown Preview Github Styles
- プレビューをいい感じにしてくれる。
- デフォルトのプレビューは黒い背景に白い文字だが、<br>この拡張機能を使うと白い背景に黒い文字を選べる。
- 動作が軽い。
- 込み入った箇条書きの報連相をしたいときによい。<br>以下の順番でやると、チャットだけでやる場合よりもラクチン。
  - VScode上でmarkdown形式でメモを作成する
  - プレビューを表示する
  - プレビューをコピーして社内チャットに貼り付ける
#### Insert Date String
- ショートカットキーで現在の日付時刻を入力できる。  
- markdownは関係ない。
- 作業ログつける場合などに便利。
#### Markdown PDF
- markdownをPDF形式にエクスポートする。
- ちなみに、PDF出力時の改ページをしたい場合は以下を記載する。
  -  `<div style="page-break-before:always"></div>`
  -  この拡張機能に限らず使えるらしい。
<br><br>

## 応用編: よくある議論 --全て拡張機能で解決--  

ここまでで取り上げたMarkdown単体の表現力だと、正直心もとない。  
しかし、以下の拡張機能を使えば様々なドキュメント作成にも耐えうる表現力を得られる。<br>  

### 表の成形が手間じゃない？
その通り。markdownの表を作るのは見づらいし、めんどくさい。  拡張機能を使おう。  

#### Text Tables
- スペースとかをいい感じにして、列をそろえてくれる。編集画面でも読みやすくしてくれる。
- 行の追加をラクにしてくれる。
- ただし、全角文字には対応していない模様。
#### Edit csv
- csvをテーブル形式で表示/編集する。
- markdownは関係ない。
<br><br>

### 表計算ができないじゃないか
そう、できない。PythonとかSQLでがんばれ。pandasは`to_markdown`なんてのもあるし。<br><br>
「コード書くの？嫌だよ。やっぱりExcel使うわ」というそこのあなた、<br>Excelからmarkdownにコピペしたら問題解決！  
そのための拡張機能、ありますぜ。

#### Excel to Markdown table
- Excelの表をmarkdownにコピペする際に、markdownの表形式に変換してくれる。

<br>

### 図をつくるのにはパワポとかExcel要るんじゃない？
できる！！拡張機能を使おう。  フロー図もガントチャートもそのほか大体できる。  <br><br>
以下の拡張機能で作成した図はいずれもテキスト形式で保存できる。  
テキスト形式で保存できるということは、gitでバージョン管理できる。便利！

#### Draw.io Integration
- ドラッグアンドドロップで直感的に作図できる。
- ファイルサイズはでかい。
#### Markdown Preview Mermaid Support
- ガントチャートが作りやすい。
- 大体何の図を作ってもコンパクトにできる。
#### PlantUML
- (作成中: 使ったことがないのでわからない。使ったら追記する。)
- Javaがインストールされていることが必要らしい。
<br><br>


### スライドは?
できる！！拡張機能を使おう。<br><br>
簡単にできる範囲だとすこし味気ない気もするが、社内説明用の資料とかならよかろう。  
複雑なデザインの設定はcssを使うとできる。<br><br>
上述の図の作成と同じく、テキスト形式で保存できる。だから、gitでバージョン管理できる。便利！
#### Marp for VS Code
- markdown形式のファイルをスライドに変換できる
- 通常のmarkdownファイルと同じく、画像や図の埋め込みも、もちろん対応可能  
<br>

## 結論
資料作成の際、VS codeとmarkdownファイルの組み合わせを使うことが超おすすめ。  
個人的にはOfficeソフトよりも便利だと感じる。
<br><br>

## 参考リンク
- [行政文書をマークダウン化しよう！ところでマークダウンって何？](https://metidx-gov.note.jp/n/n2bd18b23dba3) 
- [Markdown記法 チートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)
- [ExcelやGoogleスプレッドシートをMarkdown出力するVS Codeの拡張機能「Excel to Markdown table」が便利すぎる件](https://dev.classmethod.jp/articles/excel-to-markdown-table/)
- [VSCode上のマークダウン とDraw.ioでドキュメントを作成する](https://qiita.com/oruharo/items/f5bdeedad28731da1b11)
- [Mermaid記法の書き方（Markdownテキストでチャート・グラフが描ける）](https://notepm.jp/help/mermaid)
- [【VS Code + Marp】Markdownから爆速・自由自在なデザインで、プレゼンスライドを作る](https://qiita.com/tomo_makes/items/aafae4021986553ae1d8)

<br><br><br>

おわり

