import asyncio


def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

async def task_func1(task2: bool | None=None, task4: bool | None=None):
    await asyncio.sleep(1)
    print(f"Executed task1 with task2 result {task2} and task4 result {task4}")
    return True

async def task_func2(task3: bool | None=None, task6: bool | None=None):
    await asyncio.sleep(1)
    print(f"Executed task2 with task3 result {task3} and task6 result {task6}")
    return True

def task_func3(task5: bool | None=None) -> int:
    result = fib(10)
    print(f"Task 3: calculated fib(30) with task5 result {task5}")
    return result

# async def task_func3(task5: bool | None=None):
#     await asyncio.sleep(1)
#     print(f"Executed task3 with task5 result {task5}")
#     return True


async def task_func4(task5: bool | None=None):
    await asyncio.sleep(3)    
    print(f'Executed task4 with task5 result {task5}')
    return True

async def task_func5():
    await asyncio.sleep(5)    
    print('Executed task5')
    return True

async def task_func6(task7: bool | None=None):
    await asyncio.sleep(3)    
    print(f'Executed task6 with task7 result {task7}')
    return True

async def task_func7(): 
    await asyncio.sleep(10)   
    print("Executed task7")
    return True
    # await asyncio.sleep(2)
    # raise Exception("Task 7 failed with exception")