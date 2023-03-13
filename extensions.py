string = input()
index = string.find('.')
string = string[index:]
match string:
    case  ".gif" | ".png" :
        print("image/" + string[1:])
    case ".jpg" | ".jpeg":
        print("image/" + string[1:])
    case ".pdf" | ".zip":
        print("application/" + string[1:])
    case ".txt":
        print("text/plain")
