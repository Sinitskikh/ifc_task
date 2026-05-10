import ifcopenshell

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

stories = model.by_type("IfcBuildingStorey")

print("Схема IFC: ", model.schema)
print("Этажей: ", len(stories))

for storey in stories:
    name = storey.Name
    elevation = getattr(storey, "Elevation", None)
    print(f"Этаж: {name}, Elevation={elevation}")

print("\n--- Информация: количество этажей и список этажей с их отметками ---")