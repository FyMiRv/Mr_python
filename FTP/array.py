from multiprocessing import Process,Array

# 创建共享内存
# shm = Array('i',[1,2,3])
# shm = Array('i',3)  # 表示开辟三个空间的列表
shm = Array('c',b"hello") #字节串

def fun():
  # 共享内存对象可迭代
  for i in shm:
    print(i)
  shm[0] = b'H'

p = Process(target = fun)
p.start()
p.join()

for i in shm:
  print(i)

print(shm.value) # 打印字节串