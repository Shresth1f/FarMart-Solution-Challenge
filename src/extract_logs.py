import os
import sys


if len(sys.argv) < 2:
    print("Usage: python extract_logs.py <YYYY-MM-DD>")
    sys.exit(1)


target_date = sys.argv[1]  
log_file_path = r"C:\Users\shresth\Desktop\logs_2024.log\logs_2024.log"  
output_dir = "output"  
output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")


os.makedirs(output_dir, exist_ok=True)


print(f"Extracting logs for {target_date} from {log_file_path}...")

with open(log_file_path, "r", encoding="utf-8") as log_file, open(output_file_path, "w", encoding="utf-8") as output_file:
    for line in log_file:
        if line.startswith(target_date):
            output_file.write(line)

print(f"Extraction complete! Logs saved to: {output_file_path}")
