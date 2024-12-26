# models/warehouse_item.py
from models import db
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime


class WarehouseItem(db.Model):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Назва товару
    quantity = Column(Integer, nullable=False)  # Кількість
    section = Column(String, nullable=False)  # Секція
    min_quantity = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)  # Дата оновлення

    def __init__(self, name, quantity, section, min_quantity):
        self.name = name
        self.quantity = quantity
        self.section = section
        self.min_quantity = min_quantity

    def __repr__(self):
        return f"<WarehouseItem {self.name} - Quantity: {self.quantity}>"
