# password_auditor.py - Python Script for Project 8

import re
import math
import time

# --- Configuration ---
MIN_LENGTH = 12
CRACKING_SPEED_GUESSES_PER_SEC = 1_000_000_000_000  # 1 Trillion guesses per second (modern GPU estimate)
CHARACTER_SETS = {
    "LOWER": r'[a-z]',
    "UPPER": r'[A-Z]',
    "DIGIT": r'[0-9]',
    "SYMBOL": r'[^a-zA-Z0-9\s]' 
}
SET_SIZE = {
    "LOWER": 26, "UPPER": 26, "DIGIT": 10, "SYMBOL": 33 # 33 is a common estimate for standard symbols
}

def check_criteria(password):
    """Checks password against complexity rules and returns the number of sets met."""
    sets_met = 0
    used_sets_size = 0
    
    for key, regex in CHARACTER_SETS.items():
        if re.search(regex, password):
            sets_met += 1
            used_sets_size += SET_SIZE[key]
            
    return sets_met, used_sets_size

def calculate_time_to_crack(length, total_set_size):
    """Calculates the estimated time to brute-force based on entropy."""
    if total_set_size == 0:
        return 0, "Too Weak"

    # 1. Calculate Entropy (Total Possible Combinations)
    entropy = total_set_size ** length 

    # 2. Calculate time in seconds
    time_in_seconds = entropy / CRACKING_SPEED_GUESSES_PER_SEC
    
    # 3. Convert time to human-readable format
    if time_in_seconds < 60:
        return time_in_seconds, f"{time_in_seconds:.2f} seconds"
    elif time_in_seconds < 3600:
        return time_in_seconds, f"{time_in_seconds / 60:.2f} minutes"
    elif time_in_seconds < 86400:
        return time_in_seconds, f"{time_in_seconds / 3600:.2f} hours"
    elif time_in_seconds < 31536000:
        return time_in_seconds, f"{time_in_seconds / 86400:.2f} days"
    else:
        return time_in_seconds, f"{time_in_seconds / 31536000:.2f} years"

def main():
    print("--- Python Password Strength Auditor ---")
    password = input(f"Enter password to analyze (Min length {MIN_LENGTH}): ")
    length = len(password)
    
    if length < MIN_LENGTH:
        print(f"\n❌ FAIL: Password must be at least {MIN_LENGTH} characters long.")
        return

    sets_met, total_set_size = check_criteria(password)
    
    print("\n--- ANALYSIS ---")
    print(f"Length: {length} (Required: {MIN_LENGTH})")
    print(f"Character Sets Met: {sets_met} out of 4")
    
    if sets_met >= 3 and length >= MIN_LENGTH:
        print("✅ VERDICT: Strong - Meets modern complexity requirements.")
    else:
        print("⚠️ VERDICT: Weak - Does not meet complexity requirements.")
        
    total_time, readable_time = calculate_time_to_crack(length, total_set_size)
    print(f"Estimated Brute-Force Time: {readable_time}")
    
    if total_time < 31536000: # Less than 1 year
        print("⚠️ ACTION: Password is vulnerable. Increase length and complexity.")
    else:
        print("✅ ACTION: Brute-force time is acceptable (>1 year).")

if __name__ == "__main__":
    main()
