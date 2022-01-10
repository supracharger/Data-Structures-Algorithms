# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def OpenTime(self, time):
        if len(self.finish_time) == 0:
            return time
        return max(time, self.finish_time[-1])

    def Add(self, time, elapsed):
        self.finish_time.append(time + elapsed)

    def process(self, request):
        # write your code here
        return Response(False, -1)


def process_requests(requests, buffer):
    responses = [ ]
    for i,(arrived_at, time_to_process) in enumerate(requests):
        while len(buffer.finish_time)>0 and buffer.finish_time[0]<=arrived_at:
            del buffer.finish_time[0]
        if len(buffer.finish_time) < buffer.size:
            start_at = buffer.OpenTime(arrived_at)
            buffer.Add(start_at, time_to_process)
            responses.append(start_at)
        else: responses.append(-1)
    return responses

def process_requests_old(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append((arrived_at, time_to_process))

    #buffer_size, requests = 1, []
    #buffer_size, requests = 1, [(0,0)]
    #buffer_size, requests = 1, [(0,1), (0,1)]
    #buffer_size, requests = 1, [(0,1), (1,1)]
    #n_requests = len(requests)

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response)
        #print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
