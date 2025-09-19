import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message
    

'''
What is @staticmethod?
Indicates this method does not depend on the instance (self) or the class (cls).
Can be called as: CustomException.get_detailed_error_message(...) or from within the class without an instance.
Why static?
The method only processes input parameters (message, error_detail), and reads info from sys.exc_info(). It does not use any attributes of the exception instance.
This makes the method reusable and clear—no instance data required.
What does it do?
Uses sys.exc_info() to get current traceback info.
Returns a tuple: (type, value, traceback)
Only exc_tb (traceback) is used here.
Extracts the filename and line number from the traceback, if available.
Builds a string containing:
The passed message
The error detail
The filename
The line where the exception occurred
5. String Representation (__str__)
Python
def __str__(self):
    return self.error_message
When the exception is printed (e.g., print(e)), this method is called.
Returns the detailed error message constructed earlier.
Flow of the Code:
Raise Exception

When an error occurs in your code, you can raise CustomException with a message and optional error detail.
Example:
Python
raise CustomException("Something went wrong", error_detail=e)
Exception Handling

The __init__ method builds a detailed error message using the static method and stores it.
The static method pulls traceback info from the current exception context.
When the exception is printed or logged, __str__ returns the detailed message.
Why use @staticmethod here?
The method does not depend on instance attributes (self) or class attributes (cls).
It operates only on its input parameters and some global state (sys.exc_info()).
Using @staticmethod makes it clear that:
No instance or class context is required.
It can be reused independently.

'''