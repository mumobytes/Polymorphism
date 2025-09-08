class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model} with {self.storage}GB storage.")

# Child Class (Inheritance)
class iPhone(Smartphone):
    def __init__(self, model, storage, ios_version):
        super().__init__("Apple", model, storage)  
        self.ios_version = ios_version

    # Encapsulation example (private method)
    def __secure_chip(self):
        return "Security check passed!"

    def use_face_id(self):
        print(f"Unlocking {self.model} using Face ID.")
        print(self.__secure_chip())


# Testing
phone1 = Smartphone("Samsung", "Galaxy S22", 256)
phone1.info()
phone1.call("0712345678")

iphone = iPhone("iPhone 14", 128, "iOS 17")
iphone.info()
iphone.use_face_id()
