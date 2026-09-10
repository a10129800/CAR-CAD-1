# 🏎️ Smart EV Prototype (3D 智慧電動車 CAD 互動專案)

> 基於 **Python + build123d** 構建的開源參數化智慧電動跑車，支援 **3D 線上互動組裝、爆炸分解檢視、STL 檔案下載與 3D 列印**。

---

## 🌟 線上 3D 互動展示 (GitHub Pages)

部署完成後即可透過瀏覽器直接體驗：
👉 **`https://<您的GitHub帳號>.github.io/<倉庫名稱>/`**

* **360° 自由旋轉與縮放**：觀察每一個細部結構。
* **💥 爆炸分解圖（0% ~ 100%）**：拉動滑桿動態展開車身、輪組與底盤。
* **跑車金屬烤漆切換**：法拉利紅、電光藍、珍珠白、競速黃等 6 種配色。
* **📥 一鍵下載 STL**：點擊網頁面板即可直接下載 3D 列印檔案。

---

## 📐 車輛規格

| 項目 | 尺寸 / 規格 | 說明 |
| :--- | :--- | :--- |
| **全車尺寸** | 156mm × 88mm × 48mm | 標準 1:24 ~ 1:28 創客自走車尺寸 |
| **前後軸距** | 96 mm (前後各 ±48mm) | 車輪轉向與行駛配重黃金比例 |
| **動力電池倉** | 72mm × 21mm × 10mm | 專為標準 **18650 動力鋰電池** 設計 |
| **電控安裝孔** | 4 處 M2.5 規格固定柱 | 相容 ESP32、Arduino Nano、樹莓派 Pico |
| **車輪尺寸** | Ø 36mm × 寬 14mm | 5 輻運動化星型輪框，3mm 傳動軸孔 |

---

## 📂 3D 模型檔案清單 (`STL/`)

* **`print_bed_kit.stl`**：3D 列印一體排版組合包（底盤 + 車身 + 4 輪平鋪於一張列印床，一次印完）。
* **`electric_car.stl`**：全車組裝模型。
* **`car_body.stl`**：流線型跑車外殼。
* **`chassis.stl`**：工程底盤（含 18650 電池倉與馬達座）。
* **`wheel.stl`**：車輪與輪圈。

---

## 🚀 如何發布到 GitHub Pages？

### 步驟 1：在 GitHub 建立新倉庫
1. 前往 [GitHub.com](https://github.com/) 點擊右上角 **「New repository」**。
2. 倉庫名稱輸入（例如）：`smart-ev-cad`。
3. 設為 **Public**，點擊 **Create repository**。

### 步驟 2：推送本地專案到 GitHub
在專案資料夾開啟 PowerShell，執行：

```powershell
cd C:\Users\mice\.gemini\antigravity-ide\scratch\cad-project
.\deploy_to_github.ps1
```
*(腳本會引導您貼上剛建好的 GitHub 倉庫網址並自動推上去)*

或者手動執行：
```powershell
git init -b main
git add .
git commit -m "feat: 3D EV interactive page with STL models"
git remote add origin https://github.com/您的帳號/您的倉庫名.git
git push -u origin main
```

### 步驟 3：啟用 GitHub Pages
1. 打開您的 GitHub 倉庫頁面，點擊上方 **【Settings】**。
2. 在左側選單點擊 **【Pages】**。
3. 在 **Build and deployment** 下方：
   * **Source**: Deploy from a branch
   * **Branch**: 選擇 **`main`**，資料夾選擇 **`/ (root)`**
4. 點擊 **Save**。
5. 等待 1~2 分鐘，上方就會出現專屬網址：`https://<帳號>.github.io/<倉庫名>/`，任何人點開都能在瀏覽器裡玩這台 3D 電動車！
