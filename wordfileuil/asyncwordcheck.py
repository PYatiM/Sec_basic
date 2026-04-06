import asyncio

async def check_target(word, port=80):
    try:
        reader, writer = await asyncio.open_connection(word, port)
        print(f"[+] {word}:{port} is reachable")
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def main(input_file):
    tasks = []
    with open(input_file, 'r') as f:
        for line in f:
            word = line.strip()
            tasks.append(check_target(word))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main("targets.txt"))