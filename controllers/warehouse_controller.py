from flask import Blueprint, jsonify, request
from models.warehouse_model import WarehouseItem
from models import db

warehouse_blueprint = Blueprint("warehouse", __name__)


@warehouse_blueprint.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name")
    quantity = data.get("quantity")
    section = data.get("section")

    if name:
        new_item = WarehouseItem(name=name, quantity=quantity, section=section)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item added", "name": name}), 201

    return jsonify({"error": "Name is required"}), 400


@warehouse_blueprint.route("/items", methods=["GET"])
def get_items():
    items = WarehouseItem.query.all()
    return jsonify(
        [
            {"name": item.name, "quantity": item.quantity, "section": item.section}
            for item in items
        ]
    )


def setup_warehouse_routes(app):
    app.register_blueprint(warehouse_blueprint, url_prefix="/warehouse")
