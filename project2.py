def append_text_to_file(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')
        print(f"Successfully appended to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# File path
file_path = 'example.txt'
# Text to append
text_to_append = 'This is the appended text.'
append_text_to_file(file_path, text_to_append)
