def main():
    file = input("Enter filename: ").strip().lower()
    mime_type = get_mime_type(file)
    print(mime_type)

def get_mime_type(filename):
    mime_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Extract file extension
    for ext, mime in mime_types.items():
        if filename.endswith(ext):
            return mime
    return "application/octet-stream"

main()