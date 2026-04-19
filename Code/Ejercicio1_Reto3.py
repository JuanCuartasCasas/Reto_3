##Actividad 1: Reto_3:Herencia


#1. Generación clase punto, con el fin de tener coordenadas

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

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

        

class Cuadrado(Rectangle):
    def __init__(self, length: float,*, center: Point, bottom_left):
       length = float(length)
       if center and bottom_left:
           raise ValueError("Solo puedes usar centro o abajo_izquierda, no ambos.")
       if center is None and bottom_left is None:
            raise ValueError("Debes proporcionar centro o abajo_izquierda.")
       if center:
           super().__init__(center=center, width=length, height=length)
       else:
            super().__init__(bottom_left=bottom_left, width=length, height=length)
       self.length = length

if __name__ == "__main__":
    
    rectangulo_1 = Rectangle(Point(3,4), Point(10, 6))
    rectangulo_2 = Rectangle(Point(1,2), 5, 3)
    rectangulo_3 = Rectangle(center=Point(5,5), width=4, height=4)
    print(f"Rectángulo 1: BL={rectangulo_1.bottom_left.x}, {rectangulo_1.bottom_left.y}, TR={rectangulo_1.top_right.x}, {rectangulo_1.top_right.y}, C={rectangulo_1.center.x}, {rectangulo_1.center.y}")
    print(f"  area={rectangulo_1.area()}, perimetro={rectangulo_1.perimeter()}")
    print(f"Rectángulo 2: BL={rectangulo_2.bottom_left.x}, {rectangulo_2.bottom_left.y}, TR={rectangulo_2.top_right.x}, {rectangulo_2.top_right.y}, C={rectangulo_2.center.x}, {rectangulo_2.center.y}")
    print(f"  area={rectangulo_2.area()}, perimetro={rectangulo_2.perimeter()}")
    print(f"Rectángulo 3: BL={rectangulo_3.bottom_left.x}, {rectangulo_3.bottom_left.y}, TR={rectangulo_3.top_right.x}, {rectangulo_3.top_right.y}, C={rectangulo_3.center.x}, {rectangulo_3.center.y}")
    print(f"  area={rectangulo_3.area()}, perimetro={rectangulo_3.perimeter()}")

    punto = Point(4,5)
    print(f"El punto ({punto.x}, {punto.y}) pertenece al rectángulo 1: {rectangulo_1.belongs(punto)}")
    print(f"El punto ({punto.x}, {punto.y}) pertenece al rectángulo 2: {rectangulo_2.belongs(punto)}")
    print(f"El punto ({punto.x}, {punto.y}) pertenece al rectángulo 3: {rectangulo_3.belongs(punto)}")

    cuadrado = Cuadrado(4, center=Point(2,2), bottom_left=None)
    print(f"Cuadrado: BL={cuadrado.bottom_left.x}, {cuadrado.bottom_left.y}, TR={cuadrado.top_right.x}, {cuadrado.top_right.y}, C={cuadrado.center.x}, {cuadrado.center.y}")
    print(f"  area={cuadrado.area()}, perimetro={cuadrado.perimeter()}")
    print(f"El punto ({punto.x}, {punto.y}) pertenece al cuadrado: {cuadrado.belongs(punto)}")