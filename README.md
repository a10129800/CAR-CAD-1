# ⚡ CYBER EV HYPERCAR (3D 智慧電動超跑 CAD 互動專案)

> 基於 **Python + build123d** 構建的開源未來科技感參數化智慧電動超跑（Cyber Hypercar Prototype），支援 **3D 線上互動組裝、空力套件分解爆炸圖、賽博光效與風洞模擬、STL 檔案下載與 3D 列印**。

---

## 🌟 線上 3D 互動展示 (GitHub Pages)

部署完成後即可透過瀏覽器直接體驗：
👉 **`https://<您的GitHub帳號>.github.io/<倉庫名稱>/`**

* **🌌 未來賽博空氣力學外觀**：
  * **車頭**：低趴前傾分流前唇（Carbon Splitter）、雙側風刀（Canards）、貫穿式星環光刃矩陣 LED 大燈、引擎蓋 S-Duct 導流出風道。
  * **座艙與車側**：戰鬥機水滴雙曲面全景鏡面座艙、極簡流線無後視鏡純淨空力、空氣下壓側裙。
  * **車尾**：一體式天鵝頸戰鬥主動擾流尾翼、3D 刀鋒連貫 OLED 尾燈、賽道級多道垂直導流後下擴散器。
  * **輪組與煞車**：7 葉片低風阻渦輪刀鋒輪圈（Aero Turbine Blades）、中心鎖止機構、打孔通風陶瓷煞車碟盤與多活塞螢光卡鉗。
* **🎮 WASD 即時賽博試駕體驗 (Driving Physics)**：
  * **全向操控**：支援鍵盤 `W / A / S / D`、方向鍵或畫面虛擬方向盤觸控駕駛。
  * **阿克曼真實轉向**：前輪隨轉向角平滑打向（±26.5°）並具備自動回正力學。
  * **懸吊動態姿態**：加速車尾下沉、煞車車頭前傾俯仰（Pitch）、高速過彎側傾（Roll）。
  * **煞車尾燈反應**：踩踏煞車時 OLED 貫穿尾燈瞬間爆亮發光。
  * **超導氮氣加速（Nitro Boost）**：按下 `Shift` 或 `Space` 釋放超導推力，速度直飆 370 km/h。
  * **後輪甩尾光軌粒子（Drift Sparks）**：高速轉彎與彈射起步時噴發賽博青光微粒。
* **🔊 純程式碼 Web Audio 賽博音效合成引擎 (Zero-Asset Synth)**：
  * **零檔案下載**：無需任何外部音效檔，純瀏覽器振盪器即時運算合成。
  * **Formula E 雙諧波電磁嘯聲**：音頻頻率與濾波器截止點隨油門與行駛時速線性爬升。
  * **動能回充煞車聲**：高頻電磁能量回收逆變音效。
  * **Warp 氮氣頻率掃描**：衝刺時觸發空間折躍般的高亢推進音。
  * **UI 賽博科技提示音**與一鍵靜音/開啟切換。
* **🏎️ 雙鏡頭模式（Camera Modes）**：
  * **第三人稱追隨視角（Chase Cam）**：平滑伴隨超跑轉向、加速後移拉開視距，宛如 3A 賽車大作。
  * **360° 自由軌道視角（Free Orbit）**：無俯仰角限制，搭配地表反照燈，無死角檢視平整化底盤與內部構造。
* **💥 空力套件 3D 爆炸分解圖（0% ~ 100%）**：拉動滑桿動態展開車殼、主動尾翼、底盤、輪圈煞車總成。
* **⚡ 賽博光電與動態特效**：
  * **車底霓虹燈（Ground Underglow）**：投射在 3,000 米巨大賽博網格跑道上的動態氛圍冷光。
  * **風洞氣流線模擬（Wind Tunnel）**：即時動態粒子模擬超跑車身空氣流向。
* **🎨 6 款賽博未來車漆**：賽博電光青、離子脈衝紫、極速赤影紅、潛行碳纖黑、矩陣毒液綠、超導流體金。
* **📊 頂部 HUD 遙測儀表**：即時連動數位時速表 (km/h)、檔位指示 (P / D / R / BOOST)、馬達輸出功率 (kW)、空力下壓力 (kgf) 與電池狀態。
* **📥 一鍵下載 3D 列印 STL**：點擊網頁面板即可直接下載列印檔案。

---

## 📐 車輛規格

| 項目 | 尺寸 / 規格 | 說明 |
| :--- | :--- | :--- |
| **全車尺寸** | 158mm × 90mm × 46mm | 標準 1:24 ~ 1:28 寬體低趴賽博超跑尺寸 |
| **前後軸距** | 96 mm (前後各 ±48mm) | 車輪轉向與行駛配重黃金比例 |
| **動力電池倉** | 72mm × 21mm × 10mm | 專為標準 **18650 動力鋰電池** 設計 |
| **電控安裝孔** | 4 處 M2.5 規格固定柱 | 相容 ESP32、Arduino Nano、樹莓派 Pico |
| **車輪尺寸** | Ø 36mm × 寬 14mm | 7 葉片渦輪定向導風刀鋒輪框，3mm 傳動軸孔 |

---

## 📂 3D 模型檔案清單 (`STL/` & `src/`)

* **`src/car_body.py`**：賽博超跑車身外殼參數化 CAD 幾何腳本。
* **`src/wheel.py`**：渦輪刀鋒低風阻車輪與煞車盤 CAD 腳本。
* **`src/chassis.py`**：平整化空氣力學工程底盤 CAD 腳本。
* **`src/electric_car.py`**：全車組裝 Compound 裝配體腳本。
* **`STL/print_bed_kit.stl`**：3D 列印一體排版組合包。
* **`STL/electric_car.stl`**：全車組裝模型。
* **`STL/car_body.stl`**：賽博空力外殼。
* **`STL/chassis.stl`**：工程底盤。
* **`STL/wheel.stl`**：車輪模組。

---

## 🚀 如何發布到 GitHub Pages？

### 步驟 1：在 GitHub 建立新倉庫
1. 前往 [GitHub.com](https://github.com/) 點擊右上角 **「New repository」**。
2. 倉庫名稱輸入（例如）：`cyber-ev-hypercar`。
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
git add .
git commit -m "feat: upgrade to ultra-futuristic cyber EV hypercar"
git push -u origin main
```

### 步驟 3：啟用 GitHub Pages
1. 打開您的 GitHub 倉庫頁面，點擊上方 **【Settings】**。
2. 在左側選單點擊 **【Pages】**。
3. 在 **Build and deployment** 下方：
   * **Source**: Deploy from a branch
   * **Branch**: 選擇 **`main`**，資料夾選擇 **`/ (root)`**
4. 點擊 **Save**。
5. 等待 1~2 分鐘，上方就會出現專屬網址：`https://<帳號>.github.io/<倉庫名>/`，任何人點開都能在瀏覽器裡體驗這台超酷炫的 3D 賽博電動超跑！
