import os

class LibIO:
    def __init__(self):
        self.fd = None
        self.eof_flag = False
        self.error_flag = False

    def fopen(self, filename, mode):
        flags = {
            'r': os.O_RDONLY,
            'w': os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
            'a': os.O_WRONLY | os.O_CREAT | os.O_APPEND,
        }

        try:
            self.fd = os.open(filename, flags[mode])
        except OSError:
            self.error_flag = True
            raise
        return self.fd

    def fread(self, size):
        try:
            data = os.read(self.fd, size)
            if len(data) == 0:
                self.eof_flag = True
            return data
        except OSError:
            self.error_flag = True
            raise

    def fwrite(self, data):
        try:
            return os.write(self.fd, data)
        except OSError:
            self.error_flag = True
            raise

    def fclose(self):
        try:
            os.close(self.fd)
        except OSError:
            self.error_flag = True
            raise

    def feof(self):
        return self.eof_flag

    def ferror(self):
        return self.error_flag
