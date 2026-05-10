import ifcopenshell

file_path = r"C:\Users\1686768\SINITSKIKH\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")
print(f"Всего дверей в исходной модели: {len(doors)}")

min_width = 900.0
removed_count = 0

# Фильтрация по критерию
for door in doors:
    width = getattr(door, "OverallWidth", 0)
    if width < min_width:
        model.remove(door)

# Создание подмодели
output_path = r"C:\Users\1686768\SINITSKIKH\doors_wide.ifc"
model.write(output_path)
print(f"Подмодель сохранена как: {output_path}")

# Проверка количества дверей
check_model = ifcopenshell.open(output_path)
final_doors = check_model.by_type("IfcDoor")

print(f"Количество дверей в новом файле: {len(final_doors)}")

# Проверка соответствия критерию
for d in final_doors:
    width = getattr(d, "OverallWidth", 0)
    print(f"Дверь: {d.Name}, ширина = {round(width, 3)}")

