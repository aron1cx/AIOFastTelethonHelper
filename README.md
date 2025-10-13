# AIOFastTelethonHelper

Asynchronous fork of [FastTelethonhelper](https://github.com/MiyukiKun/FastTelethonHelper)  
Provides fully async and parallel file upload/download functions using `aiofiles` and non-blocking I/O.

## 📦 Installation
```bash
pip install aiofasttelethonhelper
```


## ⚙️ Usage Example
```python
from aiofasttelethonhelper.utils import print_progress_bar
from aiofasttelethonhelper import fast_download, fast_upload
from telethon import TelegramClient

client = TelegramClient("session", API_ID, API_HASH)

def custom_progress_callback(**kwargs):
  done, total = kwargs.get('done'), kwargs.get('total')
  print(f"{done}/{total}")

async def main():
  async with client:
      file_path = await fast_download(
        client=client, 
        message=message, 
        file_path="./downloads", # or ./downloads/file.txt
        progress_callback=print_progress_bar
      )

      file = await fast_upload(
        client=client,
        file_path="input.txt",
        progress_callback=custom_progress_callback
      )
      await client.send_file("me", file)
```

## ❤️ Credits
- Tulir Asokan - Original parallel transfer logic in [mautrix-telegram](https://github.com/mautrix/telegram)
- MiyukiKun - Original [helper](https://github.com/MiyukiKun/FastTelethonhelper) creator
- Lonami - Creator of the amazing [Telethon](https://github.com/LonamiWebs/Telethon) library
