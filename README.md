# TRIANGLE_SCENARIO
# 🔺 Triangle Class in Python

A Python implementation of a **Triangle** class with encapsulated side lengths (`a`, `b`, `c`) and built-in validation.  
The class demonstrates **object-oriented programming (OOP)** concepts like class variables, encapsulation with properties, operator overloading (`__str__`), and instance counting.

---

## ✨ Features

- ✅ Encapsulation with properties for `a`, `b`, `c`  
- ✅ Input validation (sides must be positive numbers)  
- ✅ Triangle type detection:
  - Equilateral
  - Isosceles
  - Scalene  
- ✅ Right-angle triangle check (Pythagoras theorem)  
- ✅ Perimeter calculation  
- ✅ Clone method to duplicate triangles  
- ✅ Object counter to track created instances  
- ✅ String representation for easy printing  

---

## 📂 Class Overview

### Attributes
- `_object_count: int` → class variable tracking total triangles created  
- `_a: double` → private side length  
- `_b: double` → private side length  
- `_c: double` → private side length  

### Properties
- `a: double` → getter/setter for `_a`  
- `b: double` → getter/setter for `_b`  
- `c: double` → getter/setter for `_c`  

### Methods
- `__init__(a, b, c)` → constructor with validation & default sides  
- `which_type()` → returns `"equilateral"`, `"isosceles"`, or `"scalene"`  
- `Is_Right_Angle_Triangle()` → returns `"YES"` or `"NO"`  
- `perimeter()` → calculates perimeter of the triangle  
- `clone()` → creates a copy of the current triangle  
- `__str__()` → string description of the triangle  
- `object_count()` → returns number of triangles created  

---

## 📝 Example Usage

```python
from triangle import Triangle

# Create triangles
t1 = Triangle(3, 4, 5)
t2 = Triangle(5, 5, 5)

print(t1)  
# Output: Triangle with sides: a=3, b=4, c=5 is scalene with perimeter= 12

print(t2.which_type())  
# Output: equilateral

print(t1.Is_Right_Angle_Triangle())  
# Output: YES

print(t2.perimeter())  
# Output: 15

# Clone triangle
t3 = t1.clone()
print(t3)  
# Output: Triangle with sides: a=3, b=4, c=5 is scalene with perimeter= 12

# Object count
print(t1.object_count())

🚀 Future Enhancements

Area calculation (Heron’s formula)

Support for degenerate/invalid triangle detection

Overloading comparison operators (==, <, >) to compare triangles by perimeter or area  
# Output: 3

