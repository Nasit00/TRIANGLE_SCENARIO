class Triangle:
    _object_count = 0 
    def __init__(self,a=None,b=None,c=None):
        if a is None and b is None and c is None:
            # default triangle
            a = b = c = 1
        elif b is None and c is None or a is None and c is None or a is None and b is None:
            b=c=a
        elif c is None:
            c=b
            b=a
        self.a = a
        self.b = b
        self.c = c
        Triangle._object_count += 1
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side length must be a positive number.")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side length must be a positive number.")
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side length must be a positive number.")
        self._c = value
    
    def which_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "scalene"
    def Is_Right_Angle_Triangle(self):
        sides = sorted([self.a, self.b, self.c])  # sort so largest side is last
        return "YES" if sides[0]**2 + sides[1]**2 == sides[2]**2 else "NO"
    def perimeter(self):
        p=self.a + self.b + self.c
        return p
    def clone(self):
        return Triangle(self.a, self.b, self.c)

    def __str__(self):
        return f"Triangle with sides: a={self.a}, b={self.b}, c={self.c} is {self.which_type()} with perimeter= {self.perimeter()}"
    
    def object_count(self):
        return Triangle._object_count


