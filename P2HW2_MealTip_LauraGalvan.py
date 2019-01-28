#Create a new Python code file named P2HW2_MealTip_FirstLast.py 
#(replace "FirstLast" with your own name)
#.Add a title comment block to the top of the new Python file using the following form:

 # Calculate total cost of meal
 # Date: 1/23/19
 # CTI-110 P2HW2 - Meal and Tip calculator
 # Laura L. Galvan
 #
 #======================================================

print("Meal and Tip Calculator\n");
mealCost = float(input("Enter amount of meal: "))
Tip15 = mealCost * .15
Tip18 = mealCost *.18
Tip20 = mealCost * .20
Cost15 = mealCost + Tip15
Cost18 = mealCost + Tip18
Cost20 = mealCost + Tip20
print("total Costs for meal and tip ",
      "Tip 15% ", round(Tip15,2), "\tTotal Cost = ", round(Cost15,2))

print("total Costs for meal and tip ",
      "Tip 18% ", round(Tip18,2), "\tTotal Cost = ", round(Cost18,2))
print("total Costs for meal and tip ",
      "Tip 20% ", round(Tip20,2), "\tTotal Cost = ", round(Cost20,4))
