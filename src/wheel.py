"""
未來科技感渦輪刀鋒輪圈模組 (Cyber Aero-Blade Turbine Wheel Module)
特色：
1. 封閉式低風阻空氣動力學渦輪扇葉 (Aero Turbine Blades)
2. 賽車級中心鎖止機構 (Central Lock Nut)
3. 內凹散熱通風槽與打孔煞車碟盤槽位
4. 3mm 標準動力傳動軸孔
"""
import math
from cadgen import build123d as bd
from cadgen import step, stl, threemf

WHEEL_DIAMETER = 36.0     # 車輪直徑 36mm
WHEEL_WIDTH = 14.0        # 車輪寬度 14mm
RIM_DIAMETER = 26.0       # 輪框直徑 26mm
AXLE_HOLE_RADIUS = 1.5    # 軸孔半徑 1.5mm (對應 3mm 軸)

@step(out="../STEP/wheel.step")
@stl(out="../STL/wheel.stl")
@threemf(out="../3MF/wheel.3mf")
def wheel():
    # 1. 輪胎主體圓柱 (Tire Base)
    tire = bd.Cylinder(radius=WHEEL_DIAMETER / 2, height=WHEEL_WIDTH)
    
    # 2. 雙層深凹外側與內側輪框凹槽 (Deep Rim Pockets)
    rim_outer_pocket = bd.Pos(0, 0, 2.5) * bd.Cylinder(radius=RIM_DIAMETER / 2, height=WHEEL_WIDTH / 2 + 2)
    rim_inner_pocket = bd.Pos(0, 0, -3.5) * bd.Cylinder(radius=RIM_DIAMETER / 2 - 1.5, height=WHEEL_WIDTH / 2 + 2)
    
    # 3. 煞車碟盤造型內凹 (Brake Rotor Cavity)
    brake_rotor_ring = bd.Pos(0, 0, 1.0) * bd.Cylinder(radius=9.0, height=3.0)
    
    # 4. 中心鎖止式高科技輪轂凸台 (Aero Center-Lock Hub)
    center_hub = bd.Pos(0, 0, 2.0) * bd.Cylinder(radius=4.8, height=WHEEL_WIDTH / 2)
    center_hex_nut = bd.Pos(0, 0, 5.0) * bd.Box(3.6, 3.6, 3.0)
    
    # 5. 3mm 中心傳動軸孔 (Axle Hole)
    axle_hole = bd.Cylinder(radius=AXLE_HOLE_RADIUS, height=WHEEL_WIDTH + 6)
    
    # 6. 7 葉片渦輪定向導風刀鋒 (7-Blade Directional Aero Turbine Blades)
    blade_cuts = []
    num_blades = 7
    for i in range(num_blades):
        angle = i * (360.0 / num_blades)
        rad = math.radians(angle)
        dist = 8.5
        bx = dist * math.cos(rad)
        by = dist * math.sin(rad)
        # 傾斜 25 度的扇葉導風切口
        blade_cut = bd.Pos(bx, by, 3.0) * bd.Rot(0, 0, angle + 25) * bd.Box(2.2, 5.5, WHEEL_WIDTH / 2 + 2)
        blade_cuts.append(blade_cut)
        
    # 7. 煞車碟盤通風散熱小穿孔 (Ventilated Rotor Holes)
    rotor_vents = []
    for j in range(6):
        v_angle = j * (360.0 / 6.0)
        v_rad = math.radians(v_angle)
        vx = 7.0 * math.cos(v_rad)
        vy = 7.0 * math.sin(v_rad)
        v_hole = bd.Pos(vx, vy, 1.0) * bd.Cylinder(radius=0.9, height=4.0)
        rotor_vents.append(v_hole)
        
    # 8. 胎面低滾阻科技胎紋 (12 道幾何對稱微槽)
    tread_grooves = []
    num_grooves = 12
    for k in range(num_grooves):
        t_angle = k * (360.0 / num_grooves)
        t_rad = math.radians(t_angle)
        tx = (WHEEL_DIAMETER / 2) * math.cos(t_rad)
        ty = (WHEEL_DIAMETER / 2) * math.sin(t_rad)
        groove = bd.Pos(tx, ty, 0) * bd.Rot(0, 0, t_angle) * bd.Box(1.6, 1.2, WHEEL_WIDTH + 1)
        tread_grooves.append(groove)
        
    # 結合與布林裁切
    result = (tire + center_hub + center_hex_nut) - rim_outer_pocket - rim_inner_pocket - axle_hole
    for bc in blade_cuts:
        result = result - bc
    for rv in rotor_vents:
        result = result - rv
    for tg in tread_grooves:
        result = result - tg
        
    return result

if __name__ == "__main__":
    wheel()
