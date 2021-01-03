from pathlib import Path

"""
Repo of files that uses a flat file list.
The list should have a single file name with relative path on each line.
Provides files as an iterable.
"""
class FlatFileRepo:
    file_list_name = ""
    file_list = []

    def __init__(self, file_list_name):
        self.file_list_name = Path(file_list_name).expanduser()
        if not self.file_list_name.exists():
            raise Exception("Unable to find the file " + str(self.file_list_name))
        else:
            file_object = open(self.file_list_name, "r")

        for line in file_object:
            self.file_list.append(line.rstrip())

        file_object.close()

    def files(self):
        return self.file_list
