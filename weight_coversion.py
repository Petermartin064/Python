# Here I'm using the assumption that one package weighs 10grams and therefore, it will take 100 such packages to make one kilogram.
package_weight = float(input("Enter package weight in grams: "))
weight_kg = package_weight / 1000
no_package = weight_kg * 100
print("The weight in kilograms is", weight_kg, "kg")
print("It will take", no_package, "such packages to make", weight_kg, "kg")
