# 🔍 Project 1: Automated Log Analyzer (Python)

## 🎯 Focus Area
**IT Support, Automation, and Incident Response**

## 💡 Overview
This project is a practical demonstration of using **Python** to solve a common IT Support challenge: efficiently identifying and isolating critical error messages from large system log files. The script automates a manual, time-consuming process, improving troubleshooting speed and accuracy.

## ⚙️ Technologies Used
* **Python 3:** Core scripting language (used for file I/O and pattern matching).
* **Linux/Bash Concepts:** Understanding of system log file locations and command-line execution.
* **Core IT/Networking:** Recognition of keywords (`ERROR`, `DENIED`, `CRITICAL`) related to system failure, access control, and denial of service issues.

## 📝 The Challenge
Manually searching massive log files for high-priority keywords is inefficient and prone to human oversight. A faster, automated method is needed for first-level incident response.

## ✅ The Solution
The **`log_analyzer.py`** script takes the full path to a log file as a command-line argument. It searches for a defined list of security and error keywords and exports all matching lines into a clean, easy-to-read report file (`error_report.txt`).

### Usage Example:
```bash
python log_analyzer.py /var/log/syslog.log
