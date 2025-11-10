import sys

# Define the list of keywords you want to search for
# These keywords are common indicators of system failure or security issues.
SEARCH_KEYWORDS = ["ERROR", "FAIL", "CRITICAL", "DENIED", "REFUSED"]
OUTPUT_FILE = "error_report.txt"

def analyze_log(log_file_path):
    """Reads a log file, searches for specific keywords, and writes matches to a report."""
    print(f"[*] Analyzing log file: {log_file_path}...")
    
    found_count = 0
    
    try:
        # Open the log file for reading and the output file for writing (creates it if it doesn't exist)
        with open(log_file_path, 'r') as log_file, open(OUTPUT_FILE, 'w') as output_file:
            # Write a professional header for the report file
            output_file.write(f"--- Automated Error Analysis Report for {log_file_path} ---\n")
            output_file.write(f"Keywords Searched: {', '.join(SEARCH_KEYWORDS)}\n\n")

            for line_number, line in enumerate(log_file, 1):
                # Check if any keyword (converted to uppercase) exists in the line
                if any(keyword in line.upper() for keyword in SEARCH_KEYWORDS):
                    # Write the matching line to the report file
                    output_file.write(f"[Line {line_number}]: {line.strip()}\n")
                    found_count += 1

        print(f"[+] Analysis complete. Found {found_count} matching lines.")
        print(f"[+] High-priority report saved to {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"[!] Critical Error: The log file specified at '{log_file_path}' was not found.")
    except Exception as e:
        print(f"[!] An unexpected error occurred during processing: {e}")

if __name__ == "__main__":
    # Check if the user provided exactly one argument (the path to the log file)
    if len(sys.argv) != 2:
        print("\nUsage: python log_analyzer.py <path_to_log_file>")
        print("Example: python log_analyzer.py /var/log/syslog\n")
    else:
        # Execute the main function with the provided file path
        analyze_log(sys.argv[1])
