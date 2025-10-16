import asyncio


async def producer(queue: asyncio.Queue):
    """Produces 5 tasks and puts them into the queue with a 1 second delay between each."""
    for i in range(1, 6):
        await asyncio.sleep(1)
        task = f"Task-{i}"
        await queue.put(task)
        print(f"Produced: {task}")
    # Optionally, put None for each consumer to signal completion


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """Consumes tasks from the queue, simulating work with a 2 second delay."""
    while True:
        task = await queue.get()
        if task is None:
            queue.task_done()
            print(f"Consumer {consumer_id} exiting.")
            break
        print(f"Consumer {consumer_id} processing {task}")
        await asyncio.sleep(2)
        print(f"Consumer {consumer_id} finished {task}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    num_consumers = 2
    consumers = [consumer(queue, i + 1) for i in range(num_consumers)]
    producer_task = asyncio.create_task(producer(queue))
    consumer_tasks = [asyncio.create_task(c) for c in consumers]

    await producer_task
    # Signal consumers to exit
    for _ in range(num_consumers):
        await queue.put(None)
    await queue.join()
    await asyncio.gather(*consumer_tasks)

# Example usage:
# if __name__ == "__main__":
#     asyncio.run(main())
