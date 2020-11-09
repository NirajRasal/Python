import os

file_name = input('enter the file name that you want to delete(tempfile.txt):')


if os.path.exists(file_name):           #checks if file exist or not
    os.remove(file_name)
    print('file deleted!!!')
else:
      print('file does not exist')      #dispaly message if file does not exist

#os.rmdir()  to remove empty folders