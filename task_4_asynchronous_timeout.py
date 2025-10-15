import asyncio


async def slow_task():
    """Simulates a slow task that takes 10 seconds to complete."""
    print("Task started...")
    await asyncio.sleep(10)
    print("Task completed!")


async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Timeout! The task took too long to complete.")

# Example usage:
# if __name__ == "__main__":
#     asyncio.run(main())
