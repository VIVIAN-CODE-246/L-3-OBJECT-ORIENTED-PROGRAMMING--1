class food:
    def __init__ (self, name, nutrient):
        self.name = name
        self.nutrient = nutrient

food1 = food("Rice", "Carbohydrate")
food2 = food("Beans", "Protein")
print("Hello, I am", food1.name, "and I am a", food1.nutrient)Sir