'''
Ejercicios 2 & Reto 3
'''

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length(start, end)
        self.slope = self.compute_slope(start, end)

    def compute_length(self, start: Point, end: Point) -> float:
        length = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5
        return length

    def compute_slope(self, start: Point, end: Point) -> float:
        if end.x - start.x == 0:
            raise ValueError("La pendiente es indefinida para líneas verticales.")
        slope = (end.y - start.y) / (end.x - start.x)
        return slope

    def compute_vertical_cross(self) -> bool:
        if self.start.x < 0 and self.end.x > 0:
            return True
        elif self.end.x < 0 and self.start.x > 0:
            return True
        else:
            return False
    
    def compute_horizontal_cross(self) -> bool:
        if self.start.y < 0 and self.end.y > 0:
            return True
        elif self.end.y < 0 and self.start.y > 0:
            return True
        else:
            return False

class Rectangle: #Inicialización con métodos dinámicos
    def __init__ (self, *args, **kwargs):
        self.bottom_left:  Point # type: ignore
        self.top_right:  Point # type: ignore
        self.center:  Point # type: ignore
        self.width: float # type: ignore
        self.height:  float # type: ignore
        if args and kwargs:
            raise ValueError("Solamente puedes usar argumentos posicionales o tipo dict, no ambos.")

        if args:
            if len(args) == 2 and all(isinstance(p, Point) for p in args): #all: verifica que todos los elementos cumplan, reemplazo de "isinstance(args[0], Point) and isinstance(args[1], Point)"
                self.init_borders(*args)
            
            if len(args) == 3 and isinstance(args[0], Point):
                self.init_bl_width_height(*args)

            if len(args) == 4 and all(isinstance(p, Line) for p in args):
                self.init_line(*args)
        
        else:
            if len(kwargs) == 3 and {"center", "width", "height"}.issubset(kwargs.keys()):
                self.init_center_width_height(**kwargs)


    def init_borders(self, bottom_left: Point, top_right: Point):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.width = top_right.x - bottom_left.x
        self.height = top_right.y - bottom_left.y
        self.center = Point(

                (bottom_left.x + top_right.x) / 2,
                (bottom_left.y + top_right.y) / 2,
            )


    def init_bl_width_height(self, bottom_left: Point, width: float, height: float):
        self.bottom_left = bottom_left
        self.top_right = Point(
                    bottom_left.x + width,
                    bottom_left.y + height)
        self.center = Point(
                bottom_left.x + width / 2,
                bottom_left.y + height / 2
            )
        self.width = width
        self.height = height

    def init_center_width_height(self, center: Point, width: float, height: float):
        self.center = center
        self.width = width
        self.height = height
        self.bottom_left = Point(
                center.x - width / 2,
                center.y - height / 2
            )
        self.top_right = Point(
                center.x + width / 2,
                center.y + height / 2
            )

    def init_line(self, line1: Line, line2: Line, line3: Line, line4: Line):
        #validar que las líneas formen un rectángulo
        if line1.start.x == line2.start.x and\
        line3.start.x == line4.start.x and line1.start.y == line4.start.y\
        and line2.start.y == line3.start.y:

            minimo_x = min(line1.start.x, line2.start.x, line3.start.x, line4.start.x)
            minimo_y = min(line1.start.y, line2.start.y, line3.start.y, line4.start.y)

            maximo_x = max(line1.start.x, line2.start.x, line3.start.x, line4.start.x)
            maximo_y = max(line1.start.y, line2.start.y, line3.start.y, line4.start.y)
        
            self.bottom_left = Point(minimo_x, minimo_y)
            self.top_right = Point(maximo_x, maximo_y)

            self.width = self.top_right.x - self.bottom_left.x
            self.height = self.top_right.y - self.bottom_left.y
            
            self.center = Point(
                (self.bottom_left.x + self.top_right.x) / 2,
                (self.bottom_left.y + self.top_right.y) / 2
            )

    ## Cálcular area,perimetro y pertenece a rectángulo

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2*(self.width + self.height)

    def belongs(self, punto: Point) -> bool:
        if not isinstance(punto, Point):
            raise TypeError("El argumento debe ser un Point.")
        
        value = self.bottom_left.x <= punto.x <= self.top_right.x and self.bottom_left.y <= punto.y <= self.top_right.y   
        return value

if __name__ == "__main__":
    linea1 = Line(Point(0, 0), Point(0.1, 2))
    linea2 = Line(Point(0, 2), Point(3, 2))
    linea3 = Line(Point(3, 2), Point(2.9, 0))
    linea4 = Line(Point(3, 0), Point(0, 0))
    rectangulo = Rectangle(linea1, linea2, linea3, linea4)
    print(f"Área: {rectangulo.area()}")
    print(f"Perímetro: {rectangulo.perimeter()}")
   # print(linea1.slope, linea1.length, linea1.compute_vertical_cross(), linea1.compute_horizontal_cross())