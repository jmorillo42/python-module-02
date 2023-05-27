import csv


class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        # ... Your code here ...
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.__data = None
        self.__header = None
        self.__file = None

    def __enter__(self):
        # ... Your code here ...
        try:
            self.__file = open(self.filename, 'r')
        except FileNotFoundError:
            return None
        self.__lines = len(self.__file.readlines())
        self.__file.seek(0)
        self.__reader = csv.reader(self.__file, delimiter=self.sep, strict=True, quoting=csv.QUOTE_ALL,
                                   skipinitialspace=True)
        if self.header:
            self.__header = next(self.__reader)
        self.__data = []
        for i, line in enumerate(self.__reader, 1):
            if self.skip_top < i <= self.__lines - self.skip_bottom:
                if any(field in ('', None) for field in line):
                    return None
                self.__data.append(line)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # ... Your code here ...
        if self.__file:
            self.__file.close()
        # if isinstance(exc_val, IndexError):
        #   Handle IndexError here...
        #   print(f"An exception occurred in your with block: {exc_type}")
        #   print(f"Exception message: {exc_val}")
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return: nested list(list(list, list, ...)) representing the data.
        """
        # ... Your code here ...
        return self.__data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        # ... Your code here ...
        return self.__header
