class MyObj:

    def __getitem__(self, item):
        return ''

    def __call__(self, *args, **kwargs):
        print(args)
        pass

    pass


obj = MyObj()
print(obj[0])
