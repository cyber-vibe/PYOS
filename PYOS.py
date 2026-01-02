#Print the os banner
print("""██████╗ ██╗   ██╗ ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔════╝
██████╔╝ ╚████╔╝ ██║   ██║███████╗
██╔═══╝   ╚██╔╝  ██║   ██║╚════██║
██║        ██║   ╚██████╔╝███████║
╚═╝        ╚═╝    ╚═════╝ ╚══════╝""")


while True:
  
  enter = input(">>>")
  if "help" in enter:
     print("""say:x - says x
math - do math
fmake - make file
fread - read file
fdel - delete file
dmake - make dir
dread - read dir
ddel - delete dir
dfile - make a file in a parent dir
ddir - make a subdir in a parent dir
PS: always adding new features!!!
PSS: please support me.
""")
  #print() say
  if "say:" in enter:
    new_text = enter.replace("say:", "")
    print(new_text)
  #math +-*/
  if "math" in enter:
    math = input("type in the math equation ")
    ans = eval(math)
    print(ans)
  #file to create a new file
  if "fmake" in enter:
    name = input("give the file a name: ")
    contentfile = input("give the file contents ")
    globals()[name] = contentfile
  #Fread to read a file 
  if "fread" in enter:
    freadfile = input("name of file to fread: ")
    
    # Check if the variable name exists in the global namespace
    if freadfile in globals():
        print(f"the contents are: {globals()[freadfile]}")
    else:
        # Display the custom error if the variable is not found
        print("error 404 file not found")
  #Fdel
  if "fdel" in enter:
    fdelfile = input("file to delete ")
    globals().pop(fdelfile, None)
  #Directorys
  if "dmake" in enter:
    dir_name = input("name of directory to create: ")
    # Create a new empty dictionary to act as the 'directory'
    globals()[dir_name] = {}
  if "ddel" in enter:
     deldir = input("directory to delete")
     globals().pop(deldir, None)
  # To add a 'file' to your new directory variable
  if "dfile" in enter:
    target_dir = input("Enter directory to put file in: ")
    
    if target_dir in globals() and isinstance(globals()[target_dir], dict):
        file_name = input("Name of file: ")
        file_content = input("Content of file: ")
        
        # FIX: Add the file TO the existing dictionary
        # This keeps 'bob' if it's already there
        globals()[target_dir][file_name] = file_content
        
        print(f"Added {file_name} to {target_dir}.")
    else:
        print("error 404 directory not found")

  # To add a 'subdirectory'
  if "ddir" in enter:
    parent_dir = input("Enter parent directory: ")
    
    # Check if the parent exists and is a dictionary
    if parent_dir in globals() and isinstance(globals()[parent_dir], dict):
        sub_name = input("Name of new subdirectory: ")
        
        # FIX: Add the new empty dictionary TO the parent
        # This uses parent_dir[sub_name] instead of overwriting parent_dir
        globals()[parent_dir][sub_name] = {}
        
        print(f"Subdirectory '{sub_name}' created inside '{parent_dir}'.")
    else:
        print("error 404 parent directory not found")

  if "dread" in enter:
    dread_target = input("Directory to dread (read contents): ")

    # 1. Check if the variable exists and is actually a 'directory' (dictionary)
    if dread_target in globals() and isinstance(globals()[dread_target], dict):
        contents = globals()[dread_target]
        
        if not contents:
            print(f"Directory '{dread_target}' is empty.")
        else:
            print(f"Listing contents of '{dread_target}':")
            # 2. Iterate through keys to display them like files in a folder
            for item in contents.keys():
                # Check if the item is a subdirectory (another dict) or a file (string/data)
                type_label = "[DIR]" if isinstance(contents[item], dict) else "[FILE]"
                print(f"  {type_label} {item}")
    else:
        # 3. Use your custom error if it doesn't exist
        print("error 404 directory not found")

