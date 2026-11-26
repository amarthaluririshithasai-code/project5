# Project 5 – Student Performance Trend Analysis

## Description
The Student Performance Trend Analysis System is a Python-based project that compares students' marks across two assessments. It calculates improvements or declines in each subject, identifies weak subjects, calculates average marks, and classifies overall student performance.

## Objectives
- Store student marks in multiple assessments.
- Compare marks between two assessments.
- Calculate subject-wise improvement or decline.
- Identify weak subjects.
- Calculate average marks.
- Classify student performance.

## Concepts Used
- Variables and Data Types
- Lists
- For Loops
- Conditional Statements (if, elif, else)
- Arithmetic Operators
- User Input

## Performance Classification Assumptions
- Subjects: Mathematics, Physics, and Chemistry.
- Each subject carries 100 marks.
- Two assessments are compared.
- Marks below 40 are considered weak.
- Average marks of 75 or above: Excellent.
- Average marks of 50 or above: Good.
- Average marks below 50: Needs Improvement.

## Formula

**Subject-wise Improvement:**

Improvement = Assessment 2 Marks − Assessment 1 Marks

**Average Marks:**

Average = Total Marks in Assessment 2 / Number of Subjects

## Sample Output
```text
Enter Student Name: Ravi

Assessment 1: 60 55 50
Assessment 2: 80 70 75

Mathematics: Improved by 20
Physics: Improved by 15
Chemistry: Improved by 25

Weak Subjects: None
Average Marks: 75.00
Performance: EXCELLENT
```

## How to Run
1. Open the project folder in VS Code.
2. Open the Python source file.
3. Run the program.
4. Enter the student's name.
5. Enter marks for all three subjects in Assessment 1.
6. Enter marks for all three subjects in Assessment 2.
7. View the performance analysis report.

## Conclusion
This project demonstrates how Python can be used to compare student assessment marks, identify improvements and weak subjects, and classify academic performance. It helps understand lists, loops, conditional statements, and arithmetic operations.
