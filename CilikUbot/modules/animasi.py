import asyncio
from time import sleep

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP
from CilikUbot.utils import edit_or_reply, cilik_cmd


@cilik_cmd(pattern="alive(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(24)
    event = await edit_or_reply(event, "Y")
    animation_chars = [
        "**Y**",
        "**Ya**",
        "**Yan**",
        "**Yanto**",
        "**YantoUbot**",
        "**YantoUboπ**",
        "**YantoUbπππ**",
        "**YantoUππππ**",
        "**Yantoπππππ**",
        "**Yantππππππ**",
        "**Yanπππππππ**",
        "**Yaππππππππ**",
        "**Yπππππππππ**",
        "ππππππππππ",
        "πππππππππ",
        "ππππππππ",
        "πππππππ",
        "ππππππ",
        "πππππ",
        "ππππ",
        "πππ",
        "ππ",
        "π",
        "**YantoUbot is Alive Masseh Angjay πΏ**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 24])


@cilik_cmd(pattern="bulan$")
async def _(event):
    event = await edit_or_reply(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@cilik_cmd(pattern="sayang$")
async def _(event):
    e = await edit_or_reply(event, "I LOVEE YOUUU π")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("SAYANG KAMU πππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA π")
    await e.edit("ππππ")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("SAYANG KAMUπ")


@cilik_cmd(pattern="dino(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`π                        π¦`")
    await typew.edit("`π                       π¦`")
    await typew.edit("`π                      π¦`")
    await typew.edit("`π                     π¦`")
    await typew.edit("`π   `LARII`          π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`πWOARGH!   π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                    π¦`")
    await typew.edit("`π                     π¦`")
    await typew.edit("`π  Huh-Huh           π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`π          π¦`")
    await typew.edit("`π         π¦`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`π       π¦`")
    await typew.edit("`π      π¦`")
    await typew.edit("`π     π¦`")
    await typew.edit("`π    π¦`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`π§π¦`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@cilik_cmd(pattern="gabut$")
async def _(event):
    e = await edit_or_reply(event, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("ππππ")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("ππππ")
    await e.edit("π’                       πΆ")
    await e.edit("π’                      πΆ")
    await e.edit("π’                     πΆ")
    await e.edit("π’                    πΆ")
    await e.edit("π’                   πΆ")
    await e.edit("π’                  πΆ")
    await e.edit("π’                 πΆ")
    await e.edit("π’                πΆ")
    await e.edit("π’               πΆ")
    await e.edit("π’              πΆ")
    await e.edit("π’             πΆ")
    await e.edit("π’            πΆ")
    await e.edit("π’           πΆ")
    await e.edit("π’          πΆ")
    await e.edit("π’         πΆ")
    await e.edit("π’        πΆ")
    await e.edit("π’       πΆ")
    await e.edit("π’      πΆ")
    await e.edit("π’     πΆ")
    await e.edit("π’    πΆ")
    await e.edit("π’   πΆ")
    await e.edit("π’  πΆ")
    await e.edit("π’ πΆ")
    await e.edit("π’πΆ")
    await e.edit("πΆπ’")
    await e.edit("πΆ π’")
    await e.edit("πΆ  π’")
    await e.edit("πΆ   π’")
    await e.edit("πΆ    π’")
    await e.edit("πΆ     π’")
    await e.edit("πΆ      π’")
    await e.edit("πΆ       π’")
    await e.edit("πΆ        π’")
    await e.edit("πΆ         π’")
    await e.edit("πΆ          π’")
    await e.edit("πΆ           π’")
    await e.edit("πΆ            π’")
    await e.edit("πΆ             π’")
    await e.edit("πΆ              π’")
    await e.edit("πΆ               π’")
    await e.edit("πΆ                π’")
    await e.edit("πΆ                 π’")
    await e.edit("πΆ                  π’")
    await e.edit("πΆ                   π’")
    await e.edit("πΆ                    π’")
    await e.edit("πΆ                     π’")
    await e.edit("πΆ                      π’")
    await e.edit("πΆ                       π’")
    await e.edit("πΆ                        π’")
    await e.edit("πΆ                         π’")
    await e.edit("πΆ                          π’")
    await e.edit("πΆ                           π’")
    await e.edit("πΆ                            π’")
    await e.edit("πΆ                             π’")
    await e.edit("πΆ                              π’")
    await e.edit("πΆ                               π’")
    await e.edit("πΆ                                π’")
    await e.edit("πΆ                                 π’")
    await e.edit("`AHHH MANTAP`")
    await e.edit("π")
    await e.edit("π")
    await e.edit("π")
    await e.edit("π")
    await e.edit("π")
    await e.edit("π")
    await e.edit("π’                       πΆ")
    await e.edit("π’                      πΆ")
    await e.edit("π’                     πΆ")
    await e.edit("π’                    πΆ")
    await e.edit("π’                   πΆ")
    await e.edit("π’                  πΆ")
    await e.edit("π’                 πΆ")
    await e.edit("π’                πΆ")
    await e.edit("π’               πΆ")
    await e.edit("π’              πΆ")
    await e.edit("π’             πΆ")
    await e.edit("π’            πΆ")
    await e.edit("π’           πΆ")
    await e.edit("π’          πΆ")
    await e.edit("π’         πΆ")
    await e.edit("π’        πΆ")
    await e.edit("π’       πΆ")
    await e.edit("π’      πΆ")
    await e.edit("π’     πΆ")
    await e.edit("π’    πΆ")
    await e.edit("π’   πΆ")
    await e.edit("π’  πΆ")
    await e.edit("π’ πΆ")
    await e.edit("π’πΆ")
    await e.edit("πΆπ’")
    await e.edit("πΆ π’")
    await e.edit("πΆ  π’")
    await e.edit("πΆ   π’")
    await e.edit("πΆ    π’")
    await e.edit("πΆ     π’")
    await e.edit("πΆ      π’")
    await e.edit("πΆ       π’")
    await e.edit("πΆ        π’")
    await e.edit("πΆ         π’")
    await e.edit("πΆ          π’")
    await e.edit("πΆ           π’")
    await e.edit("πΆ            π’")
    await e.edit("πΆ             π’")
    await e.edit("πΆ              π’")
    await e.edit("πΆ               π’")
    await e.edit("πΆ                π’")
    await e.edit("πΆ                 π’")
    await e.edit("πΆ                  π’")
    await e.edit("πΆ                   π’")
    await e.edit("πΆ                    π’")
    await e.edit("πΆ                     π’")
    await e.edit("πΆ                      π’")
    await e.edit("πΆ                       π’")
    await e.edit("πΆ                        π’")
    await e.edit("πΆ                         π’")
    await e.edit("πΆ                          π’")
    await e.edit("πΆ                           π’")
    await e.edit("πΆ                            π’")
    await e.edit("πΆ                             π’")
    await e.edit("πΆ                              π’")
    await e.edit("πΆ                               π’")
    await e.edit("πΆ                                π’")
    await e.edit("π’                       πΆ")
    await e.edit("π’                      πΆ")
    await e.edit("π’                     πΆ")
    await e.edit("π’                    πΆ")
    await e.edit("π’                   πΆ")
    await e.edit("π’                  πΆ")
    await e.edit("π’                 πΆ")
    await e.edit("π’                πΆ")
    await e.edit("π’               πΆ")
    await e.edit("π’              πΆ")
    await e.edit("π’             πΆ")
    await e.edit("π’            πΆ")
    await e.edit("π’           πΆ")
    await e.edit("π’          πΆ")
    await e.edit("π’         πΆ")
    await e.edit("π’        πΆ")
    await e.edit("π’       πΆ")
    await e.edit("π’      πΆ")
    await e.edit("π’     πΆ")
    await e.edit("π’    πΆ")
    await e.edit("π’   πΆ")
    await e.edit("π’  πΆ")
    await e.edit("π’ πΆ")
    await e.edit("π’πΆ")
    await e.edit("πΆπ’")
    await e.edit("πΆ π’")
    await e.edit("πΆ  π’")
    await e.edit("πΆ   π’")
    await e.edit("πΆ    π’")
    await e.edit("πΆ     π’")
    await e.edit("πΆ      π’")
    await e.edit("πΆ       π’")
    await e.edit("πΆ        π’")
    await e.edit("πΆ         π’")
    await e.edit("πΆ          π’")
    await e.edit("πΆ           π’")
    await e.edit("πΆ            π’")
    await e.edit("πΆ             π’")
    await e.edit("πΆ              π’")
    await e.edit("πΆ               π’")
    await e.edit("πΆ                π’")
    await e.edit("πΆ                 π’")
    await e.edit("πΆ                  π’")
    await e.edit("πΆ                   π’")
    await e.edit("πΆ                    π’")
    await e.edit("πΆ                     π’")
    await e.edit("πΆ                      π’")
    await e.edit("πΆ                       π’")
    await e.edit("πΆ                        π’")
    await e.edit("πΆ                         π’")
    await e.edit("πΆ                          π’")
    await e.edit("πΆ                           π’")
    await e.edit("πΆ                            π’")
    await e.edit("πΆ                             π’")
    await e.edit("πΆ                              π’")
    await e.edit("πΆ                               π’")
    await e.edit("πΆ                                π’")
    await e.edit("π’                       πΆ")
    await e.edit("π’                      πΆ")
    await e.edit("π’                     πΆ")
    await e.edit("π’                    πΆ")
    await e.edit("π’                   πΆ")
    await e.edit("π’                  πΆ")
    await e.edit("π’                 πΆ")
    await e.edit("π’                πΆ")
    await e.edit("π’               πΆ")
    await e.edit("π’              πΆ")
    await e.edit("π’             πΆ")
    await e.edit("π’            πΆ")
    await e.edit("π’           πΆ")
    await e.edit("π’          πΆ")
    await e.edit("π’         πΆ")
    await e.edit("π’        πΆ")
    await e.edit("π’       πΆ")
    await e.edit("π’      πΆ")
    await e.edit("π’     πΆ")
    await e.edit("π’    πΆ")
    await e.edit("π’   πΆ")
    await e.edit("π’  πΆ")
    await e.edit("π’ πΆ")
    await e.edit("π’πΆ")
    await e.edit("πΆπ’")
    await e.edit("πΆ π’")
    await e.edit("πΆ  π’")
    await e.edit("πΆ   π’")
    await e.edit("πΆ    π’")
    await e.edit("πΆ     π’")
    await e.edit("πΆ      π’")
    await e.edit("πΆ       π’")
    await e.edit("πΆ        π’")
    await e.edit("πΆ         π’")
    await e.edit("πΆ          π’")
    await e.edit("πΆ           π’")
    await e.edit("πΆ            π’")
    await e.edit("πΆ             π’")
    await e.edit("πΆ              π’")
    await e.edit("πΆ               π’")
    await e.edit("πΆ                π’")
    await e.edit("πΆ                 π’")
    await e.edit("πΆ                  π’")
    await e.edit("πΆ                   π’")
    await e.edit("πΆ                    π’")
    await e.edit("πΆ                     π’")
    await e.edit("πΆ                      π’")
    await e.edit("πΆ                       π’")
    await e.edit("πΆ                        π’")
    await e.edit("πΆ                         π’")
    await e.edit("πΆ                          π’")
    await e.edit("πΆ                           π’")
    await e.edit("πΆ                            π’")
    await e.edit("πΆ                             π’")
    await e.edit("πΆ                              π’")
    await e.edit("πΆ                               π’")
    await e.edit("πΆ                                π’")
    await e.edit("`GABUT`")


@cilik_cmd(pattern=r"terkadang(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@cilik_cmd(pattern=r"mf$")
async def _(event):
    await edit_or_reply(event, "`mf g dl` **γ(γ;_ _)γ=3** ")


@cilik_cmd(pattern=r"(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "cinta":
        await event.edit(input_str)
        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 4%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 8%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 20%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 36%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 52%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 84%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 100%\nβββββββββCINTAKUβββββββββββ `",
            "`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You π`",
        ]
        animation_interval = 2
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@cilik_cmd(pattern=r"gombal(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Hai, I LOVE YOU π`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUππ`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUππ`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUππ`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUππ`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUππ`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@cilik_cmd(pattern="helikopter(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "β¬β¬β¬.β.β¬β¬β¬ \n"
        "ββββββββ \n"
        "β’β€ ββββββββββββ’β€ \n"
        "ββ β ββ βββββββββββ¬ \n"
        "β₯ββββββ€ \n"
        "βββ©βββ©ββ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ \n"
        "β¬ββ¬ Hallo Semuanya :) \n"
        "β¬ββ¬β»/ \n"
        "β¬ββ¬/β \n"
        "β¬ββ¬/ \\ \n",
    )


@cilik_cmd(pattern="tembak(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "_/οΉ\\_\n" "(?`_Β΄)\n" "<,οΈ»β¦β€β ?\n" r"_/οΉ\_" "\n**Mau Jadi Pacarku Gak?!**",
    )


@cilik_cmd(pattern="bundir(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "`Dadah Semuanya...`          \nγγγγγ|"
        "\nγγγγγ| \n"
        "γγγγγ| \n"
        "γγγγγ| \n"
        "γγγγγ| \n"
        "γγγγγ| \n"
        "γγγγγ| \n"
        "γγγγγ| \n"
        "γοΌοΏ£οΏ£οΌΌ| \n"
        "οΌ Β΄ο½₯ γγ |οΌΌ \n"
        "γ|γοΌγ | δΈΆοΌΌ \n"
        "οΌ γο½₯γγ|γγοΌΌ \n"
        "γοΌΌοΌΏοΌΏοΌβͺ _ βͺ) \n"
        "γγγγγ οΌ΅ οΌ΅\n",
    )


@cilik_cmd(pattern="awk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "βββββββββββββββββ\n"
        "βββββββββββββββββββ\n"
        "ββββββββββββββββββ\n"
        "ββββββββββββββββββββ\n"
        "ββββββββββββββββββββββ\n`Awkwokwokwok..`",
    )


@cilik_cmd(pattern="ular(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "βββββ\n"
        "βββββ\n"
        "ββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "βββββββ\n"
        "ββββββββ\n"
        "βββββββββ\n"
        "ββββββββββ\n"
        "βββββββββββ\n"
        "ββββββββββ\n"
        "βββββββββ\n"
        "ββββββββ\n"
        "ββββββββ\n"
        "ββββββββ\n"
        "ββββββββ\n"
        "ββββββββ\n"
        "ββββββββ\n"
        "ββββββββββ\n"
        "ββββββββββββ\n"
        "ββββββββββββββ\n"
        "ββββββββββββββββ\n"
        "ββββββββββββββββββ\n"
        "βββββββββββββββββββ\n"
        "ββββββββββββββββββββ\n"
        "ββββββββββββββββββββ\n"
        "ββββββββββββββββββββ\n"
        "ββββββββββββββββββββ\n"
        "βββββββββββββββββββ\n"
        "βββββββββββββββββββ\n"
        "βββββββββββββββββββ\n",
    )


@cilik_cmd(pattern="y(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘ββββ\n"
        "β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘ββ‘β‘β‘β‘β\n"
        "β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘ββ‘β‘β‘β‘β\n"
        "β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘ββ‘β‘β‘β‘β‘β\n"
        "β‘β‘β‘β‘β‘β‘β‘β‘β‘ββ‘β‘β‘β‘β‘β‘β\n"
        "ββββββββββ‘β‘β‘β‘β‘β‘βββββββββ\n"
        "ββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β\n"
        "ββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β\n"
        "ββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β\n"
        "ββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β\n"
        "ββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β\n"
        "ββββββββββββ‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘β‘ββ\n"
        "ββββββ‘β‘β‘β‘β‘β‘β‘ββββββββββ\n",
    )


@cilik_cmd(pattern="tank(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "βΫβββββββ]βββββββββββ \n"
        "βββββββββββββββββ¦\n"
        "[βββββββββββββββββββ]\n"
        "β₯ββ²ββ²ββ²ββ²ββ²ββ²ββ€\n",
    )


@cilik_cmd(pattern="babi(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "βββββ?β­ββββ­βββββ?\n"
        "βββββββββ­β«Ngok β\n"
        "βββ°βββββ―β―β°βββββ―\n"
        "ββ­ββ»β?β²ββββββ?β­β?β\n"
        "ββββββ²β²β²β²β²β²β£ββ―β\n"
        "ββ°ββ³β»ββ―β²β²β²β²ββββ\n"
        "ββββ°ββ³βββ³βββ―βββ\n"
        "βββββββ»βββ»βββββ\n",
    )


@cilik_cmd(pattern="ajg(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "β₯βββββββββ­βββ?βββ³\n"
        "β’β­β?β­ββββββ«ββββββ£\n"
        "β’ββ°β«ββββββββββ°β«β£\n"
        "β’β°ββ«ββββββ°β―β°β³ββ―β£\n"
        "β’βββββ³β³βββββ³β«βββ£\n"
        "β¨βββββββββββββββ»\n",
    )


@cilik_cmd(pattern="bernyanyi(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "**Ganteng Doang Gak Bernyanyi (ΰΈΛoΛ)ΰΈ§**")
    sleep(2)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")
    sleep(1)
    await typew.edit("**βͺβ(γ»oο½₯)ββͺβ ( ο½₯oο½₯) β**")
    sleep(1)
    await typew.edit("**βͺβ ( ο½₯oο½₯) ββͺβ (γ»oο½₯) ββͺ**")


@cilik_cmd(pattern=r"hua$")
async def _(event):
    e = await edit_or_reply(event, "Ψ£βΏΨ£")
    await e.edit("β₯οΉβ₯")
    await e.edit("(;οΉ;)")
    await e.edit("(ToT)")
    await e.edit("(β³Πβ³)")
    await e.edit("(ΰ²₯οΉΰ²₯)")
    await e.edit("οΌοΌγΈοΌοΌ")
    await e.edit("(TοΌΏT)")
    await e.edit("οΌΟγΌΟοΌ")
    await e.edit("(οΌ΄β½οΌ΄)")
    await e.edit("(βοΉβ)")
    await e.edit("οΌο½Πο½οΌ")
    await e.edit("(Β΄Πβγ½")
    await e.edit("(;Π;)")
    await e.edit("οΌ>οΉ<οΌ")
    await e.edit("(TΠ΄T)")
    await e.edit("(γ€οΉβ)")
    await e.edit("ΰΌΌβ―οΉβ―ΰΌ½")
    await e.edit("(γοΉγ½)")
    await e.edit("(γAγ½)")
    await e.edit("(β₯_β₯)")
    await e.edit("(TβT)")
    await e.edit("(ΰΌΰΊΆβΰΌΰΊΆ)")
    await e.edit("(βοΉβ°)ο½‘")
    await e.edit("(ΰ²₯_Κΰ²₯)")
    await e.edit("(γ€Π΄β)")
    await e.edit("(βΝ_βΜ₯)")
    await e.edit("(ΰ?οΉΰ?`ο½‘)")
    await e.edit("ΰΌΌΰ²’_ΰ²’ΰΌ½")
    await e.edit("ΰΌΌ ΰΌΰΊΆ ΰ·΄ ΰΌΰΊΆΰΌ½")


@cilik_cmd(pattern="huh(?: |$)(.*)")
async def _(event):
    e = await edit_or_reply(event, "`\n(\\_/)`" "`\n(β_β)`" "`\n />β€οΈ *Ini Buat Kamu`")
    sleep(3)
    await e.edit("`\n(\\_/)`" "`\n(β_β)`" "`\n/>π  *Aku Ambil Lagi`")
    sleep(2)
    await e.edit("`\n(\\_/)`" "`\n(β_β)`" "`\nπ<\\  *Terimakasih`")


@cilik_cmd(pattern="(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str == "ceritacinta":
        await event.edit(input_str)
        animation_chars = [
            "`Cerita β€οΈ Cinta` ",
            "  π             π \n/π\\         <π\\ \n π               /|",
            "  π          π³ \n/π\\       /π\\ \n  π            /|",
            "  π            π \n/π\\         <π> \n  π             /|",
            "  π         βΊοΈ \n/π\\      /π\\ \n  π          /|",
            "  π          π \n/π\\       /π\\ \n  π           /|",
            "  π   π \n /π\\/π\\ \n   π   /|",
            " π³  π \n /|\\ /π\\ \n /     / |",
            "π    /π°\\ \n<|\\      π \n /π    / |",
            "π \n/(),βπ? \n /\\         _/\\/|",
            "π \n/\\_,__π« \n  //    //       \\",
            "π \n/\\_,π¦_π  \n  //         //        \\",
            "  π­      βΊοΈ \n  /|\\   /(πΆ)\\ \n  /!\\   / \\ ",
            "`TAMAT π`",
        ]
        animation_interval = 3
        animation_ttl = range(103)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 103])


@cilik_cmd(pattern="(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str == "canda":
        await event.edit(input_str)
        animation_chars = [
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β β β β    β’³β‘β β‘β β β    β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ β β   β    β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Kamu    β‘\n β£β£Ώβ‘­β β β β β β’±β β   β£Ώ  β’Ήβ         β‘\n  β β’Ώβ£―β β β β __β β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β β β β   β β’³β‘β β‘β β β    β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ β β       β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Pasti   β‘\n β£β£Ώβ‘­β β β β β β’±β β   β£Ώ  β’Ήβ         β‘\n  β β’Ώβ£―β β β |__|β β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β      β β’³β‘β β‘β β     β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ β β β      β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Belum   β‘\n β£β£Ώβ‘­β β β β β β’±β β   β£Ώ  β’Ήβ          β‘\n  β β’Ώβ£―β β β (x)β β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β      β β’³β‘β β‘β β     β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ    β      β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Mandi  β‘\n β£β£Ώβ‘­β β β β β β’±β    β£Ώ  β’Ήβ         β‘\n  β β’Ώβ£―β β β β __ β β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β β β β    β’³β‘β β‘β β     β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ β  β      β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Bwhaha  β‘\n β£β£Ώβ‘­β β β β β β’±β β   β£Ώ  β’Ήβ         β‘\n  β β’Ώβ£―β β β |__| β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
            "`β β β β£ β£Άβ‘Ύβ β β β ³β’¦β‘β β β β’ β β β β ²β‘β \n β β£΄β Ώβ β β β β β   β β’³β‘β β‘β β     β β’·\nβ’ β£β£β‘β’β£β£β‘β β£β‘β£§β β’Έβ   β      β‘\nβ’Έβ£―β‘­β β Έβ£β£β β‘΄β£»β‘²β£Ώ  β£Έ Canda   β‘\n β£β£Ώβ‘­β β β β β β’±β    β£Ώ  β’Ήβ         β‘\n  β β’Ώβ£―β β β ****β β β‘Ώ β β‘β β β β     β‘Ό\nβ β β β Ήβ£Άβ β β β β β β‘΄β β    β β €β£β£ β β \nβ β β β β’Έβ£·β‘¦β’€β‘€β’€β£β£β β β β β β β β β β \nβ β’β£€β£΄β£Ώβ£β β β β Έβ£β’―β£·β£β£¦β‘β β β β β β \nβ’β£Ύβ£½β£Ώβ£Ώβ£Ώβ£Ώβ β’²β£Άβ£Ύβ’β‘·β£Ώβ£Ώβ ΅β£Ώβ β β β β β \nβ£Όβ£Ώβ β β£Ώβ‘­β β β’Ίβ£β£Όβ‘β β  β β£β’Έβ β β β β β `",
        ]
        animation_interval = 1
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@cilik_cmd(pattern="santet(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Mengaktifkan Perintah Santet Online....`")
    sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   β")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββββ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   βββββββββββββββββ")
    sleep(1)
    await typew.edit("**Target Berhasil Tersantet Online π₯΄**")


@cilik_cmd(pattern="nah(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(
        event, "`\n(\\_/)`" "`\n(β_β)`" "`\n />π *Ini Buat Kamu`"
    )
    sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(β_β)`" "`\nπ<\\  *Tapi Bo'ong`")

    
CMD_HELP.update(
    {
    "Animasi": f"**β’ Plugin : **`Animasi`\
    \n\n **α΄α΄α΄ :** `{cmd}gabut`\
    \n ββ buat bercanda\
    \n\n **α΄α΄α΄ :** `{cmd}dino`\
    \n ββ buat bercanda\
    \n\n **α΄α΄α΄ :** `{cmd}gombal`\
    \n ββ buat bercanda\
    \n\n **α΄α΄α΄ :** `{cmd}cinta`\
    \n ββ mengirim cintamu ke seseorang.\
    \n\n **α΄α΄α΄ :** `{cmd}sayang`\
    \n ββ untuk jadi buaya.\
    \n\n **α΄α΄α΄ :** `{cmd}terkadang`\
    \n ββ Auk dah iseng doang.\
    \n\n **α΄α΄α΄ :** `{cmd}helikopter` ; `{cmd}tank` ; `{cmd}tembak`\n`{cmd}bundir`\
    \n ββ liat sendiri\
    \n\n **α΄α΄α΄ :** `{cmd}y`\
    \n ββ jempol\
    \n\n **α΄α΄α΄ :** `{cmd}bulan` ; `{cmd}hati` ; `{cmd}bernyanyi`\
    \n ββ liat aja.\
    \n\n **α΄α΄α΄ :** `{cmd}awk`\
    \n ββ ketawa lari.\
    \n\n **α΄α΄α΄ :** `{cmd}lar` ; `{cmd}abi` ; `{cmd}ajg`\
    \n ββ liat sendiri.\
    \n\n **α΄α΄α΄ :** `{cmd}nah` ; `{cmd}huh` ; `{cmd}owner`\
    \n ββ cobain.\
    \n\n **α΄α΄α΄ :** `{cmd}bunga` ; `{cmd}buah`\
    \n ββ animasi.\
    \n\n **α΄α΄α΄ :** `{cmd}waktu`\
    \n ββ animasi.\
    \n\n **α΄α΄α΄ :** `{cmd}hua`\
    \n ββ nangis.\
    \n\n **α΄α΄α΄ :** `{cmd}ceritacinta` ; `{cmd}canda`\
    \n ββ liat sendiri\
    \n\n **α΄α΄α΄ :** `{cmd}santet`\
    \n ββ Santet Online Buat Bercanda.\
    "
    }
)    
