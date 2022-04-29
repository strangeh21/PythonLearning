filename = input("Filename: ").strip().rsplit(".", maxsplit=1)
file_extension = filename[1].lower()


match file_extension:
    case ("jpeg" | "jpg"):
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
