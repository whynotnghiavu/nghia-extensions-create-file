import os

def create_folder(folder_path):
    for i in range(START, END):
        subfolder_name = f"KhoaHoc{i}"
        subfolder_path = os.path.join(folder_path, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)  
        print(f"Created folder: {subfolder_path}")

folder_path = r"input-nghia-extensions-create-file"








START = 1
END = 100 









if not os.path.exists(folder_path):
    print(f"Không có thư mục {folder_path}")
    # os.mkdir(folder_path)


create_folder(folder_path)
