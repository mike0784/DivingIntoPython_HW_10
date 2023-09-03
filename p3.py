import json
import os

class parsingDir:
    result = list()
    def __init__(self, dir: str, file: str):
        self.dir = dir
        self.file = file

    def listDirectories(self) -> None:
        os.chdir(dir)
        content = os.listdir()
        for obj in content:
            if os.path.isfile(obj):
                size = os.path.getsize(obj)
                temp = {"file": obj, "parent": dir, "type": "file", "size": size}
                self.result.append(temp)
            if os.path.isdir(obj):
                size = os.path.getsize(obj)
                temp = {"file": obj, "parent": dir, "type": "directories", "size": size}
                self.result.append(temp)
                self.listDirectories(obj)
        os.chdir("..")

    def writeToJSON(self) -> None:
        with open(self.file, "w") as f:
            json.dump(self.result, f)
        print(f'Результаты сохранены в файл: {self.file}')

if __name__ == "__main__":
    file = os.getcwd() + "\\Result.json"
    obj = parsingDir("i:\\DOS", file)
    obj.listDirectories()
    obj.writeToJSON()