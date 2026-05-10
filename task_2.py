import ifcopenshell

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели: ", len(walls))

first_wall = walls[0]

print("Информация о первой стене:")
print(first_wall)

global_id = first_wall.GlobalId
name = first_wall.Name
object_type = getattr(first_wall, "ObjectType", None)
print(f"GlobalId: {global_id}")
print(f"Name: {name}")
print(f"ObjectType: {object_type}")