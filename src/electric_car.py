"""
未來科技感賽博電動超跑總裝配體 (Cyber EV Hypercar Full Assembly)
整合高剛性平整底盤、未來賽博空氣力學外殼及 4 組渦輪刀鋒車輪總成
"""
import sys
from pathlib import Path

# 將當前 src 加入搜尋路徑
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
    
    # 2. 定位底盤 (離地間隙 7.5mm)
    chassis_placed = bd.Pos(0, 0, 7.5) * chassis_part
    
    # 3. 定位賽博車身 (精確蓋合於底盤)
    body_placed = bd.Pos(0, 0, 9.5) * body_part
    
    # 4. 定位 4 個低風阻渦輪車輪 (前後軸距 ±48mm，左右輪距 ±39.5mm，車輪中心高 16.5mm)
    wheel_fl = bd.Pos(48.0, 39.5, 16.5) * bd.Rot(90, 0, 0) * wheel_model
    wheel_fr = bd.Pos(48.0, -39.5, 16.5) * bd.Rot(-90, 0, 0) * wheel_model
    wheel_rl = bd.Pos(-48.0, 39.5, 16.5) * bd.Rot(90, 0, 0) * wheel_model
    wheel_rr = bd.Pos(-48.0, -39.5, 16.5) * bd.Rot(-90, 0, 0) * wheel_model
    
    # 5. 組合成完整裝配體
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
