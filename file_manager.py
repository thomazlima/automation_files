import os
import datetime

class Disk():
    def __init__(self, location):
        self._location = location
        self._name = self._name = location.split('/')[-1]

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def last_modified_date(self):
        last_modified_date = os.stat(self._location).st_mtime
        last_modified_date = datetime.datetime.fromtimestamp(last_modified_date)      
        return last_modified_date
    

class Folder(Disk):
    def __init__(self, location):
        super().__init__(location)
        self._number_of_files = len(os.listdir(self._location))
    
    def __str__(self):
        return 'Directory info: \n Name: {} \n Nr. File(s): {} \n Location: {}'.format(self._name, self._number_of_files, self._location)

    def list_of_files(self):
        return os.listdir(self._location)

class File(Disk):
    def __init__(self, location):
        super().__init__(location)
        self._extension = os.path.splitext(location)[1] 

    @property
    def extension(self):
        return self._extension
