"""
未來科技感賽博電動超跑外殼 (Cyber EV Hypercar Body Module)
特色：
1. 低風阻極致空氣動力學下壓外觀 (Aggressive Aero Profiling)
2. 前端競速碳纖分流前唇 (Front Splitter) 與雙側風刀 (Canards)
3. 引擎蓋下壓空氣導流通道 (Hood S-Duct & Extractor Vents)
4. 兩側立體深凹進氣側裙 (Aero Side Skirts) - 無多餘突起柱狀後視鏡，純淨流線
5. 雙立柱戰鬥擾流尾翼 (Twin-Strut High-Downforce Aero Wing)
6. 賽道級後下空氣擴散器導流鰭片 (Rear Aero Diffuser Strakes)
7. 車頭星環矩陣 LED 貫穿大燈與車尾光刃尾燈槽
"""
from cadgen import build123d as bd
from cadgen import step, stl, threemf

BODY_LENGTH = 158.0
BODY_WIDTH = 72.0
BODY_HEIGHT = 38.0

@step(out="../STEP/car_body.step")
@stl(out="../STL/car_body.stl")
@threemf(out="../3MF/car_body.3mf")
def car_body():
    # 1. 下車身低重心主體 (Low-slung Main Chassis Shell)
    lower_body = bd.Pos(0, 0, 10.0) * bd.Box(BODY_LENGTH, BODY_WIDTH, 18.0)
    
    # 2. 戰鬥機式水滴座艙頂蓋 (Jet-Fighter Cockpit Dome)
    cabin = bd.Pos(-6.0, 0, 23.0) * bd.Box(74.0, 50.0, 15.0)
    
    # 3. 前後空氣動力傾角與導流面裁切 (Aerodynamic Slopes & Chamfers)
    hood_slope = bd.Pos(54.0, 0, 22.0) * bd.Rot(0, 16, 0) * bd.Box(62.0, BODY_WIDTH + 14, 20.0)
    nose_taper_top = bd.Pos(72.0, 0, 17.0) * bd.Rot(0, 28, 0) * bd.Box(28.0, BODY_WIDTH + 14, 20.0)
    windshield_cut = bd.Pos(27.0, 0, 29.0) * bd.Rot(0, 40, 0) * bd.Box(32.0, 54.0, 20.0)
    fastback_cut = bd.Pos(-48.0, 0, 28.0) * bd.Rot(0, -30, 0) * bd.Box(48.0, 54.0, 20.0)
    rear_taper_cut = bd.Pos(-72.0, 0, 18.0) * bd.Rot(0, -18, 0) * bd.Box(32.0, BODY_WIDTH + 14, 20.0)
    
    # 4. 引擎蓋空氣下壓導流槽 (Hood S-Duct Recess) 與雙側散熱開孔
    hood_sduct = bd.Pos(50.0, 0, 17.5) * bd.Box(26.0, 18.0, 5.0)
    hood_vent_l = bd.Pos(42.0, 16.0, 17.5) * bd.Box(16.0, 5.0, 4.0)
    hood_vent_r = bd.Pos(42.0, -16.0, 17.5) * bd.Box(16.0, 5.0, 4.0)
    
    # 5. 前下巴碳纖下壓力分流翼 (Front Carbon Splitter) 與側風刀 (Canards)
    front_splitter = bd.Pos(76.0, 0, 3.5) * bd.Box(8.0, BODY_WIDTH + 4.0, 2.5)
    canard_l = bd.Pos(68.0, 36.5, 6.0) * bd.Rot(0, 12, 15) * bd.Box(14.0, 2.5, 3.5)
    canard_r = bd.Pos(68.0, -36.5, 6.0) * bd.Rot(0, 12, -15) * bd.Box(14.0, 2.5, 3.5)
    
    # 6. 輪拱擴展開槽 (寬體低趴輪弧，軸心 X=±48, Y=±36)
    wheel_wells = []
    for wx in [48.0, -48.0]:
        for wy in [36.0, -36.0]:
            well = bd.Pos(wx, wy, 2.0) * bd.Rot(90, 0, 0) * bd.Cylinder(radius=21.5, height=24.0)
            wheel_wells.append(well)
            
    # 7. 兩側幾何深凹冷卻導風側裙 (Deep Side Scoops)
    side_scoop_l = bd.Pos(-8.0, 35.0, 8.0) * bd.Box(36.0, 8.0, 9.0)
    side_scoop_r = bd.Pos(-8.0, -35.0, 8.0) * bd.Box(36.0, 8.0, 9.0)
    skirt_blade_l = bd.Pos(0, 37.0, 3.5) * bd.Box(76.0, 3.0, 2.0)
    skirt_blade_r = bd.Pos(0, -37.0, 3.5) * bd.Box(76.0, 3.0, 2.0)
    
    # 8. 車頭星環光刃 LED 貫穿前大燈槽與導流氣壩
    headlight_slot = bd.Pos(77.0, 0, 11.5) * bd.Box(6.0, 54.0, 3.0)
    front_intake = bd.Pos(76.5, 0, 4.5) * bd.Box(6.0, 42.0, 4.5)
    
    # 9. 車尾 3D 光刃貫穿式尾燈槽 (Blade OLED Light Slot)
    taillight_slot = bd.Pos(-77.5, 0, 14.5) * bd.Box(5.0, 56.0, 3.0)
    
    # 10. 雙立柱戰鬥擾流尾翼 (Twin-Strut High-Downforce Wing with Endplates)
    spoiler_pillar_l = bd.Pos(-68.0, 20.0, 23.0) * bd.Rot(0, -10, 0) * bd.Box(6.0, 3.0, 12.0)
    spoiler_pillar_r = bd.Pos(-68.0, -20.0, 23.0) * bd.Rot(0, -10, 0) * bd.Box(6.0, 3.0, 12.0)
    spoiler_main_blade = bd.Pos(-71.0, 0, 28.5) * bd.Rot(0, 6, 0) * bd.Box(14.0, 64.0, 3.0)
    endplate_l = bd.Pos(-71.0, 32.0, 28.5) * bd.Box(18.0, 2.0, 9.0)
    endplate_r = bd.Pos(-71.0, -32.0, 28.5) * bd.Box(18.0, 2.0, 9.0)
    
    # 11. 賽道級後下擴散器導流鰭片 (Rear Diffuser Strakes)
    diffuser_tunnel = bd.Pos(-72.0, 0, 3.0) * bd.Rot(0, -15, 0) * bd.Box(24.0, 44.0, 6.0)
    diffuser_fin_1 = bd.Pos(-72.0, -14.0, 3.0) * bd.Box(18.0, 2.0, 5.0)
    diffuser_fin_2 = bd.Pos(-72.0, -4.5, 3.0) * bd.Box(18.0, 2.0, 5.0)
    diffuser_fin_3 = bd.Pos(-72.0, 4.5, 3.0) * bd.Box(18.0, 2.0, 5.0)
    diffuser_fin_4 = bd.Pos(-72.0, 14.0, 3.0) * bd.Box(18.0, 2.0, 5.0)
    
    # 12. 內部掏空槽 (Hollow Interior for Electronics & Chassis)
    interior_cavity = bd.Pos(0, 0, 7.5) * bd.Box(146.0, 63.0, 25.0)
    
    # 組合實體 (Union operations)
    body_solid = lower_body + cabin + front_splitter + canard_l + canard_r
    body_solid = body_solid + skirt_blade_l + skirt_blade_r
    body_solid = body_solid + spoiler_pillar_l + spoiler_pillar_r + spoiler_main_blade + endplate_l + endplate_r
    body_solid = body_solid + diffuser_fin_1 + diffuser_fin_2 + diffuser_fin_3 + diffuser_fin_4
    
    # 幾何裁切 (Cut operations)
    body_solid = body_solid - hood_slope - nose_taper_top - windshield_cut - fastback_cut - rear_taper_cut
    body_solid = body_solid - hood_sduct - hood_vent_l - hood_vent_r
    for ww in wheel_wells:
        body_solid = body_solid - ww
    body_solid = body_solid - side_scoop_l - side_scoop_r
    body_solid = body_solid - headlight_slot - front_intake - taillight_slot - diffuser_tunnel
    body_solid = body_solid - interior_cavity
    
    return body_solid

if __name__ == "__main__":
    car_body()
