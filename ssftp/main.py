import os
import subprocess
import asyncio

async def main():

    host = str(input("What is the IP of the other PI: "))
#Checksum
async def fileChecksum(path):
    cmd = ["md5sum", path]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        raise Exception(f"Command failed: {stderr.decode()}")
    hashValue = stdout.decode().strip().split()[0]
    return hashValue
#Check if the file has been updated
async def didFileChange(path):
    hashFunc = asyncio.create_task(fileChecksum(path))
    returnHash = await hashFunc
    isSame = True
    newHASH = ""
    while isSame:
        newHashFunc = asyncio.create_task(fileChecksum(path))
        newReturnHash = await newHashFunc  # Use await here
        await asyncio.sleep(1)
        if newReturnHash != returnHash:
            isSame = False
            newHASH = newReturnHash  # Assign the new hash value
    return f"{returnHash} {newHASH}"
#Initializes the UFW settings
async def Initializer():
    cmd = ["sudo","ufw"]
asyncio.run(main())
