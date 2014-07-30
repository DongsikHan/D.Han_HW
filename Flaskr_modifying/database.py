class Database(object):
    def __init__(self):
        self.database = [

        {
            'title':"",
            'content':"",
            'time':""
        }]
        
    def put(self, storage):
        self.database.append(storage)

    def out(self):
        return self.database

    def get_entries_10(self):
        return self.database[:10]