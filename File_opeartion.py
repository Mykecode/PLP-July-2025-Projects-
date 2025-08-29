def file_operation():
    file_name = input('Enter file name to read from. ')
    try:
        with open(file_name, 'r') as files:
            reading = files.read()
            print(reading)
            
        content = input('Enter content to be added to file. ')  
            
        with open('modified.txt', 'a')  as new_file:
               write_to_file = new_file.write(reading + content)
               print('Success.')
        
    except FileNotFoundError:
            print(FileNotFoundError)
            
file_operation()