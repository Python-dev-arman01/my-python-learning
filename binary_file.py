# work on binary files
with open("mymovie.dat", "wb") as file:
   file.write(b"Hello Binary World\n")
    text_data = "This is english syntax"
    file.write(text_data.encode('utf-8')) 
print("Congratulation your binary file creat sucssesfully!")
with open("mymovie.dat", "rb") as file:
    content = file.read()
    
    print("Raw Bytes Data:", content)
    print("---")
    print("Decoded Text:\n", content.decode('utf-8'))

