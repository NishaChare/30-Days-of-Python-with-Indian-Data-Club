import threading
import requests

# Function to download a single file
def download_file(url, filename):
    try:
        print(f"Starting download: {filename}")
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Completed download: {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# List of file URLs to download
file_urls = [
    ("file:///C:/Users/punam/OneDrive/NISHA/OneDrive/Desktop/my%20resume/NISHA%20CHARE.pdf", "file1.pdf"),
]

# Create a list to hold threads
threads = []

# Create and start a thread for each download
for url, filename in file_urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All downloads completed.")
