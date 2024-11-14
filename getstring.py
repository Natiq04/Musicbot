import asyncio
from aylak import get_keys
from pyrogram import Client

API_HASH, API_ID = get_keys()

print("\n\n Enter Phone number when asked.\n\n")

i = Client("vipstring", in_memory=True, api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"HERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n\n`{ss}`\n\n STRING GENERATED"
    await i.send_message("me", xx)
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
    print("\n STRING GENERATED\n")


asyncio.run(main())
