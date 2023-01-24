import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂")


@Client.on_message(filters.command("requst", CMD))
async def check_alive(_, message):
    await message.reply_text("<b>🍂SEᑎᗪ ᗰOᐯIE ᑎᗩᗰE ᗰE🍂 \n\nനിങ്ങൾക്ക് വേണ്ട മൂവി നെയിം എനിക്ക് അയച്ച് തരിക \n\n🍃SEᑎᗪ ᑕOᖇᖇEᑕT GOOGᒪE SᑭEᒪᒪIᑎG🍃</b>")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
