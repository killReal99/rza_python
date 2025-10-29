import matplotlib.pyplot as plt
import numpy as np

# Настройка поддержки русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'

# Параметры характеристики (в относительных единицах от Iном)
I_diff_min = 0.27  # Минимальный ток срабатывания (о.е.)
I_brake1 = 0.5    # Начало первого наклонного участка (о.е.)
I_brake2 = 1.5    # Начало второго наклонного участка (о.е.)
I_brake_max = 3 # Максимальный тормозной ток (о.е.)

# Углы наклона участков (в процентах)
slope1 = 25  # Наклон первого участка (%)
slope2 = 50  # Наклон второго участка (%)

# Ток дифференциальной отсечки
I_diff_cutoff = 4.5  # Дифференциальная отсечка (о.е.)

# Преобразование наклонов в коэффициенты
k1 = slope1 / 100
k2 = slope2 / 100

# Расчет точек характеристики
# Точка A: начало характеристики (0, I_diff_min)
point_A = (0, I_diff_min)

# Точка B: конец горизонтального участка (I_brake1, I_diff_min)
point_B = (I_brake1, I_diff_min)

# Точка C: конец первого наклонного участка
I_diff_C = I_diff_min + k1 * (I_brake2 - I_brake1)
point_C = (I_brake2, I_diff_C)

# Точка D: конец второго наклонного участка
I_diff_D = I_diff_C + k2 * (I_brake_max - I_brake2)
point_D = (I_brake_max, I_diff_D)

# Создание массивов для построения графика
I_brake_AB = np.array([point_A[0], point_B[0]])
I_diff_AB = np.array([point_A[1], point_B[1]])

I_brake_BC = np.linspace(point_B[0], point_C[0], 50)
I_diff_BC = point_B[1] + k1 * (I_brake_BC - point_B[0])

I_brake_CD = np.linspace(point_C[0], point_D[0], 50)
I_diff_CD = point_C[1] + k2 * (I_brake_CD - point_C[0])

# Построение графика
fig, ax = plt.subplots(figsize=(10, 8))

# Основная характеристика
ax.plot(I_brake_AB, I_diff_AB, 'b-', linewidth=2.5, label='Тормозная характеристика')
ax.plot(I_brake_BC, I_diff_BC, 'b-', linewidth=2.5)
ax.plot(I_brake_CD, I_diff_CD, 'b-', linewidth=2.5)

# Дифференциальная отсечка (горизонтальная линия)
ax.axhline(y=I_diff_cutoff, color='r', linestyle='--', linewidth=2, label='Дифференциальная отсечка')

# Область срабатывания
I_brake_fill = np.concatenate([I_brake_AB, I_brake_BC, I_brake_CD])
I_diff_fill = np.concatenate([I_diff_AB, I_diff_BC, I_diff_CD])
ax.fill_between(I_brake_fill, I_diff_fill, 12, alpha=0.2, color='red', label='Область срабатывания')

# Область торможения
ax.fill_between(I_brake_fill, 0, I_diff_fill, alpha=0.2, color='green', label='Область торможения')

# Отметка ключевых точек
ax.plot(*point_A, 'ko', markersize=8)
ax.plot(*point_B, 'ko', markersize=8)
ax.plot(*point_C, 'ko', markersize=8)
ax.plot(*point_D, 'ko', markersize=8)

# Настройка осей и сетки
ax.set_xlabel('Тормозной ток Iторм (о.е.)', fontsize=12, fontweight='bold')
ax.set_ylabel('Дифференциальный ток Iдиф (о.е.)', fontsize=12, fontweight='bold')
ax.set_title('Характеристика срабатывания дифференциальной защиты трансформатора',
             fontsize=14, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(-0.05, 3.15)
ax.set_ylim(0, 5.5)

# НН × 2.0
I_brake_NN2 = 2.6287  # о.е.
I_diff_NN2 = 1.3144   # о.е.
point_NN2 = (I_brake_NN2, I_diff_NN2)

ax.plot(*point_NN2, 'go', markersize=11, color='darkred', markeredgewidth=2,
        markeredgecolor='darkred', label=f'НН × 2 (Iдиф={I_diff_NN2:.4f})', zorder=5)

ax.annotate('Подмена тока на стороне НН',
            xy=point_NN2,  # Координаты точки
            xytext=(40, -50),  # Смещение текста (пиксели)
            textcoords='offset points',  # Координаты смещения
            fontsize=10,
            fontweight='bold',
            ha='center',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='lightgreen',
                     edgecolor='darkgreen', linewidth=1.5),
            arrowprops=dict(arrowstyle='->', lw=2, color='darkgreen'))

plt.tight_layout()
plt.savefig('differential_protection_characteristic.png', dpi=300, bbox_inches='tight')
plt.show()

print("График успешно построен")
print("\nКоординаты ключевых точек:")
print(f"Точка A: Iторм = {point_A[0]:.2f} о.е., Iдиф = {point_A[1]:.2f} о.е.")
print(f"Точка B: Iторм = {point_B[0]:.2f} о.е., Iдиф = {point_B[1]:.2f} о.е.")
print(f"Точка C: Iторм = {point_C[0]:.2f} о.е., Iдиф = {point_C[1]:.2f} о.е.")
print(f"Точка D: Iторм = {point_D[0]:.2f} о.е., Iдиф = {point_D[1]:.2f} о.е.")
print(f"\nТок дифференциальной отсечки: {I_diff_cutoff:.2f} о.е.")




