class LogSystem:

    def __init__(self):
        self.logs = defaultdict(int)

    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp] = id

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        startDate = list(start)
        endDate = list(end)
        log_ids = []
        remove_last_n_chars = 0
        if granularity == 'Minute':
            startDate = startDate[:-3]
            endDate = endDate[:-3]
            remove_last_n_chars = 3
        elif granularity == 'Hour':
            startDate = startDate[:-6]
            endDate = endDate[:-6]
            remove_last_n_chars = 6
        elif granularity == 'Day':
            startDate = startDate[:-9]
            endDate = endDate[:-9]
            remove_last_n_chars = 9
        elif granularity == 'Month':
            startDate = startDate[:-12]
            endDate = endDate[:-12]
            remove_last_n_chars = 12
        elif granularity == 'Year':
            startDate = startDate[:-15]
            endDate = endDate[:-15]
            remove_last_n_chars = 15
        for timestamp, _id in self.logs.items():
            timestamp_parsed = list(timestamp)[:-remove_last_n_chars] if remove_last_n_chars != 0 else list(timestamp)
            if str(startDate) <= str(timestamp_parsed) <= str(endDate):
                log_ids.append(_id)
        return log_ids
