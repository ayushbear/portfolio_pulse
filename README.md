# Portfolio Manager: Investment Risk Tool

A tool to track a 7-fund investment strategy and calculate if the portfolio is too risky. This project taught me how to organize professional Python code into separate files.

##  What I Used
 **Python Modules:** I split the code into `main.py`, `analytics.py`, and `database.py`.
 **JSON:** Used as a simple way to store my fund list.

##  What it Does
 **Modular Code:** Keeps the math logic separate from the file-saving logic.
 **Risk Score (HHI):** Calculates a "Concentration Score" to see if I have too much money in one fund.
 **Crash Math:** Calculates exactly how much the portfolio needs to grow to "break even" after a market drop.
 **Goal Forecast:** Predicts how many months it takes to reach a specific target (like ₹10 Lakhs).

##  What I Learned
The biggest lesson here was **Separation of Concerns.** By putting my math in one file and my storage code in another, the project is much easier to read and fix.