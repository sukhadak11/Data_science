'''
Problem Statement (Question): Hospital Billing System
A hospital charges its patients based on the following:
•	Room charges per day: ₹2,000
•	Doctor consultation fee (flat): ₹1,500
•	Lab test charges: Based on the number of tests taken. Each test costs ₹300
•	Medicine charges: Total cost of medicines provided
•	Discount: If the total bill (before discount) exceeds ₹10,000, a 10% discount is applied
Write a Python program to calculate the final bill for a patient who:
•	Stayed for 4 days
•	Had 3 lab tests
•	Had medicine charges of ₹2,400
'''

room_charges_per_day = 2000
doctor_consultation_fee = 1500
Lab_test_charges = 300
medicine_charges = 2400

total_room_charges = room_charges_per_day * 4
total_doctor_consultation_fee = doctor_consultation_fee
total_lab_test_charges = Lab_test_charges * 3
total_medicine_charges = medicine_charges

total = total_room_charges+ total_doctor_consultation_fee + total_lab_test_charges + total_medicine_charges

if total > 10000:
    discount = total * 0.10
else:
    discount = 0

final_total = total - discount

print("Total:", final_total)
