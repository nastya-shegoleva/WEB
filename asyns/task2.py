import asyncio
import time


async def task(name, task_num, prep_time, defense_time):
    print(f"{name} started the {task_num} task.")
    await asyncio.sleep(prep_time / 100)
    print(f"{name} moved on to the defense of the {task_num} task.")
    await asyncio.sleep(defense_time / 100)
    print(f"{name} completed the {task_num} task.")


async def interviews(*applicants):
    tasks = []
    for name, prep_time1, defense_time1, prep_time2, defense_time2 in applicants:
        task1 = task(name, 1, prep_time1, defense_time1)
        tasks.append(task1)
        await asyncio.gather(task1)
        print(f"{name} is resting.")
        await asyncio.sleep(5)
        task2 = task(name, 2, prep_time2, defense_time2)
        tasks.append(task2)
        await asyncio.gather(task2)

    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)
