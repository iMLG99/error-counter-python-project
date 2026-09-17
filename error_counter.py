import sys
import json

def error_counter_web(filename):
    with open(filename, "r") as file:
        text = file.read()
        sentences = text.split()

        counter = 0
        for word in sentences:
            if "ERROR" in word.upper():
                counter += 1
        return f"Error count: {counter}"

def error_counter_json(filename):
    error_count = 0
    with open(filename, "r") as file:
        for line in file:
            error = json.loads(line)
            if error.get("level") in ["ERROR", "CRITICAL"]:
                error_count += 1
        return f"Error count: {error_count}"

def error_counter_java(filename):
    error_count = 0
    with open(filename, "r") as file:
        text = file.read()
        sentences = text.split()
        for word in sentences:
            if word == "ERROR" or word == "FATAL":
                error_count += 1
        return f"Error Count: {error_count}"

def error_counter_linux(filename):
    error_count = 0
    error_keywords = ["failed", "timeout", "deleted inode", "error"]
    with open(filename, "r") as file:
        text = file.read()
        if "deleted inode" in text:
            error_count += 1
        sentences = text.split()
        for word in sentences:
            if word.lower() in error_keywords:
                error_count += 1
        return f"Error Count: {error_count}"

error_type = input("type of error file? (web, json, linux, java): ")
if error_type == "web":
    print(error_counter_web(sys.argv[1]))
elif error_type == "json":
    print(error_counter_json(sys.argv[1]))
elif error_type == "linux":
    print(error_counter_linux(sys.argv[1]))
elif error_type == "java":
    print(error_counter_java(sys.argv[1]))
else:
    print("invalid file type")
