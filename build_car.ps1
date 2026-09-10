Write-Host "=== 正在準備輸出資料夾 (STEP / STL / 3MF) ===" -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path ".\STEP" | Out-Null
New-Item -ItemType Directory -Force -Path ".\STL" | Out-Null
New-Item -ItemType Directory -Force -Path ".\3MF" | Out-Null

Write-Host "`n=== 正在編譯電動車 3D 裝配體模型 ===" -ForegroundColor Yellow
python .\src\electric_car.py

Write-Host "`n[V] 3D CAD 模型生成完成！" -ForegroundColor Green
Write-Host "輸出檔案清單：" -ForegroundColor Cyan
Get-ChildItem -Path ".\STEP", ".\STL", ".\3MF" | Select-Object Name, Length, DirectoryName | Format-Table -AutoSize
