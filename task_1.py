import ifcopenshell

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели: ", len(walls))