import ifcopenshell

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 800

narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    # Если ширина меньше заданного порога, добавляем в список «узких» дверей
    if width is not None and width < min_width:
        narrow_doors.append({
            "name": name,
            "width": width,
            "height": height
        })

print("Узкие двери")
for d in narrow_doors:
    print(f"{d['name']}: ширина = {round(d['width'], 3)}, высота = {round(d['height'], 3)}")

if narrow_doors:
    print(f"\nКоличество найденных узких дверей: {len(narrow_doors)}")
else:
    print("\nУзких дверей не обнаружено.")
