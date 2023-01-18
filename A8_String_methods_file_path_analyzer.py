# A8-String methods - file path analyzer
path = input("Input path: ")
if len(path) > 0:
    windows_path_split = path.split("\\")
    linux_path_split = path.split("/")
    path_type = ""
    if path[0].isupper() and path[1:3] == ":\\" and windows_path_split[-1].count(".") == 1:
        path_type = "Windows"
    if path[0] == "/" and linux_path_split[-1].count(".") == 1:
        path_type = "Linux"
    if path_type != "Linux" and path_type != "Windows":
        print("Invalid path.")
    elif path_type == "Windows":
        print(f"The depth of the path: {len(windows_path_split)-1}")
        file = windows_path_split[-1].split(".")
        print(f"The filename: {file[0]}")
        print(f"The file's extension: {file[-1]}")
    else:
        print(f"The depth of the path: {len(linux_path_split)-2}")
        file = linux_path_split[-1].split(".")
        print(f"The filename: {file[0]}")
        print(f"The file's extension: {file[-1]}")
else:
    print("Invalid input, Please write SOMETHING.")

