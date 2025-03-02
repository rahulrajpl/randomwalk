class content():
    def __init__(self):
        super().__init__()
        self.name = 'Rahul Raj'
        self.place = 'Delhi, India'
        self.tags = 'python, cybersecurity, machinelearning'

    def show(self):
        print(f'Name: {self.name}')
        print(f'place: {self.place}')
        print(f'Tags: {self.tags}')

if __name__ == '__main__':
    obj = content()
    obj.show()
    
