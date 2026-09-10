"""
車輪模組 (Wheel Module)
包含輪胎本體、5 輻運動化輪圈、裝飾螺栓孔及 3mm 傳動軸孔
"""
import math
from cadgen import build123d as bd
from cadgen import step, stl, threemf

WHEEL_DIAMETER = 36.0     # 車輪直徑 36mm
WHEEL_WIDTH = 14.0        # 車輪寬度 14mm
RIM_DIAMETER = 24.0       # 輪框直徑 24mm
AXLE_HOLE_RADIUS = 1.5    # 軸孔半徑 1.5mm (對應 3mm 軸)

@step(out="../STEP/wheel.step")
@stl(out="../STL/wheel.stl")
@threemf(out="../3MF/wheel.3mf")
def wheel():
    # 1. 輪胎基本圓柱
    tire = bd.Cylinder(radius=WHEEL_DIAMETER / 2, height=WHEEL_WIDTH)
    
    # 2. 外側與內側輪圈凹槽
    rim_outer_cut = bd.Pos(0, 0, 3) * bd.Cylinder(radius=RIM_DIAMETER / 2, height=WHEEL_WIDTH / 2 + 1)
    rim_inner_cut = bd.Pos(0, 0, -4) * bd.Cylinder(radius=RIM_DIAMETER / 2 - 2, height=WHEEL_WIDTH / 2 + 1)
    
    # 3. 中心軸孔 (3mm)
    axle_hole = bd.Cylinder(radius=AXLE_HOLE_RADIUS, height=WHEEL_WIDTH + 4)
    
    # 4. 輪圈中心凸台
    center_hub = bd.Pos(0, 0, 1) * bd.Cylinder(radius=4.5, height=WHEEL_WIDTH / 2)
    
    # 5. 5 輻輪圈鏤空
    spoke_cuts = []
    for i in range(5):
        angle = i * (360.0 / 5.0)
        rad = math.radians(angle)
        # 放射狀鏤空
        dist = 7.5
        cx = dist * math.cos(rad)
        cy = dist * math.sin(rad)
        hole = bd.Pos(cx, cy, 0) * bd.Cylinder(radius=2.2, height=WHEEL_WIDTH + 2)
        spoke_cuts.append(hole)
        
    # 6. 胎面裝飾防滑胎紋 (8 條圓周開槽)
    tread_grooves = []
    for i in range(8):
        angle = i * (360.0 / 8.0)
        rad = math.radians(angle)
        gx = (WHEEL_DIAMETER / 2) * math.cos(rad)
        gy = (WHEEL_DIAMETER / 2) * math.sin(rad)
        groove = bd.Pos(gx, gy, 0) * bd.Rot(0, 0, angle) * bd.Box(1.5, 1.2, WHEEL_WIDTH + 1)
        tread_grooves.append(groove)
    
    # 布林運算結合
    result = (tire + center_hub) - rim_outer_cut - rim_inner_cut - axle_hole
    for sc in spoke_cuts:
        result = result - sc
    for tg in tread_grooves:
        result = result - tg
        
    return result

if __name__ == "__main__":
    wheel()
