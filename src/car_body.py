"""
流線型電動車車身外殼 (Streamlined EV Canopy Module)
空氣動力學低風阻外觀、前進氣壩、前後輪拱開孔、流線車頂與後擾流尾翼
"""
from cadgen import build123d as bd
from cadgen import step, stl, threemf

BODY_LENGTH = 156.0
BODY_WIDTH = 70.0
BODY_HEIGHT = 35.0

@step(out="../STEP/car_body.step")
@stl(out="../STL/car_body.stl")
@threemf(out="../3MF/car_body.3mf")
def car_body():
    # 1. 下車身主體基塊
    lower_body = bd.Pos(0, 0, 10.0) * bd.Box(BODY_LENGTH, BODY_WIDTH, 20.0)
    
    # 2. 上座艙流線車頂 (Cabin Dome)
    cabin = bd.Pos(-5.0, 0, 24.0) * bd.Box(76.0, 52.0, 16.0)
    
    # 3. 前後空氣動力傾角裁切 (Windshield & Hood slope)
    # 前引擎蓋下斜切
    hood_slope = bd.Pos(55.0, 0, 22.0) * bd.Rot(0, 18, 0) * bd.Box(60.0, BODY_WIDTH + 10, 20.0)
    # 前車頭尖角斜切 (Nose taper)
    nose_taper_top = bd.Pos(70.0, 0, 18.0) * bd.Rot(0, 30, 0) * bd.Box(30.0, BODY_WIDTH + 10, 20.0)
    # 擋風玻璃斜角切
    windshield_cut = bd.Pos(28.0, 0, 31.0) * bd.Rot(0, 42, 0) * bd.Box(30.0, 56.0, 20.0)
    # 後車頂斜背裁切 (Fastback slope)
    fastback_cut = bd.Pos(-46.0, 0, 30.0) * bd.Rot(0, -32, 0) * bd.Box(45.0, 56.0, 20.0)
    # 後尾部導流斜切
    rear_taper_cut = bd.Pos(-70.0, 0, 20.0) * bd.Rot(0, -20, 0) * bd.Box(30.0, BODY_WIDTH + 10, 20.0)
    
    # 4. 4 個輪拱開槽 (Wheel Wells，半徑 21mm，確保車輪轉動與轉彎不摩擦)
    # 軸心位於 X=±48, Y=±35, Z=0
    wheel_wells = []
    for wx in [48.0, -48.0]:
        for wy in [35.0, -35.0]:
            well = bd.Pos(wx, wy, 2.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=21.0, height=22.0)
            wheel_wells.append(well)
            
    # 5. 車頭 LED 貫穿式前大燈槽與導流氣壩
    headlight_slot = bd.Pos(75.5, 0, 12.0) * bd.Box(6.0, 50.0, 3.5)
    front_intake = bd.Pos(75.0, 0, 4.0) * bd.Box(6.0, 38.0, 5.0)
    
    # 6. 車側空氣導流進氣口 (Side scoops)
    side_scoop_l = bd.Pos(-10.0, 34.0, 8.0) * bd.Box(25.0, 6.0, 8.0)
    side_scoop_r = bd.Pos(-10.0, -34.0, 8.0) * bd.Box(25.0, 6.0, 8.0)
    
    # 7. 後擾流尾翼片 (Integrated Rear Spoiler Lip)
    spoiler_lip = bd.Pos(-72.0, 0, 18.0) * bd.Box(10.0, 56.0, 3.0)
    
    # 8. 內部底盤掏空槽 (Hollow interior to fit chassis & electronics)
    # 壁厚約 2.5 ~ 3.0 mm
    interior_cavity = bd.Pos(0, 0, 8.0) * bd.Box(146.0, 62.0, 26.0)
    
    # 組合實體
    result = lower_body + cabin + spoiler_lip
    result = result - hood_slope - nose_taper_top - windshield_cut - fastback_cut - rear_taper_cut
    for ww in wheel_wells:
        result = result - ww
    result = result - headlight_slot - front_intake - side_scoop_l - side_scoop_r
    result = result - interior_cavity
    
    return result

if __name__ == "__main__":
    car_body()
