#f=open('file_name', 'w') open the file in write mode
#'r'=> open the file in read mode, is also the default if no mode is specified
#'r+'=> open the file in read and write mode
#'a'=>open the file for appending, data is added to the end of the file
#'w'=> open the file in write mode
#'b'=> if appended to the mode open the file in binary mode. data are read and written in form of bytes objects(used for files that do not contain text)
#with=> using the keyword 'with' to open file is a good practice when dealing with file objects. it allowd the file to be properly closed afterits suite finishes even if an exception is raised at some point no need to use try-finally block
# with open('file_name') as f:
#     read_data = f.read()
#if you are not using 'with' you have to immediately close the file 'f.close()' to free system resources used by the file.
#You can not do any operation on the file after it has been closed
#f.read(size)=> size specifies the size of the data to be returned by the read function. if size is not specified the read function return the entire contain of the file. read function returns and empty string when the end of the file is reached
#f.readline()=> read a single line from the file
# Memory efficient example
# f = open('file_name', 'r')
# for line in f:
#     print(line, end="")
#list(f) or f.readlines() => read all the lines in the file
#f.write(content) => writes the contents of content to file and return the number of characters written
#f.tell() return the position of the file object from the beginning of the file
#serializing => convert json object to string
#deserializing => convert string to json object
