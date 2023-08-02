#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BMI Calculator


# In[ ]:





# In[ ]:


weight = float(input("Please enter your weight (in kgs) : "))
height = float(input("Please enter your height (in cms) : "))


# In[ ]:





# In[ ]:


bmi = weight / ((height/100)**2)


# In[ ]:





# In[ ]:


print(" Your BMI is " ,bmi, " (kg/m2)")


# In[ ]:





# In[ ]:


if bmi < 18.5:
    print("Your BMI is classified as 'Underweight' and your health risk is 'Minimal'. ")

elif (bmi > 18.5) and (bmi < 24.9):
    print("Your BMI is classified as 'Normal Weight' and your health risk is 'Minimal'. ")        

elif (bmi > 25) and (bmi < 29.9):
    print("Your BMI is classified as 'Overweight' and your health risk is 'Increased'. ")        

elif (bmi > 30) and (bmi < 34.9):
    print("Your BMI is classified as 'Obese' and your health risk is 'High'. ")        

elif (bmi > 35) and (bmi < 39.9):
    print("Your BMI is classified as 'Severely Obese' and your health risk is 'Very High'. ")        

else:
    print("Your BMI is classified as 'Morbidly Obese' and your health risk is 'Very High'. ")        


# In[ ]:





# In[ ]:


print("Thank you for using the BMI Calculator.")


# In[ ]:




