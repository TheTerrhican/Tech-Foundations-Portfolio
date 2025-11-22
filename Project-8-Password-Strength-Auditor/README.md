# 🔒 Project 8: Python Password Strength & Time Estimator

## 🎯 Focus Area
**Cybersecurity Fundamentals, Authentication, and Python Scripting**

## 💡 Overview
This project is a foundational cybersecurity utility developed in **Python** that enforces modern authentication policies. It analyzes a password based on criteria (length, character variety) and calculates the estimated time required for a modern GPU to successfully brute-force the password, providing a clear measure of **password entropy**.

## ⚙️ Technologies & Concepts Demonstrated
* **Python:** Core development and use of the `re` (regular expression) library.
* **Cybersecurity Fundamentals:** Enforcement of policies requiring multiple character sets (upper/lower/digits/symbols).
* **Entropy Calculation:** Demonstrating knowledge of how password length and complexity directly influence security (combinatorics/math).
* **Security Policy:** Translating security requirements (e.g., "must contain 3 of 4 types") into executable code logic.

## 📝 The Implementation
The `password_auditor.py` script performs three core functions:

1.  **Policy Check:** Verifies the password against length and character diversity rules.
2.  **Entropy Calculation:** Calculates the mathematical size of the search space (e.g., $95^{\text{length}}$ if all sets are used). 
3.  **Time Estimation:** Divides the search space by a simulated modern cracking speed (1 trillion guesses per second) to output the estimated time required for a brute-force attack.

## 🚀 Impact
This tool is excellent for demonstrating the practical implementation of security standards learned in certification programs, providing immediate feedback on a user's authentication security posture.
