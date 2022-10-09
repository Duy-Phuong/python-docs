import zipfile
import os


def un_zip_files(path, des_folder_path):
    # path = 'F:\\programing\\language\\react\\react-docs\\Source\\The Complete React Developer Course (w Hooks and Redux)\\16. Firebase Authentication'
    files = os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            file_path = path + '/' + file
            print(file_path)
            zip_file = zipfile.ZipFile(file_path)
            for names in zip_file.namelist():
                zip_file.extract(names, path)
            zip_file.close()
    print('unzip file successfully!')


def main():
    path = 'F:\\programing\\language\\react\\react-docs\\Source\\The Complete React Developer Course (w Hooks and Redux)\\16. Firebase Authentication'
    un_zip_files(path, '')


if __name__ == "__main__":
    main()
