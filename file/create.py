def create_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = "somtu.txt"
content = """Hello Students,
Are you Happy?
Goodbye!"""
create_file(file_name, content)
