# while True:
#     pass  # đợi một sự kiện nhưng không làm gì cả

# #########################################################################

def http_error():
    x = int(input("nhập mã: "))
    match x:
        case 400:
            return "Bad request"
        case 404 | 405:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 450:
            return "Something's wrong with the internet"
        
print(http_error())

# #########################################################################

class point:
    def __init__(self):
        self.x = int(input("Nhập biến X: "))
        self.y = int(input("Nhập biến y: "))

def where_is(point):
    match (point.x, point.y):
        case (0, 0):
            print("Gốc")
        case (0, y):
            print(f"Điểm trên trục y với giá trị y={y}")
        case (x, 0):
            print(f"Điểm trên trục x với giá trị x={x}")
        case (x, y):
            print(f"Điểm khác với tọa độ (x={x}, y={y})")
        case _:
            raise ValueError("Không phải là một điểm")

print(where_is(point()))

# #########################################################################

from enum import Enum 
class color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

color = color(input("chọn 3 màu red, green, blue: "))

match color:
    case color.RED:
        print("màu đỏ!")
    case color.GREEN:
        print("màu xanh lá!")
    case color.BLUE:
        print("mauf xanh nước biển!")