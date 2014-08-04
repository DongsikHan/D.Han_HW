class Database(object):
    def __init__(self):
        self.database = [

        ]
    
    def maxid(self):
        _id = -1
        for item in self.database:
            if 'id' in item and _id < item['id']:
                _id = item['id']
        return _id

    def newid(self):
        return self.maxid() + 1

    def put(self, storage):
        self.database.append(storage)

    def select(self, _id):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id: # string 
                return value
 
    def update(self, _id, item):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id: # string 
                self.database[key] = item
                break

    def delete(self, _id):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id: # string 
                self.database.pop(key)
                break

    def out(self):
        return self.database

    def get_entries_10(self):
        return self.database[:10]

    def maxlike_3(self):
        arr = self.database
        for i in range(0, len(arr)):
            check = arr[i]
            for j in range(i+1, len(arr)):
                if check['likecount'] < arr[j]['likecount']:
                    temp = arr[j]
                    arr[j] = check
                    check = temp
            arr[i] = check       
        arr_3=arr[:3]
        return arr_3
















