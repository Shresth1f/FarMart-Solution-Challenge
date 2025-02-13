One approach considered was loading the entire log file into memory, splitting it into individual lines, and then filtering based on the specified date. 
This method was simple and easy to implement, allowing for fast data processing once the file was fully loaded. 
However, it proved to be impractical for large files, particularly for a 1TB log file, as it would consume excessive memory, potentially causing crashes and significant performance degradation. 
Due to its inefficiency in handling massive datasets, this approach was ultimately discarded.

Chosen Solution:
The chosen solution involved processing the log file line by line, ensuring that only one line was loaded into memory at any given time. 
This method was highly memory-efficient, as it prevented excessive resource usage while still allowing for effective log extraction. 
Additionally, it significantly reduced unnecessary I/O operations, making it faster and more optimized than the in-memory approach. 
Furthermore, it was scalable, meaning it could handle extremely large files without overwhelming system resources. 
Although this approach was slightly more complex to implement, it was selected as the final solution due to its efficiency and ability to process large log files while maintaining optimal performance.

Steps to run:
Navigate to the script’s directory
Example:
python extract_logs.py 2025-02-13
Logs will be saved to:
output\output_2025-02-13.txt
