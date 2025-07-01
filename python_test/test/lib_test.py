import sys
import os
import pytest

# Add project root to sys.path so that we can import from the 'app' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.os_lib import LibIO

# Name of the temporary test file
TEST_FILE = "test_io_temp.txt"

class TestLibIO:

    """
        Setup method run before each test.
        Ensures any pre-existing test file is removed to avoid test contamination.
    """
    def setup_method(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
    
    """
        Teardown method run after each test.
        Cleans up the test file created during the test execution.
    """
    def teardown_method(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)


    def test_write_read(self):
        lib = LibIO()
        data = b"Hello Test"

        # Write data to file
        lib.fopen(TEST_FILE, 'w')
        written = lib.fwrite(data)
        assert written == len(data)
        lib.fclose()

        # Read data back from file
        lib.fopen(TEST_FILE, 'r')
        read_back = lib.fread(100)
        lib.fclose()

        assert read_back == data
        assert not lib.ferror()        
        print("Verified fread() and fwrite() implementation passed. No ferror triggered.")

    def test_open_nonexistent_file(self):
        lib = LibIO()
        with pytest.raises(OSError):
            lib.fopen("no_such_file_123.txt", 'r')
        assert lib.ferror()
        print("Verified fopen() with nonexistent file correctly triggered ferror.")

    def test_feof_behavior(self):
        lib = LibIO()
        # Write fixed data to file manually
        with open(TEST_FILE, 'wb') as f:
            f.write(b"abc")
        
        # Read full data
        lib.fopen(TEST_FILE, 'r')
        data = lib.fread(3)
        assert data == b"abc"
        assert not lib.feof()
        
        # Try to read beyond EOF
        leftover = lib.fread(1)
        assert leftover == b""  
        assert lib.feof()
        lib.fclose()
        print("Verified feof() behavior correctly detected end-of-file.")