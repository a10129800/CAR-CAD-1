"""
電動超跑工程底盤模組 (EV Hypercar Aero Chassis Module)
包含：平整化低風阻底板、18650 動力電池散熱隔艙、前後馬達/軸承支座、前唇加固座與後擴散器底板
"""
from cadgen import build123d as bd
from cadgen import step, stl, threemf

CHASSIS_LENGTH = 152.0      # 底盤長度 152mm
CHASSIS_WIDTH = 70.0        # 底盤寬度 70mm
CHASSIS_BASE_THICK = 3.5    # 底板厚度 3.5mm
WHEELBASE = 96.0            # 前後軸距 96mm (前後各 ±48mm)

@step(out="../STEP/chassis.step")
@stl(out="../STL/chassis.stl")
@threemf(out="../3MF/chassis.3mf")
def chassis():
    # 1. 平整化空氣動力學主底板 (Flat Aero Floor)
    base = bd.Box(CHASSIS_LENGTH, CHASSIS_WIDTH, CHASSIS_BASE_THICK)
    
    # 2. 前端前唇結合延伸台 (Front Splitter Extension Mount)
    front_lip_ext = bd.Pos(74.0, 0, 0) * bd.Box(6.0, 64.0, CHASSIS_BASE_THICK)
    
    # 3. 前後車角幾何減重倒角 (Chamfer cuts)
    front_left_cut = bd.Pos(72, 32, 0) * bd.Rot(0, 0, 45) * bd.Box(25, 25, 10)
    front_right_cut = bd.Pos(72, -32, 0) * bd.Rot(0, 0, -45) * bd.Box(25, 25, 10)
    rear_left_cut = bd.Pos(-72, 32, 0) * bd.Rot(0, 0, -45) * bd.Box(25, 25, 10)
    rear_right_cut = bd.Pos(-72, -32, 0) * bd.Rot(0, 0, 45) * bd.Box(25, 25, 10)
    
    # 4. 側邊氣流收束腰身 (Aero Waist Inset)
    side_cut_l = bd.Pos(0, 36.5, 0) * bd.Box(48, 8, 10)
    side_cut_r = bd.Pos(0, -36.5, 0) * bd.Box(48, 8, 10)
    
    # 5. 中央 18650 動力鋰電池保護隔艙 (72mm x 21mm 空間)
    battery_wall = bd.Pos(0, 0, 4.0) * bd.Box(74, 23, 8.0)
    battery_pocket = bd.Pos(0, 0, 5.0) * bd.Box(70, 19, 10.0)
    # 電池散熱側窗 (Cooling Slots)
    bat_vent_1 = bd.Pos(-20, 0, 4.0) * bd.Box(6, 26, 4.0)
    bat_vent_2 = bd.Pos(20, 0, 4.0) * bd.Box(6, 26, 4.0)
    
    # 6. 前軸承支架 (X = +48mm)
    f_bracket_l = bd.Pos(48, 27, 6.0) * bd.Box(14, 8, 14)
    f_bracket_r = bd.Pos(48, -27, 6.0) * bd.Box(14, 8, 14)
    f_axle_hole = bd.Pos(48, 0, 8.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=1.6, height=CHASSIS_WIDTH + 14)
    
    # 7. 後軸/馬達支架 (X = -48mm)
    r_bracket_l = bd.Pos(-48, 27, 6.0) * bd.Box(14, 8, 14)
    r_bracket_r = bd.Pos(-48, -27, 6.0) * bd.Box(14, 8, 14)
    r_axle_hole = bd.Pos(-48, 0, 8.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=1.6, height=CHASSIS_WIDTH + 14)
    
    # 8. 電控主板固定柱 (ESP32 / Pico / Arduino Nano M2.5 柱)
    standoffs = []
    standoff_holes = []
    standoff_coords = [(28, 19), (28, -19), (-28, 19), (-28, -19)]
    for sx, sy in standoff_coords:
        st = bd.Pos(sx, sy, 5.0) * bd.Cylinder(radius=3.0, height=8.0)
        hole = bd.Pos(sx, sy, 5.0) * bd.Cylinder(radius=1.2, height=12.0)
        standoffs.append(st)
        standoff_holes.append(hole)
        
    # 9. 動力線與感測器走線孔
    cable_hole_front = bd.Pos(38, 0, 0) * bd.Cylinder(radius=3.5, height=10)
    cable_hole_rear = bd.Pos(-38, 0, 0) * bd.Cylinder(radius=3.5, height=10)
    
    # 結合主體
    result = base + front_lip_ext + battery_wall + f_bracket_l + f_bracket_r + r_bracket_l + r_bracket_r
    for st in standoffs:
        result = result + st
        
    # 裁切掏槽
    result = result - front_left_cut - front_right_cut - rear_left_cut - rear_right_cut
    result = result - side_cut_l - side_cut_r - battery_pocket - bat_vent_1 - bat_vent_2
    result = result - f_axle_hole - r_axle_hole
    for sh in standoff_holes:
        result = result - sh
    result = result - cable_hole_front - cable_hole_rear
    
    return result

if __name__ == "__main__":
    chassis()
