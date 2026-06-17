import os
import re
import json
from typing import Dict, List

class TextParserAutomation:
    """A class to handle file processing and structured text parsing."""
    
    def __init__(self, target_directory: str = "."):
        self.target_directory = target_directory

    def find_and_list_files(self, extension: str) -> List[str]:
        """Automates file processing by scanning directories for specific file types."""
        print(f"Scanning '{self.target_directory}' for {extension} files...")
        matched_files = []
        
        for root, _, files in os.walk(self.target_directory):
            for file in files:
                if file.endswith(extension):
                    relative_path = os.path.relpath(os.path.join(root, file))
                    matched_files.append(relative_path)
        
        return matched_files

    def parse_log_data(self, log_text: str) -> List[Dict[str, str]]:
        """Parses structured text data using Regular Expressions (Regex).
        
        Extracts Timestamp, Log Level, and Message from standard log formats.
        """
        # Example pattern: [2026-06-17 10:42:01] [ERROR] Connection failed
        log_pattern = r"\[(?P<timestamp>.*?)\]\s+\[(?P<level>\w+)\]\s+(?P<message>.*)"
        parsed_entries = []

        for line in log_text.strip().split("\n"):
            match = re.match(log_pattern, line)
            if match:
                parsed_entries.append(match.groupdict())
                
        return parsed_entries

# --- Demonstration of the Module ---
if __name__ == "__main__":
    automation = TextParserAutomation()

    # 1. Simulate File Automation
    # (Finds all Python files in the current workspace)
    py_files = automation.find_and_list_files(".py")
    print(f"Found files: {py_files}\n")

    # 2. Simulate Structured Text Parsing
    mock_logs = """
    [2026-06-17 14:22:10] [INFO] Server started successfully.
    [2026-06-17 14:23:15] [WARNING] High memory usage detected.
    [2026-06-17 14:25:00] [ERROR] Failed to connect to database.
    """
    
    print("Parsing structured log data...")
    parsed_results = automation.parse_log_data(mock_logs)
    print(json.dumps(parsed_results, indent=4))