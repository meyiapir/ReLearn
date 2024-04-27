import csv


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
