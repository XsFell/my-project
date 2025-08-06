from vehicles import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar ):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"Motorcycle: {self.full_name} - Sidecar : {'Yes' if self.has_sidecar else 'NO'}"