import numpy as np

well_dept = np.array([56, 12, 66, 19, 32, 72, 27, 32])

# Крок 1: середнє значення
average = np.average(well_dept)
print("Крок 1, середнє:", average)

# Крок 2: відхилення кожного значення від середнього
deviations = well_dept - average
print("Крок 2, відхилення:", deviations)

# Крок 3: квадрат відхилень
squared_deviations = deviations ** 2
print("Крок 3, квадрати відхилень:", squared_deviations)

# Крок 4: середнє значення квадратів відхилень (дисперсія)
variance = np.average(squared_deviations)
print("Крок 4, дисперсія:", variance)

# Крок 5: квадратний корінь (SD)
SD = np.sqrt(variance)
print("Крок 5, SD:", SD)

# Перевірка вбудованою функцією
print("Перевірка np.std:", np.std(well_dept))
