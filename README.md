# 請求書自動作成システム

DjangoとSQLiteを使用した請求書自動作成システムです。

## 機能

- **ユーザー管理**: 責任者/管理者/一般の3種類のユーザー種別
- **ログイン機能**: ユーザー名とパスワードによる認証
- **管理画面**: 取引先会社追加、請求書項目追加、ユーザー管理（責任者のみ）
- **請求書作成**: 会社コード入力による自動入力、10セットの請求内訳入力
- **取引履歴出力**: 月ごとの取引履歴をExcelファイルに出力

## セットアップ

1. 必要なパッケージをインストール：
```bash
pip install Django openpyxl
```

2. データベースのマイグレーション：
```bash
cd invoice_automation
python manage.py makemigrations
python manage.py migrate
```

3. 初期ユーザーを作成（責任者）：
```bash
python manage.py createsuperuser
```
または、Djangoシェルで：
```bash
python manage.py shell
```
```python
from invoices.models import CustomUser
user = CustomUser.objects.create_user('admin', 'password123', role='director')
```

4. 開発サーバーを起動：
```bash
python manage.py runserver
```

5. ブラウザでアクセス：
- ログイン画面: http://127.0.0.1:8000/login/
- 管理画面: http://127.0.0.1:8000/admin/ (Django管理画面)

## 使い方

### 1. ログイン
- ログイン画面でユーザー名とパスワードを入力
- 責任者/管理者は管理画面に遷移
- 一般ユーザーは請求書作成画面に遷移

### 2. 管理画面（責任者/管理者）
- **取引先会社追加**: 会社コード、会社名、担当者、住所などの情報を登録
- **請求書項目追加**: 請求書で使用する項目テンプレートを追加
- **ユーザー管理**（責任者のみ）: 新しいユーザーの追加・削除

### 3. 請求書作成
- 会社コードを入力すると、自動的に会社情報が表示されます
- 請求書番号を入力
- 請求内訳を入力（最大10セット、スクロール可能）
  - 請求内容、個数、単価を入力すると金額が自動計算されます
- 「請求書作成」ボタンをクリックすると、Excelファイルがダウンロードされます
- ファイル名: `invoice_会社名_会社コード_請求書番号.xlsx`

### 4. 取引履歴出力
- 会社コード、年、月を選択
- 「取引履歴を出力」ボタンをクリック
- ファイル名: `invoice_会社名_会社コード_何年何月分.xlsx`

## ユーザー種別

- **責任者**: すべての機能にアクセス可能、ユーザー管理が可能
- **管理者**: 取引先会社追加、請求書項目追加、請求書作成が可能
- **一般**: 請求書作成のみ可能

## データベースモデル

### CustomUser（ユーザー）
- username: ユーザー名
- password: パスワード
- role: ユーザー種別（general/manager/director）

### Company（取引先会社）
- company_code: 会社コード（英数字、一意）
- company_name: 会社名
- contact_person: 担当者名
- address: 番地
- postal_code: 郵便番号
- prefecture: 都道府県
- phone: 電話番号
- email: メールアドレス

### Invoice（請求書）
- invoice_number: 請求書番号（一意）
- company: 取引先会社（外部キー）
- customer_id: 顧客ID
- created_at: 作成日時
- created_by: 作成者（外部キー）

### InvoiceDetail（請求書明細）
- invoice: 請求書（外部キー）
- item_name: 請求内容
- quantity: 個数
- unit_price: 単価
- amount: 金額（自動計算）
- order: 順序

### InvoiceItemTemplate（請求書項目テンプレート）
- name: 項目名
- description: 説明

## ファイル構成

- `invoice_template.xlsx`: 請求書のテンプレートファイル
- `generated_invoices/`: 生成された請求書が保存されるディレクトリ
- `db.sqlite3`: SQLiteデータベースファイル

## 請求書テンプレートのセル配置

- A8: 請求先会社の担当者
- A9: 会社名
- A10: 会社の番地
- A11: 郵便番号/都道府県
- A12: 電話番号
- A13: メールアドレス
- A16: 請求書番号
- F5: 請求書番号
- F8: 顧客ID
- H5: 請求書作成日時
- A17以降: 請求内容（最大10セット）
- F17以降: 個数
- G17以降: 単価
- H17以降: 金額

## 注意事項

- `invoice_template.xlsx`は`invoice_automation`フォルダの直下に配置してください
- 生成された請求書は`generated_invoices`フォルダに保存されます
- 会社コードは英数字のみ使用可能です
- 請求書番号は一意である必要があります
