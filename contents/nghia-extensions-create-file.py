import os

def create_file(folder_path):
    for i in range(START, END):
        file_name = f"KhoaHoc{i}.txt"
        file_path = os.path.join(folder_path, file_name)
        
        


        

        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(f"This is file {file_name}")
            
            
            




        print(f"Created file: {file_path}")

folder_path = r"input-nghia-extensions-create-file"








START = 1
END = 100 









if not os.path.exists(folder_path):
    print(f"Không có thư mục {folder_path}")
    # os.mkdir(folder_path)


create_file(folder_path)
