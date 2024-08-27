# Multithreading in python - (for parallel task execution)
'''multithreading is a technique in programming that allows 
multiple threads of execution to run concurrently within a
single process in python we can use the 'threading' module
to implement multithreading in this.'''

#creating thread -
'''To create a thread we need to create a thread 
object and then call its 'start()' method runs the
thread and then to stop the execution we use
the 'join()' method.'''


#Example 1 

from concurrent.futures import ThreadPoolExecutor #for bulk tasks
import threading
import time

#indicates same task being done

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter() #to count time required for code execution.

#normal code 
'''func(4)
func(3) #thses normal function execute one after another.
func(1)

time2 = time.perf_counter()
print(time2 - time1) #to find diff before function start and end(8 secs)'''


#same code with multithreading (threads)

t1 = threading.Thread(target=func,args=[4]) #args - input for function
t2 = threading.Thread(target=func , args= [2])
t3 = threading.Thread(target=func, args=[4])

t1.start() #to start thread 1
t2.start() #these function start execution at same time.
t3.start()



t1.join()#to wait until t1 is over
t2.join()#to wait until t2 is over #takes (4 sec) for exec
t3.join()#to wait until t3 is over

#to find time taken for execution(0 seconds)
time2 = time.perf_counter()
print(time2 - time1) 



#thread Pool executor (miscelleneous) #long code
#it helps in bulk task scheduling

def poolingdemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3) #func, args
        future2 = executor.submit(func,2) #func, args
        future3 = executor.submit(func,4) #func, args

        '''print(future1.result())
        print(future2.result()) #executes at same time
        print(future3.result())'''

#poolingdemo()
        
##################################################################
#easier method compared to upper for thread pooling unign (map executor)

        l = [1, 2, 3, 4]
        results = executor.map(func, l) #giving list l as args to func
        for result in results:
            print(result)


poolingdemo()



        