class CircularBuffer(object):

    def __init__(self, max_size=10):
        """Инициализация класса циклического буфера с дефолтным размером 10"""
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
        """Отформатированная строка содержимого буфера"""
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'

    def size(self):
        """Актуальный размер буфера"""
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        """Если начало буфера совпадает с его концом то возвращает значение True"""
        return self.tail == self.head

    def is_full(self):
        """Возвращает True если конец буфера стоит на 1 пункт перед его началом"""
        return self.tail == (self.head-1) % self.max_size

    def enqueue(self, item):
        """Добавляет значение в конец буфера"""
        if self.is_full():
            raise OverflowError(
                "CircularBuffer is full, unable to enqueue item")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def front(self):
        """Возвращает значение, стоящее в начале буфера."""
        return self.buffer[self.head]

    def dequeue(self):
        """Возвращает значение в начале буфера и удаляет его"""
        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item
