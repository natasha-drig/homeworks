fruits = {"груша": "желтый", 
          "яблоко": "красный", 
          "киви": "зеленый",
          "гранат": "красный",
          "банан": "желтый"};
for fruit, color in fruits.items():
    if "к" in color:
        print (fruit)
