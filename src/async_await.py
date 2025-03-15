import asyncio
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

async def brew_coffee() -> None:
    """Simulate brewing coffee with logging"""
    start_time = time.perf_counter()
    logging.info("Brewing coffee started")
    
    # Simulate brewing time
    await asyncio.sleep(4)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    logging.info(f"Brewing coffee completed in {duration:.2f} seconds")

async def prepare_bagel() -> None:
    """Simulate preparing a bagel with logging"""
    start_time = time.perf_counter()
    logging.info("Preparing bagel started")
    
    # Simulate preparation time
    await asyncio.sleep(2)
    
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
    asyncio.run(main())
