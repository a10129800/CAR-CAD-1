Write-Host "=== 開始安裝 text-to-cad 技能與環境依賴 ===" -ForegroundColor Cyan

# 1. 安裝 Agent Skills
Write-Host "`n[1/3] 正在安裝 Agent Skills (earthtojake/text-to-cad)..." -ForegroundColor Yellow
npx skills add earthtojake/text-to-cad

# 2. 安裝 Python 幾何引擎
Write-Host "`n[2/3] 正在安裝 Python 幾何與 CAD 引擎 (cadgen)..." -ForegroundColor Yellow
python -m pip install -r requirements.txt

# 3. 安裝 Playwright 渲染引擎
Write-Host "`n[3/3] 正在安裝 Chromium 預覽渲染引擎..." -ForegroundColor Yellow
python -m playwright install chromium

Write-Host "`n[V] 安裝全部完成！" -ForegroundColor Green
Write-Host "測試範例：執行 python test_cube.py 即可生成 cube.step 模型" -ForegroundColor Cyan
