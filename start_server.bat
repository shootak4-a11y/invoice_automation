@echo off
chcp 65001 >nul
cd /d %~dp0
echo ========================================
echo 請求書自動作成システム - サーバー起動
echo ========================================
echo.
echo サーバーを起動しています...
echo ブラウザで以下のURLにアクセスしてください:
echo http://127.0.0.1:8000/login/
echo.
echo サーバーを停止するには Ctrl+C を押してください
echo.
python manage.py runserver
pause
