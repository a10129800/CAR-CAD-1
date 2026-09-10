"""
電動車底盤模組 (EV Chassis Module)
包含輕量化高剛性主底板、18650 動力鋰電池槽、前後輪軸/馬達支架、主控板固定柱及整線開孔
"""
from cadgen import build123d as bd
from cadgen import step, stl, threemf

CHASSIS_LENGTH = 150.0      # 底盤長度 150mm
CHASSIS_WIDTH = 68.0        # 底盤寬度 68mm
CHASSIS_BASE_THICK = 3.5    # 底板厚度 3.5mm
WHEELBASE = 96.0            # 前後軸距 96mm (前後各 ±48mm)

@step(out="../STEP/chassis.step")
@stl(out="../STL/chassis.stl")
@threemf(out="../3MF/chassis.3mf")
def chassis():
    # 1. 主底板主體
    base = bd.Box(CHASSIS_LENGTH, CHASSIS_WIDTH, CHASSIS_BASE_THICK)
    
    # 2. 前後車頭/車尾倒角減重
    front_left_cut = bd.Pos(70, 30, 0) * bd.Rot(0, 0, 45) * bd.Box(25, 25, 10)
    front_right_cut = bd.Pos(70, -30, 0) * bd.Rot(0, 0, -45) * bd.Box(25, 25, 10)
    rear_left_cut = bd.Pos(-70, 30, 0) * bd.Rot(0, 0, -45) * bd.Box(25, 25, 10)
    rear_right_cut = bd.Pos(-70, -30, 0) * bd.Rot(0, 0, 45) * bd.Box(25, 25, 10)
    
    # 3. 側邊減重倒槽 (左右兩側腰身微內縮)
    side_cut_l = bd.Pos(0, 35, 0) * bd.Box(45, 10, 10)
    side_cut_r = bd.Pos(0, -35, 0) * bd.Box(45, 10, 10)
    
    # 4. 中央 18650 動力電池倉 (長 72mm x 寬 21mm x 高 10mm 側牆)
    battery_wall = bd.Pos(0, 0, 4.0) * bd.Box(74, 23, 8.0)
    battery_pocket = bd.Pos(0, 0, 5.0) * bd.Box(70, 19, 10.0)
    
    # 5. 前輪軸架 (X = +48mm, 左右兩側安裝座)
    f_bracket_l = bd.Pos(48, 26, 6.0) * bd.Box(14, 8, 14)
    f_bracket_r = bd.Pos(48, -26, 6.0) * bd.Box(14, 8, 14)
    f_axle_hole = bd.Pos(48, 0, 8.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=1.6, height=CHASSIS_WIDTH + 10)
    
    # 6. 後輪軸/馬達固定架 (X = -48mm, 左右兩側安裝座)
    r_bracket_l = bd.Pos(-48, 26, 6.0) * bd.Box(14, 8, 14)
    r_bracket_r = bd.Pos(-48, -26, 6.0) * bd.Box(14, 8, 14)
    r_axle_hole = bd.Pos(-48, 0, 8.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=1.6, height=CHASSIS_WIDTH + 10)
    
    # 7. 電控板螺柱 (4 個 M2.5 固定柱，適合 ESP32 / Arduino / 樹莓派 Pico)
    # 分佈於電池倉上方左右或前後兩端
    standoffs = []
    standoff_holes = []
    standoff_coords = [(28, 18), (28, -18), (-28, 18), (-28, -18)]
    for sx, sy in standoff_coords:
        st = bd.Pos(sx, sy, 5.0) * bd.Cylinder(radius=3.0, height=8.0)
        hole = bd.Pos(sx, sy, 5.0) * bd.Cylinder(radius=1.2, height=12.0)
        standoffs.append(st)
        standoff_holes.append(hole)
        
    # 8. 整線孔 (用於走電池線與馬達動力線)
    cable_hole_front = bd.Pos(38, 0, 0) * bd.Cylinder(radius=3.5, height=10)
    cable_hole_rear = bd.Pos(-38, 0, 0) * bd.Cylinder(radius=3.5, height=10)
    
    # 結合與裁切
    result = base + battery_wall + f_bracket_l + f_bracket_r + r_bracket_l + r_bracket_r
    for st in standoffs:
        result = result + st
        
    result = result - front_left_cut - front_right_cut - rear_left_cut - rear_right_cut
    result = result - side_cut_l - side_cut_r - battery_pocket
    result = result - f_axle_hole - r_axle_hole
    for sh in standoff_holes:
        result = result - sh
    result = result - cable_hole_front - cable_hole_rear
    
    return result

if __name__ == "__main__":
    chassis()
