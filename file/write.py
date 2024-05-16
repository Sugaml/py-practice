def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            file.write('\n')
        print(f"Content appended to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "somtu.txt"
content_to_append = "SOMTU Family."
append_to_file(file_name, content_to_append)
