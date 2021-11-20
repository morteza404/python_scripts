import statsd
import asyncio
import subprocess

c = statsd.StatsClient("localhost", port=8125, prefix="swift_test")

async def func():
    for _ in range(100):
        cmd = subprocess.check_output(["sh","-c","ps -aux | wc -l"], stderr=subprocess.STDOUT)
        c.timing("ps", float(cmd.decode("utf-8")))        
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(func())
    print("ok")