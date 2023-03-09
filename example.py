# def gen():
#     print(1)
#     yield 1
#     print(2)
#     yield 2
#     print(3)
#
#
# for i in gen():
#     print(i)
#

def gen(max_count):
    count = 1
    while True:
        yield count
        count += 1
        if count > max_count:
            return


for i in gen(10):
    print(i)
