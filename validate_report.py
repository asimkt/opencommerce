
import json
import sys

def validate_report(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return False
    except Exception as e:
        print(f"Error opening file: {e}")
        return False

    if not isinstance(data, list):
        print("Root must be a list")
        return False

    required_keys = {"title", "description", "deepLink", "filePath", "lineNumber", "confidence", "rationale", "context", "language"}

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            print(f"Item {i} is not a dictionary")
            return False

        missing_keys = required_keys - item.keys()
        if missing_keys:
            print(f"Item {i} is missing keys: {missing_keys}")
            return False

        # Validate types
        if not isinstance(item['confidence'], int):
             print(f"Item {i} confidence must be int")
             return False
        if not (1 <= item['confidence'] <= 3):
             print(f"Item {i} confidence must be between 1 and 3")
             return False

    print("Validation successful")
    return True

if __name__ == "__main__":
    if not validate_report("todo_report.json"):
        sys.exit(1)
