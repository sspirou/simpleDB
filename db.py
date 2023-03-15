class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, schema):
        self.tables[name] = Table(schema)
    
    def get_table(self, name):
        return self.tables[name]
    
    def remove_table(self, name):
        self.tables.pop(name, None)

class Table:
    def __init__(self, schema):
        self.keys = list(schema.keys())
        self.types = list(schema.values())
        self.rows = []
    
    def insert_row(self, row):
        for i in range(len(row)):
            val = list(row.values())[i]
            if self.types[i] == 'string' and len(val) > 20:
                return -1
            if self.types[i] == 'integer' and (val < -1024 or val > 1023):
                return -1
        self.rows.append(row)
    
    def get_rows(self, condition):
        result = []
        key = list(condition.keys())[0]
        val = list(condition.values())[0]
        for r in self.rows:
            if r[key] == val:
                result.append(r)
        return result

    def print_table(self):
        print(self.keys)
        for r in self.rows:
            print(list(r.values()))


####### Test Code

SQL = Database()
SQL.create_table('people', {'name': 'string', 'age': 'integer'})
table = SQL.get_table('people')
p1 = {'name': 'strat', 'age': 27}
table.insert_row(p1)
p2 = {'name': 'cat', 'age': 23}
table.insert_row(p2)

print(table.get_rows({'age': 27}))

table.print_table()