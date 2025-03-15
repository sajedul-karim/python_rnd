import asyncio
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

async def brew_coffee(time_to_brew: int = 4) -> None:
    """Simulate brewing coffee with logging"""
    start_time = time.perf_counter()
    logging.info(f"Brewing coffee started with time to brew: {time_to_brew} seconds")
    
    # Simulate brewing time
    await asyncio.sleep(time_to_brew)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    logging.info(f"Brewing coffee completed in {duration:.2f} seconds")

async def prepare_bagel(time_to_prepare: int = 2) -> None:
    """Simulate preparing a bagel with logging"""
    start_time = time.perf_counter()
    logging.info(f"Preparing bagel started with time to prepare: {time_to_prepare} seconds")
    
    # Simulate preparation time
    await asyncio.sleep(time_to_prepare)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    logging.info(f"Preparing bagel completed in {duration:.2f} seconds")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(
        brew_coffee(),
        prepare_bagel()
    )

if __name__ == "__main__":
    # python src/async_await.py
    asyncio.run(main())
