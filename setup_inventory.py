from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Базовий клас для моделей
Base = declarative_base()


# Модель для таблиці inventory
class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Назва товару
    quantity = Column(Integer, nullable=False)  # Кількість
    section = Column(String, nullable=False)  # Секція
    min_quantity = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)  # Дата оновлення


# Налаштування бази даних
DATABASE_URL = "sqlite:///mydatabase.db"  # SQLite база даних
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Створення таблиць

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Дані для заповнення складу
items = [
    # Сипучі
    {"name": "Мука", "quantity": 100, "section": "Сипучі", "min_quantity": 10},
    {"name": "Цукор", "quantity": 200, "section": "Сипучі", "min_quantity": 10},
    {"name": "Пропіонат", "quantity": 50, "section": "Сипучі", "min_quantity": 10},
    # Холодильник
    {"name": "Маргарин", "quantity": 30, "section": "Холодильник", "min_quantity": 10},
    {"name": "Пудра", "quantity": 70, "section": "Холодильник", "min_quantity": 10},
    {"name": "Меланж", "quantity": 25, "section": "Холодильник", "min_quantity": 10},
    {"name": "Творог", "quantity": 40, "section": "Холодильник", "min_quantity": 10},
    # Додаткові товари
    {"name": "Розпушувач", "quantity": 15, "section": "Додаткові", "min_quantity": 10},
    {
        "name": "Гофра (марсе)",
        "quantity": 10,
        "section": "Додаткові",
        "min_quantity": 10,
    },
    {
        "name": "Гофра (червона)",
        "quantity": 8,
        "section": "Додаткові",
        "min_quantity": 10,
    },
    {
        "name": "Папір підкладочний",
        "quantity": 20,
        "section": "Додаткові",
        "min_quantity": 10,
    },
]

# Додавання даних у базу
for item in items:
    inventory_item = InventoryItem(
        name=item["name"],
        quantity=item["quantity"],
        section=item["section"],
        min_quantity=item["min_quantity"],
    )
    session.add(inventory_item)

# Збереження змін у базу
session.commit()

# Перевірка: виведення всіх товарів з бази
for item in session.query(InventoryItem).all():
    print(
        f"ID: {item.id}, Назва: {item.name}, Кількість: {item.quantity}, Секція: {item.section}, Оновлено: {item.last_updated}"
    )

# Закриття сесії
session.close()
