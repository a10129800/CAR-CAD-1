# GitHub Pages 一鍵發布輔助腳本
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "   🏎️ Smart EV Prototype - GitHub 發布   " -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# 檢查 Git 是否安裝
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "`n[!] 找不到 git 指令，請先安裝 Git for Windows (https://git-scm.com/)" -ForegroundColor Red
    Exit
}

# 1. 初始化 Git 倉庫
if (-not (Test-Path ".git")) {
    Write-Host "`n[1/4] 初始化 Git 倉庫..." -ForegroundColor Yellow
    git init -b main
} else {
    Write-Host "`n[1/4] Git 倉庫已存在。" -ForegroundColor Green
}

# 2. 加入所有檔案並提交
Write-Host "`n[2/4] 加入檔案並建立提交 (Commit)..." -ForegroundColor Yellow
git add .
git commit -m "feat: initial release with 3D EV interactive viewer and STL files"

# 3. 設定遠端倉庫
Write-Host "`n[3/4] 設定 GitHub 遠端倉庫" -ForegroundColor Yellow
$remotes = git remote -v
if (-not $remotes) {
    $repoUrl = Read-Host "請貼上您的 GitHub 倉庫 URL (例如 https://github.com/您的帳號/smart-ev-cad.git)"
    if ($repoUrl) {
        git remote add origin $repoUrl
    } else {
        Write-Host "[!] 未輸入 URL，請手動執行: git remote add origin <你的倉庫URL>" -ForegroundColor Yellow
        Exit
    }
} else {
    Write-Host "已偵測到遠端倉庫: origin" -ForegroundColor Green
}

# 4. 推送至 GitHub
Write-Host "`n[4/4] 推送檔案至 GitHub main 分支..." -ForegroundColor Yellow
git branch -M main
git push -u origin main

Write-Host "`n=========================================" -ForegroundColor Green
Write-Host " [V] 檔案已成功推送到 GitHub！" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host "接下來只需開啟 GitHub Pages：" -ForegroundColor Cyan
Write-Host "1. 打開您的 GitHub 倉庫頁面"
Write-Host "2. 點擊 【Settings】 -> 左側選單【Pages】"
Write-Host "3. 在 Build and deployment 的 Branch 選擇 【main】 / 【/ (root)】 並點擊 Save"
Write-Host "4. 約 1~2 分鐘後，您的 3D 網站就會在 https://<帳號>.github.io/<倉庫名>/ 上線！`n"
