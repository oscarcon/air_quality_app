import threading 

def first_thread():
    print("First thread", threading.local().x)
def second_thread():
    print("Second thread")

thread_local = threading.local()
thread_local.x = 10

threading.Thread(target=first_thread).start()