class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return ["banana", "mango", "apple", "watermelon"]

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True


with HelloContextManager() as fruits:
    print(fruits)
    print(fruits[100])


class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()


with WritableFile("hello.txt") as file:
    file.write("Hello, World!")
