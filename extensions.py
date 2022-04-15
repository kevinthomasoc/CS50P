name = input("Enter file name:")
name = name.lower()
if (".gif" in name) == True:
    print("image/gif")
elif (".jpg" in name) == True or (".jpeg" in name) == True:
    print("image/jpeg")
elif (".png" in name) == True:
    print("image/png")
elif (".pdf" in name) == True:
    print("application/pdf")
elif (".txt" in name)== True:
    print("text/plain")
elif (".zip" in name)== True:
    print("application/zip")
else:
    print("application/octet-stream")
