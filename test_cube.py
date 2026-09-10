from cadgen import build123d as bd
from cadgen import step

@step(out="cube.step")
def sample_cube():
    """
    測試範例：建立一個 20x20x20 mm、中心帶有直徑 6mm 穿孔的立方體
    """
    return bd.Box(20, 20, 20) - bd.Hole(radius=3, depth=20)

if __name__ == "__main__":
    sample_cube()
