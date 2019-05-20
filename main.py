from rectangle_class import Rectangle

a = Rectangle(w=4, h=4, x=0, y=0)
b = Rectangle(w=4, h=4, x=-1, y=-1)
c = a.intersection_on_flat(b)
print(a.get_coords())
print(b.get_coords())
print(123, c.get_coords())