import ifcopenshell
import ifcopenshell.util.element

file_path = "Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")

first_wall = walls[0]
print(f"Исходное имя: {first_wall.Name}")
print(f"Исходный тип: {getattr(first_wall, "ObjectType", None)}")

# Изменяем имя файла
old_name = first_wall.Name
first_wall.Name = "MODIFIED_" + old_name

# Изменение свойств
psets = ifcopenshell.util.element.get_psets(first_wall)

if "Pset_WallCommon" in psets:
    for rel in first_wall.IsDefinedBy:
        if rel.is_a("IfcRelDefinesByProperties"):
            pset = rel.RelatingPropertyDefinition
            if pset.Name == "Pset_WallCommon":
                for prop in pset.HasProperties:
                    if prop.Name == "IsExternal":
                        prop.NominalValue.wrappedValue = True
                        print("Свойство IsExternal изменено на True.")

# Сохранение изменённой модели в новый файл,
new_file_path = "modified.ifc"
model.write(new_file_path)
print(f"\nФайл сохранен как {new_file_path}")

# Повторное открытие файла и проверка
new_model = ifcopenshell.open(new_file_path)
check_wall = new_model.by_guid(first_wall.GlobalId)
check_psets = ifcopenshell.util.element.get_psets(check_wall)

# Проверка имени
print(f"Обновленное имя: {check_wall.Name}")

if "Pset_WallCommon" in check_psets:
    result = check_psets["Pset_WallCommon"].get("IsExternal")
    print(f"Проверка после сохранения. IsExternal = {result}")