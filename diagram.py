import matplotlib.pyplot as plt
import numpy as np

# Входные данные (напряжения и фазы)
data = {
    "АБ": {"U": 6.345, "F": 37.98},
    "АВ": {"U": 9.92, "F": 34.52},
    "АГ": {"U": 9.459, "F": 25.94},
    "АД": {"U": 11.337, "F": 6.38},
    "АЕ": {"U": 9.983, "F": 15.83},
}

# Уменьшаем масштаб напряжений для удобства отображения
scale_factor = 0.1

plt.figure(figsize=(8, 8))

# Построение векторов
for key, values in data.items():
    magnitude = values["U"] * scale_factor  # Масштабируем напряжение
    angle = np.radians(values["F"])  # Переводим угол в радианы
    x = magnitude * np.cos(angle)  # Реальная часть
    y = magnitude * np.sin(angle)  # Мнимая часть

    # Рисуем вектор
    plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, label=f"{key}: {values['U']} В, {values['F']}°")

    # Добавляем подпись к вектору
    plt.text(x * 1.2, y * 1.2, key, fontsize=10, ha='center')

# Настройка графика
plt.title("Векторная диаграмма напряжений")
plt.xlabel("Реальная часть напряжения (В)")
plt.ylabel("Мнимая часть напряжения (В)")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()
