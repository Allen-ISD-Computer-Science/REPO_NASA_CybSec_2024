import os
import subprocess
import asyncio

async def main():
    
    cmdInstall = ["sudo", "dnf", "install", "netcat", "ufw"]
    cmdAllowIncoming = ["sudo", "ufw", "default", "allow", "incoming"]
    cmdAllowOutgoing = ["sudo", "ufw", "default", "allow", "outgoing"]
    cmdOpenPort6900 = ["sudo", "ufw", "allow", "6900/udp"]
    cmdOpenPort4200 = ["sudo", "ufw", "allow", "4200/udp"]

    if await prompt_user("Do you want to install the package? (y/n): "):
        try:
            subprocess.run(cmdInstall, check=True)
            print(f"{cmdInstall} - Installation is all good")

            if await prompt_user("Do you want to allow incoming connections? (yes/no): "):
                subprocess.run(cmdAllowIncoming, check=True)
                print(f"{cmdAllowIncoming} - Is all good")

            if await prompt_user("Do you want to allow outgoing connections? (yes/no): "):
                subprocess.run(cmdAllowOutgoing, check=True)
                print(f"{cmdAllowOutgoing} - Is all good")

            if await prompt_user("Do you want to open port 6900/udp? (yes/no): "):
                subprocess.run(cmdOpenPort6900, check=True)
                print(f"{cmdOpenPort6900} - Is all good")

            if await prompt_user("Do you want to open port 4200/udp? (yes/no): "):
                subprocess.run(cmdOpenPort4200, check=True)
                print(f"{cmdOpenPort4200} - Is all good")
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")
            print("Installation canceled.")
    else:
        print("Installation canceled.")
    exiting = False
    ip = input("what is the IP of the other device: ")
    cmdReceive = [""]
    cmdSend = [""]
    while exiting == False:


async def file_checksum(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    cmd = ["md5sum", path]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    if proc.returncode != 0:
        raise Exception(f"Command failed: {stderr.decode()}")

    hash_value = stdout.decode().strip().split()[0]
    return hash_value

async def did_file_change(path):
    hash_func = asyncio.create_task(file_checksum(path))
    return_hash = await hash_func
    is_same = True
    new_hash = ""

    while is_same:
        new_hash_func = asyncio.create_task(file_checksum(path))
        new_return_hash = await new_hash_func
        await asyncio.sleep(1)

        if new_return_hash != return_hash:
            is_same = False
            new_hash = new_return_hash

    return f"{return_hash} {new_hash}"

async def prompt_user(message="Do you want to proceed? (yes/no): "):
    user_input = input(message).lower()
    return user_input == "y"

asyncio.run(main())
