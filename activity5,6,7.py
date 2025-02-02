#activity 1
import traceback

filename= "sample.txt"   
data= input("Enter the data that you want to store:") #storing user's input as data

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:  #using 'a' to write the data 
            file.write(data)
        print(f'Data successfully written to {filename}')
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

write_to_file (filename,data)

#activity 2
def read_from_file (filename):
    try:
        with open(filename,'r') as file: #using 'r' to read the content in the file's data
            data= file.read()
        print(f' file content:\n',data)
    except FileNotFoundError:
        print (f'Error in {filename}')
    except Exception as e:
        print(f'error!!')
read_from_file(filename)

#activity 3
def append_to_file (filename,data):
    try:
        with open(filename,'a') as file: #using 'a' to append 
            file.write(data)
            print(f'Data successfully written to {filename}')

    except Exception as e:
        print ("could not read the data") #for any errors

append_to_file(filename,data)


