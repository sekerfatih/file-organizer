import os, shutil

def organize_files(directory_path):
    """Organize files in the given directory by type"""
    
    file_list = os.listdir(directory_path)
    
    for filename in file_list: 
        name, file_type = os.path.splitext(filename)
       
        if file_type in [".jpg", ".jpeg", ".png"]:
            os.makedirs(directory_path + "/Images", exist_ok=True)
            shutil.move(directory_path + "/" + filename, directory_path + "/Images/")
        
        elif file_type in [".mp4", ".avi", ".mkv"]:
            os.makedirs(directory_path + "/Videos", exist_ok=True)
            shutil.move(directory_path + "/" + filename, directory_path + "/Videos/")

        elif file_type in [".txt", ".docx", ".pdf", ".sh", ".odt", ".env"]:
            os.makedirs(directory_path + "/Files", exist_ok=True)
            shutil.move(directory_path + "/" + filename, directory_path + "/Files/")

# If running this file directly, organize the test folder
if __name__ == "__main__":
    organize_files("/home/fatih/Desktop/test/")