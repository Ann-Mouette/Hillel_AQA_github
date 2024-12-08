"""
Створіть клас геометричної фігури "Ромб".

Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову:
кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні
кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    """Create a geometric shape Rhombus."""

    def __init__(self, edge_a, angle_a):
        """Initialize the Rhombus."""
        self.edge_a = edge_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        """Override attribute assignment."""
        if key == 'edge_a':
            if value <= 0:
                raise ValueError('The edge length must be greater than 0')
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('The angle must be between 0 and 180 degrees')
            super().__setattr__('angle_a', value)
            super().__setattr__('angle_b', 180 - value)
        else:
            super().__setattr__(key, value)


# Example
rhombus = Rhombus(20, 45)

print('Edge length:', rhombus.edge_a)
print('Angle a:', rhombus.angle_a)
print('Angle b:', rhombus.angle_b)
