# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    #inp = 'add 911 police;add 76213 Mom;add 17239 Bob;find 76213;find 910;find 911;del 910;del 911;find 911;find 76213;add 76213 daddy;find 76213'
    #inp = 'find 3839442;add 123456 me;add 0 granny;find 0;find 123456;del 0;del 0;find 0'
    #return [Query(cmd.split()) for cmd in inp.split(';')]
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = { }
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts.keys():
                del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts.keys():
                response = contacts[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

