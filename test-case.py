class DataTransformer:
    def __init__(self, fp):
        self.fp = fp

    def save(self, data):
        data = ''.join([chr(ord(char) + 1) for char in data])  # Caesar cipher
        with open(self.fp, 'w') as f:
            f.write(data)

    def load(self):
        with open(self.fp, 'r') as f:
            data = f.read()
        data = ''.join([chr(ord(char) - 1) for char in data])  # Caesar cipher
        return data

    def print(self):
        with open(self.fp, 'r') as f:
            print(f.read())

# Example usage
dt = DataTransformer('test.txt')
dt.save('GdkknVnqkc ')
print(dt.load())
dt.print()