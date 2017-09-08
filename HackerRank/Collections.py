from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import deque


def counter():
    heights = [170, 170, 169, 152, 170, 169, 158, 188, 142, 168, 171, 158]
    print(Counter(heights))
    print(Counter(heights).items())
    print(Counter(heights).keys())
    print(Counter(heights).values())


def average_mark():
    Student = namedtuple("Student", "MARK, NAME, ID")
    students = [Student(90, "Jake", "J13"), Student(79, "Tony", "T44"), Student(83, "Matt", "M24")]
    average = sum(stud.MARK for stud in students)/len(students)
    print(average)


def dictionary():
    food = OrderedDict()
    food["Milk"] = 1.50
    food["Oats"] = 0.80
    food["Cheese"] = 1.99
    food["Watermelon"] = 5.10
    for item, price in food.items():
        print("{0:10}{1:10}".format(item, price))
    print("Net price is: ", sum(food.values())/len(food))


def double_ended_queue():
    deq = deque()
    deq.append(1)
    deq.pop()
    deq.extendleft('234')
    deq.popleft()
    deq.appendleft(55)
    print(*deq)
