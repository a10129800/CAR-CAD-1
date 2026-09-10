"""
電動汽車完整組裝體 (Electric Car Full Assembly)
整合底盤、流線外殼及 4 個車輪模組，構成完整參數化 CAD 裝配體
可單獨執行編譯，亦可匯出全車 STEP 與 3D 列印 STL/3MF
"""
import sys
from pathlib import Path

# 將當前 src 加入搜尋路徑，方便相互引用
sys.path.insert(0, str(Path(__file__).parent))

from cadgen import build123d as bd
from cadgen import step, stl, threemf

from chassis import chassis
from wheel import wheel
from car_body import car_body

@step(out="../STEP/electric_car.step")
@stl(out="../STL/electric_car.stl")
@threemf(out="../3MF/electric_car.3mf")
def electric_car():
    # 1. 取得各子部件幾何
    chassis_part = chassis()
    body_part = car_body()
    wheel_model = wheel()
    
    # 2. 定位底盤 (離地間隙 8mm)
    chassis_placed = bd.Pos(0, 0, 8.0) * chassis_part
    
    # 3. 定位流線車身 (蓋在底盤上方)
    body_placed = bd.Pos(0, 0, 10.0) * body_part
    
    # 4. 定位 4 個車輪 (前/後軸距 ±48mm，左右輪距 ±39mm，車輪中心高 18mm)
    # 車輪模型預設軸向為 Z 軸，旋轉 90 度轉為 Y 軸方向
    wheel_fl = bd.Pos(48.0, 39.0, 16.0) * bd.Rot(90, 0, 0) * wheel_model
    wheel_fr = bd.Pos(48.0, -39.0, 16.0) * bd.Rot(-90, 0, 0) * wheel_model
    wheel_rl = bd.Pos(-48.0, 39.0, 16.0) * bd.Rot(90, 0, 0) * wheel_model
    wheel_rr = bd.Pos(-48.0, -39.0, 16.0) * bd.Rot(-90, 0, 0) * wheel_model
    
    # 5. 組合成完整複合裝配體 (Compound Assembly)
    assembly = bd.Compound(
        children=[
            chassis_placed,
            body_placed,
            wheel_fl,
            wheel_fr,
            wheel_rl,
            wheel_rr,
        ]
    )
    
    return assembly

if __name__ == "__main__":
    electric_car()
