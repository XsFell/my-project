
from database import get_connection


class FleetManager:
    def __init__(self):
        self.conn = get_connection()

    def add_vehicle(self, vehicle):
        cursor = self.conn.cursor()
        if vehicle.__class__.__name__ == "Car":
            cursor.execute("INSERT INTO vehicles (type, brand, model, year, seats) VALUES (?, ?, ?, ?, ?)", ("car", vehicle.brand, vehicle.model, vehicle.year, vehicle.seats))
        elif vehicle.__class__.__name__ == "Motorcycle":
            cursor.execute("INSERT INTO vehicles (type, brand, model, year, has_sidecar) VALUES (?, ?, ?, ?, ?)", ("mototrcycle", vehicle.brand, vehicle.model, vehicle.year, vehicle.has_sidecar))
        self.conn.commit()

    def remove_vehicle(self, brand):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM vehicles WHERE brand = ?", (brand,))
        self.conn.commit()

    def update_vehicle(self, brand, new_model):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE vehicles SET model = ? WHERE brand = ?", (new_model, brand))
        self.conn.commit()

    def list_vehicles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM vehicles")
        for row in cursor.fetchall():
            print(row)

    def find_vehicle(self, keyword):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM vehicles WHERE brand LIKE ? OR model LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        for row in cursor.fetchall():
            print(row)

    def close(self):
        self.conn.close()


        