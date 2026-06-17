import os
import re

def find_files(extension):
    """Finds all files ending with a specific extension."""
    print("Searching for files ending with " + extension + "...")
    found_files = []
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(extension):
                # Get the path relative to where we are running the script
                path = os.path.relpath(os.path.join(root, file))
                found_files.append(path)
                
    return found_files

def parse_logs(log_data):
    """Extracts timestamp, log level, and message from log lines."""
    # Pattern to match: [date time] [LEVEL] message
    pattern = r"\[(.*?)\]\s+\[(\w+)\]\s+(.*)"
    parsed_list = []

    for line in log_data.strip().split("\n"):
        match = re.match(pattern, line.strip())
        if match:
            # Create a basic dictionary for the line data
            log_dict = {
                "timestamp": match.group(1),
                "level": match.group(2),
                "message": match.group(3)
            }
            parsed_list.append(log_dict)
            
    return parsed_list

# Testing the functions
if __name__ == "__main__":
    # Test file search
    print(find_files(".py"))
    print()

    # Test log parser
    sample_logs = """
    [2026-06-17 14:22:10] [INFO] Server started successfully.
    [2026-06-17 14:23:15] [WARNING] High memory usage detected.
    [2026-06-17 14:25:00] [ERROR] Failed to connect to database.
    """
    
    results = parse_logs(sample_logs)
    for entry in results:
        print(entry)