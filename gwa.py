# Kenneth John Costa
# Assignment 4
# GWA (Highest)

# Write a Python program that read a file containing the name of 
# 20 students together with their GWA. The program will outputs the 
# name of the student who got the highest GWA (including the GWA). 

# Create a txt file that will read a file with 20 names and GWA on it
with open("name_gwa.txt", "r") as input_file:
# Declare a variable for the student with highest GWA and its GWA
     highest_gwa_name = ""
     ceiling_gwa = 5.00
# Split the student's name and its corresponding GWA
# Convert the gwa of students into float
# If GWA is the highest, showcase the name and its GWA
# Print the output