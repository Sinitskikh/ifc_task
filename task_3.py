import ifcopenshell
import ifcopenshell.util.element

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели: ", len(walls))

first_wall = walls[0]
print(first_wall)

psets = ifcopenshell.util.element.get_psets(first_wall)

print(psets)

for pset_name, props in psets.items():
    print("Psets: ", pset_name)
    for prop_name, value in props.items():
        print("     ", prop_name, ": ", value)