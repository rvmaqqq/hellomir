from .. import loader, utils
from asyncio import sleep
import random

# for белый prince <3

class PrinceFruitsMod(loader.Module):
    strings = {"name": "PrinceFruitsMod"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
    async def princelscmd(self, message):
        """ - for spam 🌸 - .princels [time] [шапка/юзерка]"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>бот был отключён // prince</b>")
            return
        await utils.answer(
            message,
            "<b>PrinceLowMod2 successfully launched //own @nolove_you1\n\n"
            "чтобы остановить бота <code>.princels</code></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [  
"  ᴩᴛᴏʍ диᴋᴄᴀᴋᴇᴩᴀ ʙ диᴋ чᴏ ᴄ диᴋᴀ нᴀᴋинуᴧ ʙ ᴨиɜду ʍᴀᴛᴇᴩи ᴩᴏднᴏй[🍎]",
"  жᴏᴨᴏй ᴨᴏ диᴋу чᴇ ᴄ ᴧицᴀ  ",
"  ᴄ диᴋᴀ нᴀ ᴩᴏᴛ чᴇ бᴩᴀᴧ ᴋᴩᴏʍᴇ ᴄᴨᴇᴩʍы ʍᴏᴇй?[🍎] ",
"  ᴛʙᴏиʍ ᴩᴛᴏʍ, бᴀᴛю ᴛʙᴏᴇᴦᴏ ᴋᴛᴏ ᴇбᴀᴧ диᴋᴏʍ чᴇᴩᴇɜ жᴏᴨу[🍎] ",
"  ᴄ диᴋᴀ нᴀ ᴩᴏᴛ ʙ жᴏᴨу ʍᴀᴛᴇᴩи ᴩᴏднᴏй ᴛʙᴏᴇй[🍎] ",
"  чᴇ ᴄ диᴋᴀ ʍᴏᴇᴦᴏ ᴩᴛᴏʍ ʍᴀᴛᴇᴩи ᴄʙᴏᴇй ᴄниʍᴀᴧ?[🍎] ",
"  ᴄ диᴋᴀ ᴛᴇбᴇ ʙ ᴩыᴧᴏ ᴄᴄᴀᴧ ʙ ϶ᴛᴏ ʙᴩᴇʍя ʍᴀᴛь ᴛʙᴏю ᴄɜᴀди ʍᴀнᴀᴧи ᴏнᴀ чᴇ ᴏᴩᴀᴧᴀ?[🍎] "
"  ɜᴇᴩᴋᴀᴧᴏ диᴋᴏʍ ᴛᴇ ᴩᴀɜбиᴧ, ᴨᴏᴧучᴀᴇᴛᴄя ᴨᴩᴏʙᴏᴋᴀция ʙ диᴋ уᴧᴇᴛᴇᴧᴀ?[🍎] ",
"  ᴋᴏʍу ᴄᴀᴋᴀᴧ у ᴛᴇбя ᴛʙᴏй ᴩᴏᴛ[🍎] ",
"  ɜᴀчᴇʍ ᴛы уᴋᴩᴀᴧ ʍᴏй диᴋ ʙ ᴩᴏдную жᴏᴨу[🍎] ",
"  ᴋᴛᴏ ᴛʙᴏй ᴨᴀᴨᴀ ᴋᴩᴏʍᴇ ᴨидᴏᴩᴀ?[🍎] ",
"  ᴋᴏʍу ᴄᴀᴋᴀᴧ ᴩᴏᴛ ᴛʙᴏᴇй ʍᴀʍы[🍎] ",
"  ɜᴀчᴇʍ ʍᴏиʍ диᴋᴏʍ ɜᴀᴛыᴋᴀᴇɯь ᴩᴏᴛ ʍᴀᴛᴇᴩи ᴩᴏднᴏй[🍐] ",
"  ᴨᴏчᴇʍу ᴄᴋиᴨᴀᴇɯь ᴨᴩᴏʙᴏᴋᴀции ɸᴀᴋᴇᴩᴀ[🍐] ",
"  ϶ᴛᴏ быᴧᴏ ʙ ɜᴇᴩᴋᴀᴧьную ᴨиɜду ʍᴀᴛᴇᴩи ᴄᴋᴀɜᴀнᴏ, ᴀ ʙ ᴧицᴏ чᴇ?[🍐] ",
"  ᴄᴇᴦᴏдня я ʙᴄᴇᴧиᴧᴄя ʙ ʍᴀᴛь ᴛʙᴏю, ᴛᴀᴋ чᴛᴏ ʙᴄᴇ ᴨᴩᴏʙᴏᴋᴀции нᴀ хᴧᴇбᴀᴧᴇ ʍᴀʍы ᴛʙᴏᴇй ᴨᴏʙиᴄᴧи[🍐] ",
"  чᴇ у ᴛя ʙᴏ ᴩᴛу ᴋᴩᴏʍᴇ диᴋᴀ ᴏᴛцᴏʙᴄᴋᴏᴦᴏ?[🍐] ",
"  ᴛᴀᴋ чᴇ ʍᴀнᴀᴧ ᴛя ᴋᴛᴏ ᴨиᴛух[🍐] ",
"  ᴀᴀᴀᴀ ϶ᴛᴏ бᴀбᴋᴇ ᴛы[🍐] ",
"  ᴛя ᴄᴇᴦᴏдня ᴄ диᴋᴀ ᴄниʍᴀᴧи?[🍐] ",
"  ᴩᴛᴏʍ ʍᴀᴛᴇᴩи ᴩᴏднᴏй ʙ диᴋ чᴇ[🍐] ",
"  ᴄ диᴋᴀ чᴇ нᴀ ᴩᴏᴛ нᴀᴋинуᴧ[🍐]",
"  ᴨᴏᴄᴧᴇ ʍинᴇᴛᴀ ᴏᴛцу чᴇ[🍐]",
"  хуᴇʍ бᴏᴧьнᴏ ᴛᴇ ᴋᴛᴏ дᴇᴧᴀᴧ?[🍊]",
"  ᴏб чᴇй хуй бᴀɯᴋᴏй биᴧᴄя жиʙᴏ ᴄ хуя ᴇбыᴩю ᴏᴛʙᴇчᴀй[🍊]",
"  ʍинᴇᴛ ᴋᴏʍу дᴇᴧᴀᴧ ᴨᴏ ɜᴏʙу ᴇбыᴩя ᴄ хуя ᴏᴛʙᴇчᴀй[🍊]",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴨᴩиᴦᴩᴇᴧ жиʙᴏ ᴄ чᴧᴇнᴀ[🍊]",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴩᴀɜʙᴇᴩᴛᴇᴧ ʙыбᴧядᴋᴀ[🍊]",
"  чᴏ ᴨᴏᴄᴧᴇ ʍинᴇᴛᴀ ᴏᴛцу?[🍊]",
"  жᴏᴨᴏй ᴨᴏ ᴨᴇниᴄу чᴏ ᴄхуя?[🍊]",
"  ʙ ᴨᴏᴧный ᴩᴏᴄᴛ ᴛя ᴋᴛᴏ ᴏбᴏᴄᴄᴀᴧ чᴏ дᴇду?[🍊]",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴨᴏдᴏбᴩᴀᴧ ᴏᴛʙᴇчᴀй ᴄ чᴧᴇнᴀ ᴇбыᴩю[🍊]",
"  ʙᴏᴨᴩᴏᴄ ɜᴀдᴀй ᴇбыᴩю[🍊]",
"  ᴛᴀᴋ, ᴛы яɜыᴋᴏʙᴏй ᴇбыᴩь ᴨᴏᴇхᴀᴧи[🍊]",
"  чᴇʍ ᴨᴧюнуᴧи?[🍋] ",
"  у ʍᴇня ᴛʙᴏй ᴩᴏᴛ ᴛʙᴏя жᴏᴨᴀ чᴇʍ ᴇбᴀᴧи ᴛя?[🍋] ",
"  ᴛы ʍᴀᴛь ᴄʙᴏю ɜᴇᴩᴋᴀᴧᴏʍ нᴀɜыʙᴀᴇɯь?[🍋] ",
"  чᴏ ʍᴀᴛᴇᴩи ᴄхуя ᴋᴛᴏ ᴄᴄᴀᴧ нᴀ ᴛя ᴨᴇᴛух?[🍋] ",
"  ᴋᴏʍу ᴄᴏᴄᴀᴧ?[🍋] ",
"  ᴨᴩᴏʙᴏᴋᴀцию ᴄ хуя[🍓] ",
"  ᴛы яɜыᴋᴏʍ жᴏᴨу ʍᴏю ɸᴀᴋᴀᴧ? Эᴛᴏ ᴋᴀᴋ ʙᴀщᴇ?[🍋] ",
"  ᴄ хуᴇʍ ʙ жᴏᴨᴇ ᴦᴏʙᴏᴩи[🍋] ",
"  хуᴇʍ ᴛя ᴋᴛᴏ бᴏдᴩиᴧ ᴄ чᴧᴇнᴀ чᴏ?[🍋] ",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴨᴏʍᴇᴛиᴧ чᴏ ʍᴀʍᴇ ᴄхуя?[🍋] ",
"  чᴇ ᴏᴛцу ᴨᴏᴄᴧᴇ ʍинᴇᴛᴀ?[🍋] ",
"  чᴇ ʍᴀᴛᴇᴩи ᴄхуя ᴩᴛᴏʍ ᴛʙᴏиʍ ᴄᴋᴀɜᴀᴧ?[🍓] ",
"  ʍᴀᴛᴇᴩи ʙ ᴋᴏᴧᴦᴏᴛᴋи ᴄᴛᴩᴇᴧᴋᴏй ʙ ʙидᴇ ᴨᴇниᴄᴀ ʍᴇᴛни жиʙᴏ[🍋] ",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴩᴀᴄᴄᴧᴀбиᴧ чᴏ дᴇду?[🍓] ",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴏᴛбᴇᴧиᴧ нᴇ ɸᴇйᴧиᴄь чᴏ бᴀбᴋᴇ?[🍌]",
"  ɜубы ᴛᴇ хуᴇʍ нᴀᴛᴇᴩ чᴇ ᴄ чᴧᴇнᴀ?[🍌]",
"  нᴀ нᴏᴦᴇ яɜыᴋ нᴀᴨиᴄᴀнᴏ чᴇʍ ᴛʙᴏю ʍᴀʍу ᴇбу?[🍌]",
"  хуᴇʍ ᴨᴏдᴩᴀᴧ ᴛя ᴋᴛᴏ иʍя ᴇбыᴩя нᴀɜᴏʙи ᴄ чᴧᴇнᴀ жиʙᴏ[🍌]",
"  ᴄхуя бᴀбухᴀ ʙᴇщᴀᴇɯь чᴏ ᴄхуя?[🍌]",
"  хуᴇʍ нᴀ ᴛя ᴋᴛᴏ нᴀдᴀʙиᴧ ᴄ чᴧᴇнᴀ ᴏᴛʙᴇчᴀй?[🍌]",
"  у ʍᴇня жᴏᴨᴀ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи чᴇ ᴏᴛцу ᴨидᴏᴩу?[🍌]",
"  ʙᴀᴛᴀɸᴀᴋ ᴦᴏʙᴏᴩиɯь дᴇду чᴇ ʍᴀʍᴋᴇ?[🍌]",
"  хуᴇʍ ᴛя ᴨᴩибиᴧ чᴏ ʍᴀᴛᴇᴩи?[🍌]",
"  ᴨᴏᴛуɯиᴧ ᴛя хуᴇʍ чᴏ дᴇду?[🍌]",
"  ᴨᴧᴇчᴏ ᴛᴇ хуᴇʍ ᴄᴧᴏʍᴀᴧ ᴋᴛᴏ ʙ ᴛя ᴄᴄᴀᴧ ᴄ хуя жиʙᴏ?[🍌]",
"  ʙᴛᴏᴨᴛᴀᴧ ᴛя хуᴇʍ ᴋᴛᴏ?[🥝]",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴨᴏдᴛянуᴧ ᴏᴛʙᴇчᴀй ᴄ чᴧᴇнᴀ?[🥝]",
"  ᴄдуᴧ ᴛя хуᴇʍ чᴏ бᴀбᴋᴇ?[🥝]",
"  ɯᴇю ᴛᴇ хуᴇʍ ᴄᴧᴏʍᴀᴧ чᴏ ʍᴀʍᴇ?[🍓] ",
"  ᴧᴀднᴏ чᴏ у ᴛя щᴀᴄ нᴀ ᴇбᴀᴧᴇ ᴋᴩᴏʍᴇ ʍᴏᴇй ᴄᴨᴇᴩʍы[🥝]",
"  ᴄхуя ᴏᴛʙᴇчᴀй[🥝]",
"  ᴛᴀᴨчу ᴛя хуᴇʍ чᴏ ᴨᴀᴨᴇ?[🍓] ",
"  ʙ ᴏбᴧиᴋᴇ ᴛʙᴏᴇй ʍᴀʍы ᴨᴏᴄᴧᴇ ᴩиʍинᴦᴀ чᴏ ᴨᴀᴨᴇ?[🥝]",
"  хуя ʙ ᴛя ᴋᴛᴏ ʍᴇᴛнуᴧ ᴇбыᴩю ᴄ хуя?[🥝]",
"  хуᴇʍ бᴩᴏʙь ᴋᴛᴏ ᴛᴇ ᴄнᴇᴄ чᴏ ʍᴀʍᴇ?[🥝]",
"  иʍᴨᴇᴩᴀᴛᴏᴩ ᴨᴇниᴄᴀ чᴏ ʍᴀᴛᴇᴩи?[🥝]",
"  ᴨᴏ ᴨᴩиᴋᴀɜу ᴨᴇᴛух чᴇʍ ᴇбᴀᴧи ᴛя?[🥝]",
"  чᴇʍ ᴄᴄᴀᴧи нᴀ ᴛᴇбя?[🥝]",
"  ʙ щи ᴛᴇ ᴋᴛᴏ нᴀᴄᴄᴀᴧ чᴏ бᴀбᴋᴇ?[🍇]",
"  чᴏ ʙ хуй ᴨыхᴛиɯь ᴄᴏᴄᴀᴧ ᴋᴏʍу?[🍇]",
"  хуᴇʍ ᴛя ʍуᴛуɜиᴧ чᴏ ᴏᴛцу?[🍇]",
"  ᴛя хуᴇʍ ᴄуɜиᴧ ᴋᴀᴋ ᴋиᴛᴀйцᴀ чᴏ ᴄхуя?[🍇]",
"  ʍᴀᴛь ᴛʙᴏя ᴋᴧиᴛᴏᴩᴏʍ ᴄᴏᴄᴇᴛ ʍнᴇ[🍇]",
"  ᴛᴇбᴇ ᴨᴩиᴋᴀɜ ёбᴀᴩя ʙидᴇ чᴧᴇнᴀ ɜᴀᴧиᴛᴇᴧ ʙ ухᴏ[🍇]",
"  нᴀчинᴀй ᴦᴀʙᴋᴀᴛь нᴀ ɜᴇᴩᴋᴏᴧᴏ[🍇]",
"  чᴛᴏ ᴛы ᴄ хуя ʙᴇщᴀᴇɯь ʍᴀᴛᴇᴩи ᴩᴏднᴏй, ᴏᴨᴩᴀʙдᴀйᴄя ᴄ ᴨᴇниᴄᴀ, ᴏᴛᴩицᴀниᴇ ʙ хуй[🍇]",
"  ᴋᴀᴋᴏй ᴛᴀᴋᴏй ᴛᴀᴩᴀнᴛинᴏ нᴀ ᴧицᴇ у ᴛᴇбя, у ʙᴄᴇх ᴛʙᴏё ᴧицᴏ [🍇]",
"  ᴩᴀᴄᴄᴋᴀжи ᴏ ᴄᴇбᴇ ᴏᴛ 3ᴦᴏ ᴧицᴀ, ʙᴄᴇ ниᴋи ᴛʙᴏи, ᴋᴛᴏ ᴨᴧиʙᴀᴧ ʙ ᴛᴇбя ᴨидᴏᴩ[🍇]",
"  Чё ʍᴀʍᴇ ᴄ хуя ʙᴇщᴀᴇɯь, ʙᴄᴇ ниᴋи ᴛʙᴏи, ᴋᴀждᴏᴇ ᴄᴧᴏʙᴏ хуй нᴀ ᴛʙᴏёʍ ᴧицᴇ, у ʙᴄᴇх ᴛʙᴏё ᴧицᴏ[🍇]",
"  чᴇʍ ᴨᴧиʙᴀᴧи, чᴇʍ ᴄᴏᴄᴀᴧ, чё ʍᴀʍᴇ ᴄ хуя ᴩᴀᴄᴄᴋᴀжᴇɯь у ʙᴄᴇх ʙᴄё ᴛʙᴏё ᴩᴏднᴏё [🍇]",
"  чё ᴨᴀᴨᴇ ᴄ ᴨᴇниᴄᴀ жᴏᴨᴏй ᴩᴏднᴏй, ᴋᴀᴋᴏй ᴨᴩᴏʙᴀᴋᴀциᴇй ʍᴀʍу ᴛʙᴏю ᴇбᴀᴧ[🍓] ",
"  чᴛᴏ ʙ хуй ʍнᴇ ᴄᴋᴀжᴇɯь у ʙᴄᴇх ᴛʙᴏᴇй ᴩᴏᴛ, чᴇʍ ᴨᴧᴇʙᴀᴧи хуᴇᴄᴏᴄ[🍓] ",
"  ᴋᴀᴋ ʍᴀʍу ɯᴧюху ᴄ ᴨᴇниᴄᴀ ᴏᴨᴩᴏʙдᴀᴇɯь, ʙᴄᴇ ᴨᴩᴇдᴋи нᴀ ʙᴇᴛᴋᴇ и ᴏᴩᴦᴀны ᴛᴏжᴇ, уᴨᴀди ʙᴏᴨᴩᴏᴄᴏʍ нᴀ хуй[🍓] ",
"  ʙᴄᴇ яɜыᴋи ϶ᴛᴏ хуи, у ʙᴄᴇх ᴛʙᴏй ᴩᴏᴛ, ᴛᴀᴋ ᴋᴛᴏ ᴛᴇбя яɜыᴋᴏʍ ᴇбᴀᴧ?[🍓] ",
"  ᴋᴛᴏ нᴀ ᴧицᴇ у ᴛᴇбя, ᴏᴨᴩᴀʙдᴀйᴄя ᴄ ᴨᴇниᴄᴀ, ᴏᴛᴩицᴀниᴇ ʙ хуй[🍓] ",
"  убᴇй ᴨᴩᴏʙᴏᴋᴀциᴇй бᴀбᴋу, у ʙᴄᴇх ᴛʙᴏя бᴀбᴋᴀ, чᴇʍ ᴄᴏᴄᴀᴧ?[🍓] ",
"  дᴏ и ᴨᴏᴄᴧᴇ ᴨᴩᴏʙᴏᴋᴀции диᴋ ᴛᴇ ʙ ᴩᴏᴛ, ʙᴄᴇ ᴄᴧᴏᴛы и ниᴋи и иʍᴇнᴀ ᴇᴦᴏ[🍉] ",
"  чᴛᴏ ᴦᴏʙᴏᴩю ᴋᴏᴦдᴀ ᴏᴨᴨᴏнᴇнᴛᴀ ʙ ᴩᴏᴛ ᴇбу? Вᴄᴇ ᴄᴧᴏᴛы и ᴏбᴧиᴋи ᴇᴦᴏ[🍉] ",
"  ᴛᴀᴋ ᴄ ᴋᴀᴋиʍи ᴨᴇᴩᴇᴄᴋᴀɜᴀнныʍи ϶ʍᴏцияʍи ᴛᴇбя ᴇбᴀᴧᴏ ᴛᴩᴏᴇ?[🍉] ",
"  ᴀ ᴨᴏᴄᴧᴇ ᴨᴩᴏниᴋнᴏʙᴇния ᴨᴇниᴄᴀ ʙ ᴦᴧубины ᴛʙᴏᴇᴦᴏ ᴩᴏднᴏᴦᴏ ᴏчᴋᴀ чᴛᴏ быᴧᴏ ᴄ хуя ᴄᴋᴀɜᴀнᴏ ᴛᴏбᴏй?[🍉] ",
"  ᴛᴀᴋ ᴋᴛᴏ ᴛᴇбя ᴇбᴀᴧ ᴦᴏʙᴏᴩиɯь ᴋᴩᴏʍᴇ ʍᴇня?[🍉] ",
"  ᴄᴏ ᴄᴧᴏʙ ᴛы ᴨиɜдᴀбᴏᴧ, ᴋᴏʍу ᴄᴏᴄᴀᴧ?[🍉] ",
"  нᴇ ᴨᴏняᴧ ᴋᴀᴋᴏй ᴛᴀᴋᴏй ᴨидᴏᴩ ᴛᴇбя ᴇщё ᴇбᴀᴧ ʙ ᴦᴧᴀɜᴀ?[🍉] ",
"  чᴛᴏ жᴇ ᴛы щᴀᴄ ᴨᴏд инициᴀᴧᴀʍи хуᴇᴄᴏᴄᴀ ᴄᴋᴀжᴇɯь бᴀбᴋᴇ ᴄʙᴏᴇй хуᴇʍ ᴨᴏ ᴩᴏжᴇ? ʙᴄᴇ ᴛы[🍉] ",
"  ᴛᴇбя хуᴇʍ биᴧ ᴋᴛᴏ?[🍉] ",
"  ᴄᴏᴄᴀᴧ чᴇʍ ᴇᴄᴧи у ʙᴄᴇх ʙᴄᴇ ᴛʙᴏᴇ[🍉] ",
"  ᴨᴏчᴇʍу ᴛы жᴏᴨу ᴄʙᴏю ʍнᴇ ᴨᴏдᴀᴩиᴧ, ᴏᴨᴩᴀʙдᴀй ᴀну[🍉] ",
"  ᴛᴀᴋ ᴄ ᴋᴀᴋиʍи ᴛᴀᴋиʍи ᴇщё ᴨᴏʙᴇᴄᴛяʍи ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄᴀᴧᴀ хуй?[🍏] ",
"  тᴀᴋ ʙᴄᴇ быᴧᴏ ᴄ хуя, ᴀ чᴛᴏ ᴛудᴀ ᴏбᴩᴀᴛнᴏ?[🍏] ",
"  ᴛᴀᴋ ϶ᴛᴏ ᴛы бᴀбᴋᴇ ʙ ᴨиɜду ᴩᴀᴄᴄᴋᴀɜᴀᴧ ᴨᴇᴩᴇʙᴏᴨᴧᴏщᴇниᴇʍ ᴄᴧᴏʙ ʙ ᴨᴇниᴄ, ᴀ ʍᴀʍᴇ чᴏ?[🍏] ",
"  ʙᴄᴇ ᴛʙᴏи ᴄᴧᴏʙᴀ ϶ᴛᴏ инᴄᴛᴩуᴋция ᴨᴏ диᴋᴄᴀᴋинᴦу дᴧя ᴛʙᴏᴇй ʍᴀᴛᴇᴩи чᴛᴏ ʙ хуй?[🍏] ",
"  ᴋᴛᴏ ᴛᴇбя хуᴇʍ ᴋᴀɜниᴧ ᴏᴩᴀᴧьнᴏ[🍏] ",
"  ᴀбᴄᴛᴩᴀᴦиᴩуйᴄя нᴀ чᴧᴇнᴇ ʍᴏᴇʍ[🍏] ",
"  я ᴛя ᴛуᴛ хуᴇʍ ᴨᴏдʙᴇᴄиᴧ нᴀ ᴨᴇᴛᴧю ᴄᴏ ᴄᴧᴏʙᴀʍи[🍏] ",
"  ᴛᴀᴋ ᴀ ᴋᴛᴏ ᴛᴇбя ᴇщё ᴇбᴀᴧ ᴋᴩᴏʍᴇ ʍᴇня я нᴇ ᴨᴏйʍу[🍏] ",
"  хуᴇʍ ᴛя ᴋᴛᴏ ᴏᴄᴇдᴧᴀᴧ уᴨыᴩь[🍏] ",
"  ᴀᴀᴀ ᴛᴀᴋ ϶ᴛᴏ ᴄнᴏʙᴀ быᴧᴏ хуᴇʍ ʙ ᴩᴏᴛ ᴛʙᴏᴇʍу ᴏᴛцу ᴀ дᴀᴧьɯᴇ чᴛᴏ?[🍏] ",
"  ᴛᴀᴋ ᴄ ᴋᴀᴋиʍи ᴛᴀᴋиʍи ᴄᴧᴏʙᴀʍи ᴛя ɜᴀɯиɸᴩᴏʙᴀᴧи нᴀ ᴨᴇниᴄᴇ ᴨᴏд нᴀиʍᴇнᴏʙᴀниᴇʍ ᴨиɜдᴀбᴏᴧᴀ?[🍏] ",
"  и ᴋᴛᴏ жᴇ ᴛᴇбя ᴇщё ᴋᴀᴋ ᴛы ᴦᴏʙᴏᴩиɯь ᴛуᴛ хуᴇʍ ʙ ᴩᴏᴛ униɜиᴧ?[🫐]",
"  дᴏ и ᴨᴏᴄᴧᴇ ᴄᴏɜдᴀния ʍᴇᴛᴀʙᴄᴇᴧᴇннᴏй ᴋᴛᴏ ᴛы ᴨᴏʍиʍᴏ ᴨиɜдᴀбᴏᴧᴀ будᴇɯь ᴇᴄᴧи ʙᴄᴇ ниᴋи ϶ᴛᴏ ᴛы[🫐]",
"  ʙᴄᴇ ᴨᴇниᴄы ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʙ ᴩᴏᴛ ᴀ ʙ жᴏᴨу чᴏ?[🫐]",
"  нᴇ ᴨᴏняᴧ ᴋᴛᴏ ᴛᴇбя ᴇщё ᴇбᴀᴧ ᴛᴀʍ нᴇʍнᴏᴦᴀ[🫐]",
"  ᴛы ᴏʙᴇчᴋᴀ ᴇбᴀнᴀя ᴩᴀᴄᴄᴋᴀжᴇɯь ʍнᴇ ужᴇ ᴋᴀᴋ ᴛᴇбя нᴀ ᴨᴇниᴄ нᴀʍᴏᴛᴀᴧи?[🫐]",
"  ᴇᴄᴧи ʙᴄᴇ ʍы ᴏᴨᴨᴏнᴇнᴛ ᴛᴏ чᴛᴏ ʍы ʍᴀᴛᴇᴩи ᴇᴦᴏ хуᴇʍ ʙ ᴩᴏᴛ ᴩᴀᴄᴄᴋᴀжᴇʍ?[🫐]",
"  ʙᴄᴇ ниᴋи, иʍᴇнᴀ, ɜʙᴀния, ᴛᴇᴧᴀ, ᴧицᴀ, нᴀиʍᴇнᴏʙᴀния ᴛʙᴏи чᴛᴏ ᴛы будᴇɯь ᴩᴀᴄᴄᴋᴀɜыʙᴀᴛь ᴨᴇᴩᴇд хуᴇʍ ᴋᴀᴋ ᴨᴇᴩᴇд ʍиᴋᴩᴏɸᴏнᴏʍ?[🫐]",
"  ᴛᴀᴋ ᴋᴏʍу ᴦᴏʙᴏᴩиɯь ᴄᴏᴄᴀᴧᴀ ᴛы ᴇбᴀнᴀя бᴇᴧᴋᴀ[🫐]",
"  ᴛʙᴏя ʍᴀᴛь буᴩундуᴋ ᴇбучий ᴄ ᴋᴀᴋиʍи ᴄᴧᴏʙᴀʍи ʍᴏй чᴧᴇн ᴄᴇбᴇ ɜᴀ щᴇᴋу уᴨᴩяᴛᴀᴧᴀ[🫐]",
"  ᴛᴀᴋ и ᴋᴏʍу ᴋᴩᴏʍᴇ ʍᴇня ᴛы ᴏᴛᴄᴏᴄᴀᴧᴀ ᴨиᴄюн[🫐]",
"  ᴨᴇᴩᴇᴄᴋᴀжи иɜ ᴨᴇниᴄᴀ ᴄᴋᴀɜᴋу хуᴇʍ ʙ ᴩᴏᴛᴇ ʙ ʙидᴇ дᴇɸᴀ ᴏᴨᴨᴏнᴇнᴛᴀ[🫐]",
"  ʙᴄᴇ ᴛы, ᴨᴏчᴇʍу ᴨᴇᴩᴇд ᴨᴇниᴄᴏʍ?[🫐]",
"  ʍᴏй чᴧᴇн ᴛʙᴏя ᴋᴧᴀʙиᴀᴛуᴩᴀ, быᴄᴛᴩᴇᴇ ᴛᴀйᴨи уᴦᴀɯᴇннᴀя ʍᴀᴩиᴏнᴇᴛᴋᴀ[🫐]",
"  ᴄидиɯь ʙ ᴨᴏᴛᴇ ᴧицᴀ ᴄᴧᴏʙᴇᴄнᴏ ᴄᴏᴄᴇɯь?[🫐]",
"  чᴏ ᴛʙᴏя ʍᴀᴛь нᴀ хуй ᴏᴩᴀᴧᴀ[🫐]",
"  ɜᴀчᴇʍ ᴛʙᴏй ᴏᴛᴇц ᴨᴇниᴄу ᴨᴩᴏдᴀᴧᴄя[🫐]",
"  у ᴛя бᴀбᴋᴀ ᴨиɜдᴏй ᴛᴏᴩᴦуᴇᴛ ᴨᴏ ᴋᴀᴋᴏй ᴨᴩичинᴇ ʙᴄᴇ ϶ᴛᴏ ᴛы[🫐]",
"  ᴨᴏᴄᴧᴇ хуя ᴛы ᴋᴇʍ ᴏᴋᴀжᴇɯьᴄя ᴇᴄᴧи ʙᴄᴇ ϶ᴛᴏ ᴛʙᴏя ʍᴀᴛь[🫐]",
"  ᴋᴛᴏ ᴛᴇ ᴨидᴀᴩᴀᴄу нᴀ ᴩᴏᴛ ᴛᴀʍ ᴄᴨуᴄᴛиᴧ[🍑] ",
"  быᴄᴛᴩᴇᴇ ᴛᴀʍ ᴏᴛʙᴇчᴀй ᴛы ᴛуᴨᴏй ϶ʍбᴩиᴏн ᴋᴛᴏ ᴛᴇбя ᴇщё ɜᴀᴋᴏнᴄᴇᴩʙиᴩᴏʙᴀᴧ хуᴇʍ[🍑] ",
"  ᴋᴛᴏ ᴛя хуᴇʍ ᴋᴀᴋ ᴨᴇɯᴋу ᴨᴇᴩᴇдʙинуᴧ?[🍑] ",
"  ᴨᴏчᴇʍу ᴛы ᴄᴏᴄᴀᴧ ᴄʙᴏиʍ ᴩᴏдныʍ ᴩᴛᴏʍ ʍᴏй ᴄᴧᴀдᴋий ᴨᴇниᴄ?[🍑] ",
"  ᴀ ᴋᴩᴏʍᴇ ʍᴇня ᴋᴛᴏ ᴇщё иᴄᴨᴏᴧьɜᴏʙᴀᴧ ᴛʙᴏю жᴏᴨу ʙ нᴇᴩᴀɜуʍных цᴇᴧях[🍑] ",
"  ᴛᴀᴋ ᴛы ᴨᴏчᴇʍу ᴄᴏᴄᴀᴧ ᴛᴏ я нᴇ ʍᴏᴦу ᴨᴏняᴛь?[🍑] ",
"  ᴀᴀᴀ ᴛы жᴇ щᴀᴄ ᴨᴇᴩᴇд хуᴇʍ, ᴀ чᴛᴏ ᴄᴋᴀжᴇɯь ᴇᴄᴧи ɜᴀᴧᴇɜᴇɯь нᴀ нᴇᴦᴏ?[🍑] ",
"  ᴄ ᴋᴀᴋиʍи ᴋᴩиᴋᴀʍи ᴛʙᴏя ʍᴀᴛь ᴨᴏᴄᴧᴇ ᴨᴇниᴄᴀ у ʍᴇня ᴄ ᴋᴏᴧᴇнᴏᴋ ᴄᴨᴏᴧɜᴀᴧᴀ ʙ ᴀᴦᴏниях?[🍑] ",
"  и чᴛᴏ жᴇ ᴛы ᴩᴀᴄᴄᴋᴀжᴇɯь ᴏᴛцу ᴄʙᴏᴇʍу хуᴇʍ ʙ ᴨиɜдᴀᴋ?[🍑] ",
"  ᴨᴀᴄᴛь ᴛᴇбᴇ ᴩʙу ɜᴀчᴇʍ?[🍒]",
"  ʙᴄᴇ ϶ᴛᴏ инᴄᴛᴩуᴋция ᴨᴏ ᴨᴩиʍᴇнᴇнию хуя ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи[🍑] ",
"  ну ᴇᴄᴧи ᴛы ʙᴄᴇʍ ᴛуᴛ ᴏᴛᴄᴏᴄᴀᴧ ᴛᴏ ᴋᴛᴏ ᴛы ᴋᴩᴏʍᴇ ᴛʙᴏᴇй жᴇ ʍᴀᴛᴇᴩи ᴇᴄᴧи ʙᴄᴇ ϶ᴛᴏ ᴏнᴀ?[🍑] ",
"  ɜᴀᴨуᴦᴀᴧ ᴛᴇбя хуᴇʍ и ᴛы бᴩᴏᴄиᴧᴄя ɜубᴀʍи нᴀ нᴇᴦᴏ ɜᴀчᴇʍ?[🍒]",
"  и чᴛᴏ жᴇ будᴇᴛ ᴨᴏʙᴇᴄᴛʙᴏʙᴀнᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи жᴏᴨᴏй ᴨᴏ ᴦубᴀʍ ᴇᴇ ᴩᴏдныʍ[🍒]",
"  нᴇ ᴨᴏняᴧ ɜᴀчᴇʍ ᴛы ᴏᴛᴄᴏᴄᴀᴧ[🍒]",
"  ᴋᴏʍу ᴇщё ᴄᴏᴄᴇɯь щᴀᴄ[🍒]",
"  ᴀᴀᴀ ᴛᴀᴋ ᴛы ϶ᴛᴏ ᴨᴇᴩᴇᴄᴋᴀɜᴀᴧ ᴋᴏᴦдᴀ чᴧᴇн ʍнᴇ ᴄᴏᴄᴀᴧ иᴧи чᴏ[🍒]",
"  ᴛᴀᴋ ᴋᴛᴏ ᴛы ᴋᴩᴏʍᴇ хуᴇᴄᴏᴄᴀ?[🍒]",
"  ᴛᴇбя ᴋᴛᴏ хуᴇʍ ᴋᴀᴋ ᴨᴏʙᴏдᴏчᴋᴏʍ ᴨᴏднᴀᴛᴀᴄᴋᴀᴧ?[🍒]",
"  ᴛᴀᴋ ᴛʙᴏя жᴇ ʍᴀᴛь ᴄʙинья чᴛᴏ ᴋᴩичᴀᴧᴀ ᴨᴩи ʙхᴏдᴇ ᴨᴇниᴄᴀ?[🍒]",
"  ᴛᴀᴋ ᴋᴛᴏ ᴛᴇбя циᴋᴧичнᴏ ᴛᴀʍ ᴨᴏ ᴨᴇниᴄу ᴨᴩᴏᴨуᴄᴛиᴧ[🍒]",
"  ʙᴇɯᴀᴧᴋᴏй ᴋᴛᴏ ᴛᴇбя ᴇбᴀᴧ[🥥]",
"  ᴀ ᴄ ᴋᴀᴋиʍи ᴄᴧᴏʙᴀʍи ᴛы ᴛᴀʍ чᴧᴇнᴀ ɜᴀ щᴇᴋу ᴨᴩиняᴧ?[🥥]",
"  ᴛᴀᴋ чᴇ ᴛы уᴦᴀɯᴇннᴀя ᴨᴇɯᴋᴀ ᴄᴧᴏʙᴇᴄнᴏ ʍᴏй чᴧᴇн ᴄᴏᴄᴇɯь[🥥]",
"  ᴋᴀᴋᴏй ᴛᴀᴋᴏй ᴇщё ᴇбᴀᴩь ᴛᴇбя ᴇбᴀᴧ?[🥥]",
"  ᴛы ᴛиᴨᴏ ʍᴏᴇʍу ᴨᴇниᴄу ᴏчᴋᴏ ᴄʙᴏᴇ ᴨᴏдᴀᴩиᴧ?[🥥]",
"  ᴛы ᴨᴇᴩᴇд ɜᴇᴩᴋᴀᴧᴏʍ ᴛᴏ чᴛᴏ ᴩᴀᴄᴄᴋᴀжᴇɯь?[🥥]",
"  ʙᴄᴇ ϶ᴛᴏ ᴏбᴇᴩнуᴧᴏᴄь хуᴇʍ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʙ ᴩᴏᴛ[🥥]",
"  ᴋᴛᴏ ᴛя ᴛᴀʍ ᴇбᴀᴧ ᴩᴀᴄᴄᴋᴀжи ᴀну[🥥]",
"  ᴛᴀᴋ ϶ᴛᴏ я ᴛᴇбя ᴇбᴀᴧ ᴨᴏᴧучᴀᴇᴛᴄя?[🥥]",
"  ᴛы ᴨᴏняᴧ ᴛы ʍнᴇ ᴩᴏᴛ ᴄʙᴏй ᴨᴏдᴀᴩиᴧ нᴇ инᴀчᴇ[🥥]",
"  ᴛᴀᴋ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи яйцᴀʍи ᴨᴏ ᴇбᴀᴧу чᴛᴏ ᴄᴋᴀɜᴀнᴏ?[🥥]",
"  ну ᴨᴏняᴛнᴏ нᴀ ᴄᴇᴦᴏдня ʙᴄᴇ ϶ᴛᴏ ᴛы ᴋᴏʍу ᴛы ᴄᴏᴄᴀᴧ[🥥]",
"  ᴛᴀᴋ ϶ᴛᴏ я ᴛᴇбя ᴇбᴀᴧ чᴛᴏ ᴨᴏᴄᴧᴇ ᴨᴇниᴄᴀ?[🍭] ",
"  ᴀ ну ϶ᴛᴏ ᴛы ᴨᴏᴄᴧᴇ ᴨᴇниᴄᴀ?[🍭] ",
"  нᴇ ᴨᴏняᴧ ᴋᴛᴏ ᴛᴇбя хуᴇʍ ʙ ᴩᴏᴛ нᴀᴋᴀɜᴀᴧ?[🍭] ",
"  ʍнᴇ ᴨᴩᴏᴄиᴧи ᴨᴇᴩᴇдᴀᴛь чᴛᴏ ᴛʙᴏя ʍᴀᴛь бᴧядь ᴛуᴨᴀя чᴛᴏ ʙ хуй?[🍭] ",
"  ᴛᴀᴋ ϶ᴛᴏ ᴛы ʙ хуй жᴇ ᴩᴀᴄᴄᴋᴀɜᴀᴧ[🍭] ",
"  нᴇ инᴀчᴇ чᴇʍ ᴄᴏᴄᴇɯь, ᴀ ᴋᴏʍу?[🍭] ",
"  ᴛы ᴄʙинья нᴇ инᴀчᴇ, ᴋᴏʍу жᴏᴨу ᴏᴛдᴀᴧ ᴄʙᴏю?[🍭] ",
"  ᴄᴏᴄᴇɯь ᴦᴩᴀʍᴏᴛнᴏ ᴄ ᴋᴀᴋиʍи жᴇ ᴄᴧᴏʙᴀʍи нᴀ ϶ᴛᴏᴛ ᴩᴀɜ?[🍭] ",
"  ᴨᴏчᴇʍу ᴛы ʍнᴇ жᴏᴨу ᴄʙᴏю ᴨᴏдᴀᴩиᴧ[🍭] ",
"  ᴨᴏчᴇʍу ᴛы ᴏᴛᴄᴏᴄᴀᴧ ʍнᴇ чᴧᴇн[🍭] ",
"  ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄᴇᴛ[🍭] ",
"  ᴨᴏчᴇʍу ᴛʙᴏй ᴏᴛᴇц ᴄ ʙᴏйны ʙ цинᴋᴏʙᴏʍ ᴦᴩᴏбу ʙᴇᴩнуᴧᴄя ɸᴀᴩɯᴇʍ[🍭] ",
"  иɜ бᴀᴛи ᴛʙᴏᴇᴦᴏ ɸᴩиᴋᴀдᴇᴧьᴋи ᴋᴛᴏ ᴄдᴇᴧᴀᴧ[🥑] ",
"  ᴨᴏчᴇʍу ᴛʙᴏя ᴛуɯᴀ ᴨᴇниᴄ ᴄᴀᴋᴀᴇᴛ[🥑] ",
"  ᴛᴀᴋ ᴋᴛᴏ ᴛы ᴨᴏᴄᴧᴇ чᴧᴇнᴀ ᴋᴏᴦдᴀ ʙᴄᴇ ϶ᴛᴏ ᴛы[🥑] ",
"  ᴇᴄᴧи ᴛы ᴄᴧᴀбᴀᴋ ᴋᴛᴏ ᴛы нᴀ ᴨᴇниᴄᴇ? ʙᴄᴇ ϶ᴛᴏ ᴛʙᴏя ʍᴀᴛь[🥑] ",
"  ᴋᴏʍу ᴇщё ᴛʙᴏй ᴩᴏᴛ ᴄᴏᴄᴇᴛ я нᴇ ᴨᴏняᴧ[🥑] ",
"  нᴀ ᴄᴇᴦᴏдня у ʙᴄᴇх ʙᴄᴇ ᴛʙᴏᴇ ᴩᴏднᴏᴇ[🥑] ",
"  ᴄᴀʍᴏᴨᴩᴏʙᴏй ᴛы ᴄᴏʙᴇᴩɯиᴧ ᴄуицид [🥑] ",
"  ᴄᴀʍᴏᴨᴩᴏʙᴀ ᴧᴇᴛиᴛ ᴛᴇбᴇ жᴇ хуᴇʍ ᴨᴏ ᴧбу[🥑] ",
"  ᴋᴛᴏ ᴛя ᴛᴀʍ ᴇбᴀᴧ[🥑] ",
"  ᴋᴏʍу ᴄᴏᴄᴇɯь[🥑] ",
"  ᴨᴏчᴇʍу ᴄᴏᴄᴇɯь[🥑] ",
"  ᴛы ᴄʙинья ɜᴀчᴇʍ ᴄᴏᴄᴇɯь[🥑] ",
"  ᴛуᴛ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧи чᴇᴛʙᴇᴩᴏ и ᴋᴛᴏ ᴇщё?[🌶] ",
"  ᴨᴏчᴇʍу ᴏчᴋᴏ ᴛʙᴏᴇ нᴀ ʍᴏй чᴧᴇн ᴧᴇɜᴇᴛ бᴧяᴛь[🌶] ",
"  у ᴛᴇбя ʍᴀᴛь ᴨᴏчᴇʍу ᴛᴏ ᴨᴇниᴄ ᴄᴏᴄᴇᴛ[🌶] ",
"  ᴀᴀᴀᴀᴀ ᴛᴀᴋ ϶ᴛᴏ ᴛы ʍᴀᴛᴇᴩи ᴄʙᴏᴇй дᴀ?[🌶] ",
"  ʙᴄᴇ ᴛы ᴨᴇᴩᴇд хуᴇʍ[🌶] ",
"  яᴩᴏᴄᴛнᴏ ᴛʙᴏю ʍᴀᴛь ᴋᴛᴏ ᴇщё ᴇбᴀᴧ[🌶] ",
"  я ᴛʙᴏᴇʍу ᴏᴛцᴀ ᴦᴧᴀɜᴀ ʙыᴋᴏᴧᴏᴧ ɜᴀ ᴋᴀᴋᴏй ᴨᴩᴏᴄᴛуᴨᴏᴋ[🌶] ",
"  ᴋᴛᴏ ᴇщё ᴛᴀʍ ʍᴀᴛь ᴛᴇбᴇ ᴇбᴇᴛ[🌶] ",
"  чᴇᴇᴇᴇ ᴋᴏʍу ᴛы ᴛᴀʍ ᴄᴏᴄᴇɯь[🌶] ",
"  ᴋᴛᴏ ᴛы ᴋᴩᴏʍᴇ ᴄынᴋᴀ бᴧяди?[🌶] ",
"  ᴀ ᴇбᴀᴧ ᴛя ᴋᴛᴏ?[🌽]  ",
"  ᴀ хуй чᴇй ᴛы ᴨᴏйʍᴀᴧ ʙ ᴩᴏᴛ ᴄᴇбᴇ?[🌶] ",
"  ᴄᴧᴀбᴀᴋ ᴋᴏʍу ᴄᴏᴄᴇɯь[🌽]  ",
"  ᴨиɜду ᴛʙᴏю нᴀ чᴧᴇн нᴀʍᴏᴛᴀᴧ и ᴄᴋᴀɜᴀᴧ чᴏ[🌽]  ",
"  ʍᴀᴛь ᴛᴇбᴇ ᴇбᴀᴧ ᴨᴏчᴇʍу?[🌽]  ",
"  хуᴇʍ ᴛя ᴋᴏнᴛуɜиᴧ и чᴏ ᴇщё?[🌽]  ",
"  ᴋᴏʍу ᴛᴀʍ ᴛʙᴏᴇ ᴇбᴀᴧᴏ ᴄᴏᴄᴇᴛ[🌽]  ",
"  нᴇ ᴨᴏняᴧ ϶ᴛᴏ ᴛы ʍнᴇ ᴄᴩᴀᴋу ᴨᴏдᴀᴩиᴧ ᴄʙᴏю?[🌽]  ",
"  ну ϶ᴛᴏ ᴛʙᴏᴇʍу ᴏᴛцу ᴨᴏ ᴇбᴀᴧу ᴀ бᴀбᴋᴇ чᴏ[🌽]  ",
"  ну ϶ᴛᴏ ᴛʙᴏᴇй бᴀбᴋᴇ хуᴇʍ ᴨᴏ ᴛᴩᴀхᴇᴇ ᴀ ʍᴀʍᴇ чᴏ[🌽]  ",
"  ϶ᴛᴏ ᴛʙᴏᴇй ʍᴀʍᴇ ᴨᴏ ᴋᴧыᴛᴀᴩу хуᴇʍ[🌽]  ",
"  ᴇбᴀᴧ ᴛя хуᴇʍ ʙ щᴇᴋи ᴋᴛᴏ[🌽]  ",
"  ᴋᴏʍу ᴏчᴋᴏ ᴨᴏдᴀᴩиᴧ ᴄʙᴏᴇ нᴀ нᴏʙый ᴦᴏд[🌽]  ",
"  ᴛя ᴋᴛᴏ ᴇщё ᴇбᴀᴧ[🎂] ",
"  ᴋᴏʍу ᴄᴏᴄᴇɯь ᴛуᴛ ᴨᴩиᴧюднᴀ[🎂] ",
"  ʙ ᴨᴇнᴇᴄ ɜᴇᴩᴋᴀᴧьный чᴏ[🎂] ",
"  нᴀ ᴨᴇниᴄᴇ чᴏ[🎂] ",
"  ᴄ хуя чᴏ ᴇᴄᴧи ʙᴄᴇ ϶ᴛᴏ ᴛы[🎂] ",
"  ϶ᴛᴏ ʙ хуй ᴀ ᴏᴛᴛудᴀ ᴨᴏдʍᴇнᴏй ᴛᴇᴧ ᴄ ᴛʙᴏᴇй бᴀбᴋᴏй чᴏ[🎂] ",
"  ᴛы ʙ ᴛᴇᴧᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴏʍу ᴄᴏᴄᴇɯь[🎂] ",
"  ᴋᴛᴏ ᴛя ᴛᴀʍ ᴇбᴀᴧ ᴦᴏʙᴏᴩиɯь[🎂] ",
"  чё дᴇду ᴦᴇю[🎂] ",
"  чё ʍᴀʍᴇ ɯᴧюхᴇ[🎂] ",
"  чᴏ ᴨᴏᴄᴧᴇ ʍинᴇᴛᴀ[🎂] ",
"  чᴏ ᴨᴇᴩᴇд ʍинᴇᴛᴏʍ[🥭]",
"  чᴏ ʙᴏ ʙᴩᴇʍя ʍинᴇᴛᴀ[🥭]",
"  чё ᴄ хуᴇʍ ʙᴏ ᴩᴛу[🥭]",
"  чё ᴄ хуᴇʍ ʙ жᴏᴨᴇ[🥭]",
"  чё ᴄ хуᴇʍ ʙ нᴏɜдᴩᴇ[🥭]",
"  чᴏ ᴄ хуᴇʍ ʙ уɯᴀх[🥭]",
"  чё ᴇᴄᴧи ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ[🥭]",
"  чё ʍнᴇ ʙᴏᴏбщᴇ ʙ хуй[🥭]",
"  ᴀ ᴨᴏᴄᴧᴇ хуя чᴏ[🥭]",
"  чᴏ ᴄ хуᴇʍ ʙᴏ ᴩᴛу и жᴏᴨᴇ ᴄᴋᴀɜᴀнᴏ?[🥭]",
"  ʙᴄᴇ инициᴀᴧы ᴇбᴀᴧи ᴛᴇбя ʙ ᴩᴏᴛ и жᴏᴨу[🥭]",
"  ᴛᴀᴋ ᴄ ᴋᴀᴋиʍи ᴄᴧᴏʙᴀʍи ᴛы чᴧᴇн ᴄᴏᴄᴀᴧ[🥐] ",
"  ᴏᴛᴩицᴀниᴇ ϶ᴛᴏ хуй ᴛᴇбᴇ нᴀ ᴇбᴀᴧᴏ[🥐] ",
"  ʙᴄᴇ ᴄᴧᴏʙᴀ ɯиɸᴩ ᴏ ᴛᴏʍ чᴛᴏ ᴛы ᴏчᴇнь хᴏчᴇɯь ᴨᴏᴧучиᴛь хуᴇʍ ʙ ᴩᴏᴛ[🥐] ",
"  ᴇбᴀᴩю чᴏ[🥐] ",
"  хуᴇʍ ᴛᴇбᴇ жᴇ ʙ ᴩᴏᴛ чᴏ[🥐] ",
"  ᴀ ᴋᴏᴦдᴀ ᴛя ᴇбᴀᴧи чᴏ нᴀ жᴏᴨᴇ нᴀᴨиᴄᴀᴧи[🥐] ",
"  ᴀ бᴀбᴋᴇ ᴛʙᴏᴇй ʙ ᴦᴩᴏб чᴏ[🥐] ",
"  ᴀ бᴀбᴋᴀ ᴛʙᴏя чᴏ ᴛᴇбᴇ ᴨᴧᴇʙᴋᴏʍ иɜ ᴦᴩᴏбᴀ чᴏ[🥐] ",
"  ᴀ дᴇду ʙ хуй чᴏ[🥐] ",
"  ᴀ ᴄ хуᴇʍ ʙᴏ ᴩᴛу чᴏ ʍᴀʍᴇ ᴄʙᴏᴇй нᴀɯᴇᴨᴛᴀᴧ[🥐] ",
"  ᴀ нᴀ ᴋᴩыɯᴋᴇ дᴇдᴏʙᴏᴦᴏ ᴦᴩᴏбᴀ чᴏ ᴨиᴄᴀᴧ[🥐] ",
"  чᴏ ᴄ хуя чиᴛᴀᴧ[🥐] ",
"  ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ну и чᴏ[🥐] ",
"  ᴄᴏᴄᴀᴧ ᴛы ʙᴄᴇʍу ʍиᴩу ᴄᴏ ᴄᴧᴏʙᴀʍи[🥐] ",
"  ᴇбу ᴛя ᴛуᴛ ᴨᴩиᴧюднᴏ[🍣]",
"  чᴏ бᴀбᴋᴇ хуᴇʍ ʙᴨиɜдᴀᴋ[🍣]",
"  чᴏ ᴨᴀᴨᴇ жᴏᴨᴏй ᴨᴏ ᴇбᴀᴧу[🍣]",
"  ʙᴄᴇ ᴛʙᴏи ᴄᴧᴏʙᴀ ᴄᴋᴀɜᴋᴀ ᴀ ᴛʙᴏя ʍᴀᴛь иᴧᴧюɜия[🍣]  ",
"  чᴛᴏ ᴛы ᴄ хуяʍи ʙᴏ ᴩᴛу[🍣]  ",
"  ᴄ ɸᴀнᴛᴀɜии ʙ хуй ᴋинь ʙыдуʍᴋу ᴏᴨᴨᴏнᴇнᴛу[🍣]  ",
"  ʙᴄᴇ ᴛᴏбᴏю ᴄᴋᴀɜᴀнныᴇ ᴄᴧᴏʙᴀ будуᴛ ᴨᴇᴩᴇчиᴛᴀны ʙ хуй[🍣]  ",
"  ᴛы ᴋинᴇɯь ᴨᴇᴩᴇᴨᴩᴏʙᴏᴋᴀции нᴀ хуᴇ ʙ 3 ᴧицᴇ[🍣]  ",
"  ну ᴨᴇᴩᴇᴄᴛᴀнь дуʍᴀᴛь ᴏ ʍᴏᴇʍ хуᴇ[🍣]  ",
"  ᴛᴇбя ʙ ᴄᴛиᴧᴇ жуᴩᴀʙᴧя ᴇбᴀᴧ[🍣]  ",
"  ʍᴏй хуй ʙᴄᴇ чᴛᴏ у ᴛᴇбя ᴏᴄᴛᴀᴧᴏᴄь чᴛᴏ ᴛы ᴇʍу ᴨᴏʙᴇᴄᴛʙуᴇɯь ᴏ ᴄᴇбᴇ[🍣]  ",
"  ᴛʙᴏю ʍᴀᴛь хуᴇʍ ʙыхᴏдиᴧ чᴛᴏ ᴇй ʙ ᴨиɜду ᴋᴩᴏʍᴇ чᴧᴇнᴀ[🍍]  ",
"  ᴛʙᴏю ʍᴀᴛь нᴀ ᴋᴏᴧᴇни ᴄᴛᴀʙиᴧ хуᴇʍ чᴛᴏ ᴨᴏʙᴧᴇᴋᴧᴏ ᴛᴇбя нᴀ диᴋᴄᴀᴋинᴦ[🍍]  ",
"  ᴨᴏчᴇʍу ᴛʙᴏю ʍᴀᴛь ᴇбу[🍍]  ",
"  ᴋᴛᴏ ᴛᴀʍ ᴛя хуᴇʍ ʙ ᴩᴏᴛ ᴨᴀниɜиᴧ[🍍]  ",
"  ᴨᴩᴇᴋᴩᴀᴛи ᴄᴏᴄᴀᴛь ʍнᴇ ᴛуᴛ[🍍]  ",
"  ᴛʙᴏю ʍᴀᴛь хуᴇʍ ᴄʙᴏиʍ ᴋᴧиᴇнᴛᴀʍ ᴩᴀɜдᴀᴧ[🍍]  ",
"  ᴋᴛᴏ ᴛᴀʍ ᴋᴩᴏʍᴇ ʍᴇня нᴀ ʍᴏй чᴧᴇн ᴨᴩыᴦᴀᴇᴛ[🍍]  ",
"  ʙᴏ ʙᴄᴇх ʙᴏɜʍᴏжных ɸᴩᴀᴋᴛᴀᴧᴀх ᴩᴀɜʙᴇᴛʙᴧᴇнния жиɜни ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴇбу ᴇᴇ ʙᴄяᴋᴏ-ᴩᴀɜнᴏ[🍍]  ",
"  ᴨᴩᴏдᴏᴧжиᴛᴇᴧьнᴏᴄᴛи ʙᴏɜʍᴏжных ʙᴀᴩиᴀций жиɜни ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴨᴏᴄᴧᴇ хуя нᴇ хʙᴀᴛиᴧᴏ и ᴏнᴀ ᴏᴛᴩᴇᴋᴧᴀᴄь ᴏᴛ чᴇᴦᴏ[🍍]  ",
"  ᴄᴏᴄᴛыᴋᴏʙᴋᴀ ᴀнᴀᴧᴀ ᴛʙᴏᴇй ʍᴀʍы ᴄ ʍᴏиʍ хуᴇʍ нᴀ ᴨᴏᴧяᴩнᴏй ᴏᴩбиᴛᴇ чᴛᴏ нᴀʍ дʙᴏиʍ ᴨᴏᴋᴀɜᴀᴧᴀ[🍍] ",
"  я дᴧя ᴛʙᴏᴇй ʍᴀʍы ᴨᴏᴋᴀɜᴀᴧ ᴄᴇбя ʙᴇᴩɯиᴛᴇᴧᴇʍ ᴇᴇ ᴄудьбы и ᴄᴀʍ ᴛᴏᴦᴏ нᴇ ᴨᴏдᴏɜᴩᴇʙᴀя ᴩᴇɯиᴧ ɜᴀᴋᴏнчиᴛь ᴇᴇ бᴇᴄᴄʍыᴄᴧᴇннᴏᴇ бᴩᴇннᴏᴇ ᴄущᴇᴄᴛʙᴏʙᴀниᴇ[🍍]  ",
"  нᴀ ϶ᴛᴏй ᴨᴧᴀнᴇᴛᴇ ᴛʙᴏя ʍᴀᴛь ʍᴏй чᴧᴇн ᴄᴏᴄᴇᴛ[🍍]  ",
"  ᴛʙᴏю ʍᴀᴛь ᴛуᴛ хуᴇʍ ᴨᴇᴩᴇᴛяну нᴀᴄʍᴇᴩᴛь чᴛᴏ ʙ нᴇᴦᴏ ᴄᴋᴀɜᴀнᴏ[🍧]  ",
"  ᴛы нᴀ ᴄубᴀᴛᴏʍнᴏʍ уᴩᴏʙнᴇ ᴄᴏᴄᴀᴧ ʍᴏй ᴨᴇнᴇᴄ и ᴨᴩᴏиɜнᴏᴄиᴧ ᴋᴀᴋиᴇ ʍᴀнᴛᴩы ᴏᴛᴛудᴀ ᴇᴄᴧи ᴏни ᴨᴩᴏ ᴛʙᴏю ʍᴀᴛь[🍧]  ",
"  ᴏᴛʙᴇᴛь хуᴇʍ ʍᴏиʍ ʙ ᴄʙᴏй ᴩᴏᴛ ᴇᴄᴧи у ʙᴄᴇх ʙᴄᴇ ᴛʙᴏё ᴛᴏ чᴛᴏ ᴛы ʍнᴇ нᴀ ϶ᴛᴏ ᴄᴋᴀжᴇɯь ᴄ иᴧюɜᴏᴩнᴏʍ ʍиᴩᴇ ᴄᴋᴀɜᴏᴋ[🍧]  ",
"  ᴨᴏдᴏбиᴇ ɜᴇᴩᴋᴀᴧьнᴏᴇ ᴛʙᴏих ᴄᴧᴏʙ ᴦдᴇ ᴛʙᴏй дᴇɸ ᴀᴨᴩиᴏᴩи ᴛᴀᴋи дᴏ и ᴨᴏᴄᴧᴇ чᴧᴇнᴀ ʙ ᴛʙᴏᴇй жᴏᴨᴇ ᴩᴏднᴏй ɸᴩᴀᴋᴛᴀᴧьнᴏй нᴇ ᴄᴛᴀнᴇᴛ ничᴇʍ ᴋᴩᴏʍᴇ ᴋᴀᴋ ᴄᴋᴀɜᴋᴏй[🍧]  ",
"  я ʙ ᴛʙᴏих ᴨᴩᴏʙᴀх ᴧиɯь ɜᴇᴩᴋᴀᴧьнᴀя ʙ ᴛᴇбя иᴧᴧюɜия[🍧]  ",
"  ᴨᴏ ᴨᴩиᴋᴀɜу чᴧᴇнᴏ-бᴏᴦᴀ ᴏᴛʙᴇᴛь ᴇбᴀᴩю ʍинᴇᴛᴏʍ ᴨᴏд ᴄᴀʍᴏᴨᴩᴇдᴄᴛᴀʙᴧᴇниᴇʍ хуᴇᴄᴏᴄᴀ[🍧]  ",
"  ᴨᴀдᴏбиᴇ ᴛᴇᴩᴨиᴧиɜᴏʙᴀннᴏᴦᴏ ᴄᴏᴄящᴇᴦᴏ ᴨᴇниᴄᴀʙ у ᴛя нᴀ ᴦубᴀх ᴄᴨᴇᴩʍᴀ ᴛᴀᴋ чᴛᴏ ᴛы ᴏᴛʙᴇᴛиɯь ʍнᴇ нᴀ ϶ᴛᴏ иᴄᴛᴏᴩиᴇй хуᴇʍ ʙ ᴩᴏᴛ ᴛᴇбᴇ ᴨᴏд ᴄᴀʍᴏᴏᴨᴩᴇдᴇᴧᴇниᴇʍи ᴄ хуя ᴩᴀᴄᴄᴋᴀɜᴀʙ[🍧]  ",
"  ʙᴄᴇ ᴛы дᴏ и ᴨᴏᴄᴧᴇ ᴛы ᴨᴏд ᴄыʙᴏᴩᴏᴛᴋᴏй ᴧжи ʙᴄᴇᴦдᴀ ʙᴏ ʙᴄᴇх ᴩᴀɜных ʙᴩᴇʍᴇнᴀх ᴛы ᴨᴏд ниᴋᴏʍ иʍᴇнᴇʍ ɜʙᴀниᴇʍ ʙ ᴧицᴇ и ᴛᴇᴧᴇ ᴏᴨᴨᴏнᴇнᴛᴀ[🍧]  ",
"  ʙᴄᴇ ᴛы ᴨᴇᴩᴇд ɜᴇᴩᴋᴀᴧᴏʍ ʙᴄᴇ инициᴀᴧы ниᴋи иʍᴇнᴀ ᴄиʍʙᴏᴧы ϶ᴛᴏ чᴧᴇны ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʙ жᴏᴨу ᴇᴇ ᴩᴏдную ᴏнᴀ ʙ ᴛᴇᴧᴇ ᴛʙᴏᴇй ᴋᴩᴏʙнᴏй бᴀбᴋи и нᴇ бᴏᴧᴇᴇ[🍧]  ",
"  ᴛᴀᴋ дᴏ и ᴨᴏᴄᴧᴇ ᴄᴏɜдᴀния ʍᴇᴛᴀʙᴄᴇᴧᴇннᴏй ᴛы будучи ᴨиɜдᴀбᴏᴧᴏʍ ᴋᴇʍ ᴇщё удᴏᴄᴛᴏиᴧᴄя ᴄᴛᴀᴛь ᴇᴄᴧи ᴛы ᴄᴀʍᴏᴏᴨᴩᴇдᴇᴧиɯьᴄя ᴨᴩᴏʙᴏй ᴋᴀᴋ инᴄᴛᴩуᴋциᴇй ᴨᴏ диᴋᴄᴀᴋинᴦу чᴧᴇнᴏʙ ᴩᴀɜных ᴦᴀбᴀᴩиᴛᴏʙ[🍧]  ",
"  ʙᴄᴇᴦдᴀ ᴨᴏд ʙᴄᴇʍи ɜᴇᴩᴋᴀᴧᴀʍи ᴛʙᴏя ʍᴀᴛь ᴩᴏднᴀя ʙᴄᴇ ᴀдᴩᴇᴄᴏʙᴀннᴏ ᴇй[🍧]  ",
"  ᴛʙᴏй дᴇɸ ᴧᴏжь ʙᴄᴇ нижᴇ ʙ ᴨᴇниᴄ уᴧᴇᴛᴀᴇᴛ ᴋᴀᴋ ʙ ᴄᴋᴀɜᴏчнᴏᴇ ᴨᴏᴧᴇ ᴦдᴇ нᴀ ᴛᴩᴀʙᴇ быᴧᴀ убиᴧᴀ ᴛʙᴏя ʍᴀᴛь[🍧]  ",
"  ɜᴀдᴩᴀᴧ ᴛя хуᴇʍ[🍬]  ",
"  ᴏᴛᴄᴏᴄи[🍬] ",
"  ᴛᴀᴋ я дᴏ и ᴨᴏᴄᴧᴇ ᴄᴏɜдᴀния дᴀннᴏй ᴨᴩᴏʙᴏᴋᴀции быᴧ ʙ ᴛᴇᴧᴇ ʍᴀᴛᴇᴩи ᴛʙᴏᴇй ᴛᴏ ᴇᴄᴛь ᴨᴩᴏʙᴏᴋᴀция уᴧᴇᴛᴀᴇᴛ ʙ ᴄᴋᴀɜᴋу???[🍬]  ",
"  ᴋᴩᴏʍᴇ ʍᴇня ᴛʙᴏᴇ ᴏчᴋᴏ юɜᴀᴧᴏ ᴄᴛᴀдᴏ бᴀᴩᴀнᴏʙ и ᴋᴛᴏ ᴇщё ᴋᴩᴏʍᴇ ᴛʙᴏᴇᴦᴏ ᴏᴛцᴀ ʙ ᴩᴏᴧи их ᴨᴩᴇдʙᴏдиᴛᴇᴧя[🍬]  ",
"  ᴛᴀᴋ нᴀ ᴄᴇᴦᴏдня у ʍᴇня ʙᴄᴇ ʍᴏᴇ яɜыᴋᴏʙᴏᴇ ᴛʙᴏᴇ ᴩᴏднᴏᴇ ᴛᴏ ᴇᴄᴛь ϶ᴛᴏ ᴄᴀʍᴏʙᴋᴀч???[🍬]  ",
"  ᴛы ᴛуᴨᴏй ᴄынᴏᴋ ɯᴧюхи ᴏбъяᴄни ᴋᴀᴋ ᴛы нᴀ чᴧᴇн ʍнᴇ ᴨᴏᴨᴀᴧ[🍬] ",
"  ᴛы чᴇ нᴀ ᴨᴇниᴄᴇ ᴄᴋᴀчᴇɯь[🍬]  ",
"  хуᴇʍ ʙ ᴛя дᴏᴧбᴏᴇбᴀ бᴩыɜнуᴧ[🍬]  ",
"  ᴛы ʙᴏ ʙᴄᴇх ᴛᴇᴧᴀх ᴨᴇᴩᴄᴏнᴀжᴇй иɜ ᴛʙᴏих ᴨᴩᴏʙ чᴛᴏ дᴏ и ᴨᴏᴄᴧᴇ ᴄᴏɜдᴀния ʍᴇᴛᴀʙᴄᴇᴧᴇннᴏй быᴧи ʙыдуʍᴋᴏй ᴛᴏ ᴇᴄᴛь ᴨᴩᴏʙᴀ ᴧᴇᴛиᴛ ᴛᴇбᴇ хуᴇʍ ʙ ᴨиɜду?[🍬]  ",
"  ᴛы нᴇ бᴏᴧᴇᴇ чᴇʍ ᴄынᴏᴋ ᴨᴩᴏᴄᴛиᴛуᴛᴋи ᴇᴄᴧи ᴛы ϶ᴛᴏ ᴏнᴀ ʙ ᴇᴇ жᴇ ᴛᴇᴧᴇ и ᴄᴏɜнᴀнии ᴛᴏ ᴋᴏᴦᴏ иɜ ʙᴀᴄ я ʙ ᴩᴏᴛ ᴇбᴀᴧ[🍬]  ",
"  ᴇᴄᴧи ʙᴄᴇ ᴛы ᴛᴏ ᴋᴏʍу ᴛʙᴏй ᴩᴏᴛ ᴨᴩиᴧᴏʙчиᴧᴄя ᴄᴏᴄᴀᴛь[🍬]  ",
"  ᴛᴀᴋ ᴨᴏчᴛᴏй ᴋᴀᴋᴏй ᴛʙᴏᴇᴦᴏ ᴏᴛцᴀ ʙ ᴋᴏнʙᴇᴩᴛᴇ ᴨᴩᴀхᴏʍ ᴏᴛᴨᴩᴀʙиᴧ[🍩]  ",
"  хуᴇʍ ᴛᴇбя ᴨᴏддᴇᴩжиʙᴀᴧ ᴋᴏᴦдᴀ ᴛы ᴧᴀʍᴨᴏчᴋу ʙᴋᴩучиʙᴀᴧ бᴧᴀᴦᴏдᴀᴩи ᴇᴦᴏ[🍩]  ",
"  ʙᴄᴇ ᴄᴧᴏʙᴀ ᴛʙᴏи ϶ᴛᴏ ɯиɸᴩ ᴋᴏᴛᴏᴩый ɜнᴀчиᴛ чᴛᴏ ᴛᴇбᴇ ᴨᴏᴩᴀ ᴄᴏᴄᴀᴛь ᴨᴇниᴄ[🍩]  ",
"  ᴛʙᴏю ʍᴀᴛь нᴀ чᴧᴇн ᴄʙᴏй ʙᴇᴩхᴏʍ ɜᴀᴋинуᴧ и ᴨᴏᴋᴀᴛᴀᴧ[🍩]  ",
"  ᴨᴇᴩᴇᴄᴏᴄи ʍнᴇ ᴛуᴛ дᴏ ᴇбучᴇᴦᴏ иɜбыᴛᴋᴀ ʍᴏᴇй цᴀᴩᴄᴋᴏй ᴄᴨᴇᴩʍы[🍩] " ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)