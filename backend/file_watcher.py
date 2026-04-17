import time, requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parser import parse_snort_alert

class SnortLogHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename
        
        file = open(self.filename, 'r')
        file.seek(0, 2)
        self.last_position = file.tell() # Save that position
        file.close()

    # This built-in function triggers instantly whenever a file is modified!
    def on_modified(self, event):
        # Make sure we are only reacting to our specific log file
        if not event.src_path.endswith(self.filename):
            return
            
        with open(self.filename, 'r') as file:
            # Jump exactly to where we stopped last time
            file.seek(self.last_position)
            
            # Read any new lines that were added
            new_lines = file.readlines()
            
            # Save our new position
            self.last_position = file.tell()
            
            # Parse the new lines!
            for line in new_lines:
                if line.strip(): # Make sure it's not a blank line
                    print("🚨 NEW ALERT DETECTED! 🚨")
                    parsed_alert = parse_snort_alert(line)
                    try:
                        requests.post("http://127.0.0.1:8000/alerts/", json=parsed_alert)
                        print("✅ Alert successfully pushed to API pipeline!")
                    except Exception as e:
                        print(f"❌ Failed to push alert: {e}")

# This is just for testing!
if __name__ == "__main__":
    path_to_watch = "mock_snort.log"
    event_handler = SnortLogHandler(path_to_watch)
    observer = Observer()
    
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()
    
    print(f"👀 Watching {path_to_watch} for new alerts...")
    
    try:
        while True:
            time.sleep(1) # Keep the script running forever
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
