import csv
import pyexcel


class CSVIO:
    @staticmethod
    def read(filepath):
        data = []
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def write(filepath, content):
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(content)


class XLSXIO:
    @staticmethod
    def read(filepath):
        try:
            content = pyexcel.get_array(file_name=filepath)
            return content
        except Exception as e:
            print("Error reading file:", e)

    @staticmethod
    def write(filepath, content):
        try:
            pyexcel.save_as(array=content, dest_file_name=filepath)
            print("File saved successfully")
        except Exception as e:
            print("Error writing file:", e)
