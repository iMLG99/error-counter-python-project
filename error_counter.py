import sys
def errorCounter(filename):
    with open(filename, "r") as file:
        text = file.read()
        sentences = text.split()

        counter = 0
        for word in sentences:
            if word.upper() == "ERROR":
                counter += 1
        return f"Error count: {counter}"


print(errorCounter(sys.argv[1]))