# import multiprocessing
# from multiprocessing import Pool
#
#
# def readAndSet():
# 	num = 0
# 	print(multiprocessing.current_process().name + " " + str(num))
# 	# print(multiprocessing.current_process().name)
#
# 	# while num < 5:
# 	# 	print(multiprocessing.current_process().name + " " + str(num))
# 	# 	num = num + 1
#
#
# pool = Pool()
# # for num in range(4):
# # 	pool.apply_async(readAndSet, args=(num,))
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.close()
# pool.join()
# print("程序运行结束")


import multiprocessing

num = 0


def readAndSet():
    global num
    while num < 5:
        print(multiprocessing.current_process().name + " "+str(num))
        num = num + 1

cpus = multiprocessing.cpu_count()
print(cpus)
pool = multiprocessing.Pool(processes = 2)
pool.apply_async(readAndSet)
pool.apply_async(readAndSet)
pool.close()
pool.join()
print("程序运行结束")