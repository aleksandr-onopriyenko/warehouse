from .warehouse_controller import setup_warehouse_routes


def setup_routes(app):
    setup_warehouse_routes(app)
