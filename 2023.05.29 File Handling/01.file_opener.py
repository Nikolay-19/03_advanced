try:
    open("text.txt", "r")
except FileNotFoundError:
    print("File not found")
