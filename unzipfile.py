import zipfile
import os


def un_zip_files(path, des_folder_path):
    # path = 'D:\\docker\\test folder'
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
    un_zip_files('D:\\docker\\test folder', '')


if __name__ == "__main__":
    main()
