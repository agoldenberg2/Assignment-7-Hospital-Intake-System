class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"Patient({self.name}, {self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        minimum = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return minimum

    def heapify_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def peek(self):
        return self.data[0] if self.data else None

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    patients = [
        Patient("Alice", 5),
        Patient("Bob", 1),
        Patient("Charlie", 3),
        Patient("Dana", 1),
    ]

    for patient in patients:
        heap.insert(patient)

    print(heap.peek())
    print(heap.remove_min())
    print(heap.remove_min())
    print(heap.is_empty())

    empty_heap = MinHeap()
    print(empty_heap.remove_min())
