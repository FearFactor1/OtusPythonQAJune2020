a = 1

# # example 1
# def change():
#     a = a + 5
#     print(a)
#
# change()


# # example 2
# def change():
#     global a
#     a = a + 5
#     print(a)
#
# change()
# print("After calling change a =", a)


# # example 3
# def change():
#     a = 10
#
#     def change_inside():
#         # nonlocal a - ?
#         # global a - ?
#         a = a + 5
#
#     print("before inside a =", a)
#
#     change_inside()
#
#     print("after inside a =", a)
#
# change()
#
# print("outside a =", a)
