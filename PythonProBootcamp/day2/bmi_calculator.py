weight = 85
height = 1.67

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

print(f"{bmi}")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("normal weight")
else:
    print("overweight")