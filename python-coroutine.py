import aiohttp
import asyncio
import datetime
import time
import requests
async def fetch_data(url):
    print(datetime.datetime.now())
    time.sleep(4)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
      'https://jsonplaceholder.typicode.com/posts/1',
      'https://jsonplaceholder.typicode.com/posts/2',
      'https://jsonplaceholder.typicode.com/posts/3'
    ]
    print(datetime.datetime.now())
    time.sleep(2)
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    time.sleep(2)
    print(datetime.datetime.now())
    tasks = [fetch_data(url) for url in urls]

    # Use asyncio.gather to run multiple coroutines concurrently
    results = await asyncio.gather(*tasks)

    # Process the results
    for url, result in zip(urls, results):
        print(f"Data from {url}: {result[:100]}...")

# Run the event loop to execute the main coroutine
asyncio.run(main())
print(datetime.datetime.now())
# import requests
# import datetime
# import time
# def fetch_data(url):
#   print(datetime.datetime.now())
#   time.sleep(2)
#   r = requests.get(url)
#   return r
# def main():
#   urls = [
#     'https://jsonplaceholder.typicode.com/posts/1',
#     'https://jsonplaceholder.typicode.com/posts/2',
#     'https://jsonplaceholder.typicode.com/posts/3'
#   ]

#   tasks = [fetch_data(url) for url in urls]

#   print(tasks)
#   # Process the results
#   # for url, result in zip(urls, tasks):
#   #   print(f"Data from {url}: {result[:100]}...")
    
# main()