import sys


# def func_exit():
#     print('func exit run')
#     sys.exit(1)
#
#
# def func_base():
#     try:
#         print('func base run')
#         func_exit()
#
#     except:
#         pass
#
#     finally:
#         print('run finally')
#
#
# func_base()


def func_exit_se():
    raise SystemExit(1)


def func_base_se():
    try:
        print('func base_se run')
        func_exit_se()

    except SystemExit:
        print('run system exit')

    finally:
        print('run finally')


func_base_se()


