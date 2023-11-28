# import requests

# #need to create an endpoint (api) what you'll work with it.
# #forexample:
# PIXELA_ENDPOINT = "https://catfact.ninja/fact"

# #need to create a parameters(dict) what you will give to get a request
# #IMPORTANT! You must to read the api documentation


# response = requests.get(url=PIXELA_ENDPOINT)
# #if you could, create a json format, or text
# response.json()
# print(response)
# print(response.text)
import asyncio
import aiohttp

async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def main():
    url = "https://catfact.ninja/fact"
    print("start")
    result = await make_request(url)
    print("between")
    print(result)
    print("end")

# Run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())