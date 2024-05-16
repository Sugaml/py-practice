def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "somtu.txt"
file_content = read_file(file_name)
if file_content:
    print("File content:")
    print(file_content)
