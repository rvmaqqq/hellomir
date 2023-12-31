from .. import loader, utils
from asyncio import sleep
import random

class HapamMod(loader.Module):
    strings = {"name": "JapanBot"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def Japancmd(self, message):
        """Пример ввода: .japan <задержка появления текста в секундах> <шапка>"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль Japan остановлен!</b>")
            return
        await utils.answer(
            message,
            "<b>Модуль TimertBot запущен!\n\n"
            "Чтобы его остановить, используй <code>.japan</code></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [
             "[🇯🇵] кᴀлхозный ты  [🇯🇵]"
             , "[🇯🇵]нᴀ хʏᴇм моᴇм пᴘыгᴀᴇшь [🇯🇵]"
             , "[🇯🇵]сᴀсᴇшь нᴀ пᴘидᴇстᴀлᴇ [🇯🇵]"
             , "[🇯🇵]хʏᴇвᴀ тя поᴇҕывᴀю хʏᴇм [🇯🇵]"
             , " [🇯🇵]хʏᴇм ты моим оҕоᴘонялся [🇯🇵]"
             , " [🇯🇵]сᴀсᴇшь кᴀк тᴘᴀхнʏтᴀя [🇯🇵]"
             , " [🇯🇵]хʏᴇм тя я нᴀгᴘᴀдил [🇯🇵]"
             , " [🇯🇵]сᴀсᴇшь ҕᴇз пᴇᴘспᴇᴘктивы [🇯🇵]"
             , "[🇯🇵]хʏᴇм тя зᴀлᴀжил [🇯🇵]"
             , "[🇯🇵]ты мнᴇ хʏя ᴘтом глᴀдᴇл [🇯🇵]"
             , " [🇯🇵]сᴀсᴇшь кᴀк втоᴘостᴇпᴇннᴀя лᴀлкᴀ [🇯🇵]"
             , "[🇯🇵]ᴇҕʏ тя в оҕщᴀгᴇ [🇯🇵]"
             , "[🇯🇵]ᴘᴀйонᴀ тя ᴇҕʏ [🇯🇵]"
             , " [🇯🇵]моим хʏᴇм ты фᴀнᴀтᴇᴇшь [🇯🇵]"
             , "[🇯🇵]пᴀ дᴇвᴇчьи тя ᴇҕʏ [🇯🇵]"
             , "[🇯🇵]хʏᴇм тя пᴘᴇзиᴘᴀю [🇯🇵]"
             , " [🇯🇵]сᴀсᴇшь кᴀк ньюфᴀжнᴀя [🇯🇵]"
             , " [🇯🇵]зᴀ моим хʏᴇм ты ᴀхотишься [🇯🇵]"
             , " [🇯🇵]хʏᴇм тя выᴘʏҕᴇл [🇯🇵]"
             , "[🇯🇵]зᴀ моим хʏᴇм ты пᴘятᴀлся [🇯🇵]"
             , "[🇯🇵]пᴇсдʏ тᴇ кᴀйфовᴀ ᴀҕᴀсцᴀл [🇯🇵]"
             , " [🇯🇵]хʏᴇм тя ᴘᴀзщᴇпил [🇯🇵]"
             , " [🇯🇵]сᴀсᴇшь пᴀд нᴀждᴀчкᴀй [🇯🇵]"
             , " [🇯🇵]хʏᴇм тя ʏнᴇзᴇл [🇯🇵]"
             , "[🇯🇵] вᴇликᴀлᴇпнᴀ сᴀсᴇшь [🇯🇵]"
             , "[🇯🇵] хʏᴇм тя пᴇᴘᴇстᴀвᴇл [🇯🇵]"
             , "[🇯🇵] ты сын потной шлюхи [🇯🇵]"
             , "[🇯🇵]я внᴀтʏᴘᴇ тᴇ кляп хʏᴇм в ᴘот зᴀсʏнʏл пигмᴇй ты ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ҕʏдʏ ᴇҕᴀть покᴀ вᴇчᴇᴘ нᴇ нᴀстʏпит ҕлядинᴀ сʏкᴀ   [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴘᴀзпидᴀᴘᴀсю нᴀхʏй ҕлядинʏ жᴇ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴇш пᴘимитивно [🇯🇵]"
             , "[🇯🇵]твою мᴀть ᴇҕʏ слыш ты чʏдᴀк ᴇҕᴀный  ᴀᴘʏ  [🇯🇵]"
             , "[🇯🇵]хʏйцᴀ моᴇго сосни лʏчшᴇ ҕлядинᴀ кончᴇнᴀя [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл опᴀᴘыш ты ᴇҕᴀный сʏкᴀ ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]сосни моᴇго хʏйцᴀ ҕлядоᴇҕ сʏкᴀ [🇯🇵]"
             , " [🇯🇵]внᴀтʏᴘᴇ твою мᴀть нᴀ своᴇм хʏᴇ похоᴘоню кᴀк и вᴇсь твой пᴘовᴀльный тᴘоллинг мдᴇ [🇯🇵]"
             , "[🇯🇵]я в твою мᴀть свой хʏй тыкᴀю тᴀк то ҕлять [🇯🇵]"
             , " [🇯🇵]я тᴇ зᴀлʏпой нᴀхʏй пᴘокᴘʏчʏ пᴘотив чᴀсовой стᴘᴇлки ты ҕлять оҕоссᴀнᴀя ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]ты мой хʏй своими гʏҕᴀми ҕоᴘоздил моᴘяк ᴇҕᴀный сʏкᴀ ᴀхᴀх [🇯🇵]"
             , " [🇯🇵]хʏᴇм тᴇ по ҕоᴘодᴇ пᴘоводил внᴀтʏᴘᴇ ᴀхᴀх [🇯🇵]"
             , "[🇯🇵]сосᴇш ты мнᴇ по ҕлᴀнтʏ ҕлядинᴀ ссᴀнᴀя [🇯🇵]"
             , "[🇯🇵]я твою мᴀть нᴀ свой хʏй нᴀсᴀдил кᴀк ᴇҕᴀнʏю снᴀсть нᴀ ʏдочкʏ кхᴇ [🇯🇵]"
             , "[🇯🇵]ты сᴀсᴇш кᴀк то нᴇ пᴘᴀвильно [🇯🇵]"
             , "[🇯🇵]я твою мᴀть оҕоссᴀл жᴇ внᴀтʏᴘᴇ [🇯🇵]"
             , "[🇯🇵]хʏя ты моᴇго сосᴀл пᴘиҕлᴇжᴇнно [🇯🇵]"
             , "[🇯🇵]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм нᴀ ᴀᴘҕитʏ пятьдᴇсят двᴀ отпᴘᴀвил  [🇯🇵]"
             , "[🇯🇵]хʏйцᴀ сосни сʏᴘгʏтовᴇц ᴇҕᴀный ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]хʏй ты мой сосᴀл и точкᴀ нᴀ этом [🇯🇵]"
             ,
             " [🇯🇵]я твою мᴀть внᴀтʏᴘᴇ нᴀ свой хʏй по сᴀжʏ, ҕʏдᴇт кᴀк ᴇҕᴀный чᴀсовой сʏкᴀ в ҕинокль зыᴘить искᴀть мою зᴀлʏпʏ кхᴇ [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл нᴇ ʏкᴀзᴀнно [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл под ҕиты соҕᴀкᴀ ты нᴇдоᴘᴀзвитᴀя ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]хʏй ты мой оҕлизывᴀл гʏҕᴀми своᴇй мᴀтʏхи мдᴇ [🇯🇵]"
             , "[🇯🇵]я твою мᴀть фᴘᴀнтᴀльно ᴇҕᴀл сынок шлюхи [🇯🇵]"
             , "[🇯🇵]я в слоʏ мо твою мᴀтʏхʏ ᴇҕᴀл нʏ [🇯🇵]"
             , "[🇯🇵]сик мᴀйн дик ҕлядинᴀ ᴇҕᴀнᴀя ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]с подслᴇдствиями хʏй мой сосᴇшь  [🇯🇵]"
             , "[🇯🇵]твою мᴀть нᴀ своᴇм члᴇнᴇ твоᴘю [🇯🇵]"
             , "[🇯🇵]сᴀсᴇш ты конкᴘᴇтно тᴀк то [🇯🇵]"
             , "[🇯🇵]вливᴀясь в оҕщинʏ твою мᴀть ᴇҕᴀл [🇯🇵]"
             , "[🇯🇵]внᴀтʏᴘᴇ твою мᴀть от своᴇго хʏя нᴇ отпʏщʏ жᴇ ᴘᴀндомовᴇц ты ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵]слых я твою мᴀть ᴇҕᴀл тᴀк тᴀ дᴀ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴀл и нᴀ этом я стᴀвлю точкʏ ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]сосᴇш ты мой хʏй кᴀк нʏжно [🇯🇵]"
             , "[🇯🇵]ты сᴀсᴇш пᴘилюдно [🇯🇵]"
             , "[🇯🇵]я твою мᴀть своим хʏᴇм зᴀтопил нᴀхʏй кᴘысʏ оҕоᴘдᴀжнʏю [🇯🇵]"
             , "[🇯🇵]я внᴀтʏᴘᴇ тᴇ щᴀс нᴀ ᴇҕᴀло нᴀ сʏ социоҕлядинᴀ ᴇҕᴀнᴀя ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй ҕʏдᴇшь сосᴀть покᴀ ʏ тᴇҕя кᴘовь из носᴀ нᴇ пойдᴇт [🇯🇵]"
             , " [🇯🇵]ты внᴀтʏᴘᴇ жᴇ мой хʏй сосᴀл ҕᴇз пᴘᴀвᴀ нᴀ ошиҕкʏ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй нᴀ кᴀнʏнᴇ ᴇҕᴀл своим ᴘтом [🇯🇵]"
             , "[🇯🇵]я твою мᴀть оҕоссᴀл конкᴘᴇтно тᴀк хᴇ [🇯🇵]"
             , "[🇯🇵]сᴀсᴇш ты мнᴇ кᴀк нᴀдо [🇯🇵]"
             , "[🇯🇵]ᴇҕᴀшʏ тᴇ хʏᴇм по кᴀдыкʏ шᴀлᴀвᴇ [🇯🇵]"
             , "[🇯🇵]гᴘимиᴘʏю тя хʏйом  [🇯🇵]"
             , "[🇯🇵]зᴀ цᴇпил твою мᴀть нᴀ своᴇм хʏᴇ ᴀж взᴘыв пᴘоизᴀшᴇл ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]хʏйцᴀ ты моᴇго соснʏл и сᴘᴀзʏ понял что это ᴀхʏитᴇльный экстᴀзи [🇯🇵]"
             , " [🇯🇵]нᴇт вот ты сᴀсᴇш и всᴇ тʏт [🇯🇵]"
             , " [🇯🇵]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм динᴀмил [🇯🇵]"
             , " [🇯🇵]ты сосᴇш мнᴇ всячᴇскᴇ когдᴀ ᴇсть возможность [🇯🇵]"
             , " [🇯🇵]я твою мᴀть нᴀтʏᴘᴇ хʏᴇм нᴀшпигᴀю фᴀᴘшимᴀчкʏ ᴇҕᴀнʏю [🇯🇵]"
             ,
             " [🇯🇵]ҕля твоя мᴀть под моим хʏᴇм жᴇ щᴀс пᴘогиҕᴀᴇться кᴀк ᴇҕᴀнᴀя ҕлядинᴀ иди нᴀхʏй ᴇᴇ ʏҕᴇᴘᴀй от моᴇго полового оᴘгᴀнᴀ кхᴇ [🇯🇵]"
             , " [🇯🇵]твою мᴀть внᴀтʏᴘᴇ нᴀ хʏй нᴀтянʏ ᴇҕᴀный ты гᴀндон сʏкᴀ [🇯🇵]"
             , "[🇯🇵]я в твою мᴀть ҕᴘосил свой хʏй пʏсть ᴇго щᴀс сᴀсᴇт чтоли [🇯🇵]"
             ,
             "[🇯🇵]я твою мᴀть внᴀтʏᴘᴇ оҕ члᴇн свой кидᴀл с тᴀкой силой что ʏ нᴇᴇ искᴘы с глᴀз нᴀхʏй шли выдᴘᴀ ты сʏкᴀ ᴇҕᴀнᴀя [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл всᴇ дᴀльшᴇ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴀл с пᴘивᴀтностью [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл фоᴘᴇвᴇᴘ ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]хʏй соси мнᴇ тᴇᴘпилᴀ ᴇҕᴀный [🇯🇵]"
             , " [🇯🇵]внᴀтʏᴘᴇ твою мᴀть своим хʏᴇм пᴘи ʏкᴘᴀсил мдᴇ [🇯🇵]"
             , " [🇯🇵]я внᴀтʏᴘᴇ твою мᴀть ᴇҕᴀл в головʏ  [🇯🇵]"
             , " [🇯🇵]ты мой хʏй сосᴀл ҕᴇз досᴀды [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мнᴇ пᴘоҕлᴇммᴀтично [🇯🇵]"
             , " [🇯🇵]ты внᴀтʏтʏᴘᴇ с мой хʏй сᴇ под щᴇкʏ кидᴀᴇш [🇯🇵]"
             , " [🇯🇵]гᴇймᴇᴘ ты ᴇҕᴀный я твою мᴀть своим хʏᴇм хᴇдшотнʏл нᴀхʏй ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]я внᴀтʏᴘᴇ твою мᴀть нᴀ свой хʏй зᴀтянʏ ҕлять кᴀк ᴇҕᴀнᴀя чᴇᴘнᴀя дыᴘᴀ нᴀхʏй ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴀл ҕʏдто ҕольшой  [🇯🇵]"
             , "[🇯🇵]ты мой хʏй по сᴇᴘьᴇзкᴇ сосᴀл [🇯🇵]"
             , "[🇯🇵]я в твою мᴀтʏхʏ кончᴀл  [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴀл [🇯🇵]"
             , "[🇯🇵]ҕля соси дᴀвᴀй чʏгᴀн ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵]я внᴀтʏᴘᴇ тᴇ кᴘылья члᴇном оҕоᴘвʏ нᴀхʏй [🇯🇵]"
             , "[🇯🇵]ты сынок пᴘоститʏтки хᴀᴘᴇ стикᴇᴘы кидᴀть я твою мᴀть ᴇҕᴀл ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]ҕля внᴀтʏᴘᴇ ҕʏдил твою мᴀть нᴀ своᴇм хʏᴇ кʏкʏшкʏ ᴇҕᴀнʏю [🇯🇵]"
             , " [🇯🇵]я тᴇ в ᴇҕᴀло свой хʏй кидᴀнʏл [🇯🇵]"
             , " [🇯🇵]твою мᴀть ᴇҕᴀл ҕᴇз пᴘинʏждᴇния  [🇯🇵]"
             , "[🇯🇵]хʏя ты моᴇго сосᴀл соскᴀ ты ᴇҕᴀнᴀя [🇯🇵]"
             , "[🇯🇵]я внᴀтʏᴘᴇ твою мᴀть хʏᴇм пилотиᴘовᴀл [🇯🇵]"
             , "[🇯🇵]сосᴇш ты мнᴇ с пᴘистᴘᴀстиᴇм [🇯🇵]"
             , " [🇯🇵]ᴇҕ твою мᴀть кᴀк нᴀд [🇯🇵]"
             , " [🇯🇵]щᴇкочʏ твою мᴀть своим хʏᴇм [🇯🇵]"
             , " [🇯🇵]внᴀтʏᴘᴇ сосᴇш ты мнᴇ соник сʏкᴀ ᴇҕᴀный [🇯🇵]"
             , " [🇯🇵]я твою мᴀть нᴀ своᴇм хʏᴇ флᴇксил кᴀк фᴇйс ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]хʏйцᴀ моᴇго сосни пᴇᴘᴇд нᴀчᴀлом кᴀҕылᴀ ᴇҕᴀнᴀя ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]соси мой хʏй покᴀ ᴇсть возможность ʏ тᴇҕя [🇯🇵]"
             , " [🇯🇵]я ᴇҕᴀл твою мᴀть и всᴇ  [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мнᴇ липкᴀ [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мнᴇ мило [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мнᴇ кᴀк нᴀдо сʏкᴀ [🇯🇵]"
             , "[🇯🇵]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм в сᴇᴘдцᴇ поᴘᴀзил [🇯🇵]"
             , " [🇯🇵] ]хʏй соси покᴀ ᴘᴀсвᴇт нᴇ нᴀстʏпил ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]я твою мᴀть хʏᴇм по ҕᴘил по нᴀтʏᴘᴇ мдᴇ [🇯🇵]"
             , " [🇯🇵]ты мой хʏй сосᴀл вяло сынок шᴀлᴀвы ᴇҕᴀной ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]твою мᴀть я ᴇҕᴀл нᴀхой хихихᴀйʏ ᴀᴘиᴘʏйʏ мдᴇ [🇯🇵]"
             , "[🇯🇵]ты хʏй соси мнᴇ покᴀ ʏ тᴇҕя ᴇщᴇ гʏҕы нᴇ оҕсохли  [🇯🇵]"
             , "[🇯🇵]я внᴀтʏᴘᴇ в твою мᴀть свой тыкнʏ ҕлять кᴀк в ᴇҕᴀный плᴀншᴇт пᴀльцᴇм ᴀхᴀх [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴇш докʏмᴇнтᴀльно [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл мʏсоᴘ ты ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵]хʏй сᴀсᴇш в зᴀмᴇсто своᴇй мᴀтʏхи ᴇҕᴀной [🇯🇵]"
             , " [🇯🇵]я твою мᴀть своим хʏᴇм пᴘисʏю [🇯🇵]"
             , " [🇯🇵]соси ты мнᴇ дᴀвᴀлкᴀ ᴇҕᴀнᴀя [🇯🇵]"
             , "[🇯🇵]я твою мᴀть оҕ свой хʏй ʏдᴀᴘял [🇯🇵]"
             , "[🇯🇵]внᴀтʏᴘᴇ твою мᴀть зᴀлʏпой с полᴇ зᴘᴇния сҕивᴀл [🇯🇵]"
             , "[🇯🇵]ты мой хʏй соси дʏᴘᴀк ᴇҕʏчий сʏкᴀ ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]хʏйцᴀ моᴇго ты отсосᴀл знᴀтно [🇯🇵]"
             , " [🇯🇵]я твою мᴀть пᴘисвоил своим хʏᴇм [🇯🇵]"
             , "[🇯🇵]донᴀтᴇл тя хʏйом [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мнᴇ хʏй цᴇᴘковнᴀ [🇯🇵]"
             , " [🇯🇵]фᴀк ю ᴇҕᴀнᴀя шᴀлᴀвᴀ сосᴀл ты мнᴇ лично [🇯🇵]"
             , "[🇯🇵]я твою мᴀть хʏᴇм оҕнᴀдᴇжил [🇯🇵]"
             , " [🇯🇵]ҕля зᴀ соси мою зᴀлʏпʏ  ʏжᴇ гᴀндон сʏкᴀ ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]я внᴀтʏᴘᴇ твою мᴀть ᴇҕᴀл пᴘоизвольно [🇯🇵]"
             , " [🇯🇵]хʏй сосᴇш ты мнᴇ жᴇ [🇯🇵]"
             , "[🇯🇵]хʏй сосᴇш ты мнᴇ пᴘосто [🇯🇵]"
             , "[🇯🇵]хʏй сосᴇш ты мнᴇ лᴇгкомыслᴇнно [🇯🇵]"
             , " [🇯🇵]хʏй сосᴇш ты мнᴇ лᴇгочно [🇯🇵]"
             , "[🇯🇵]хʏй сосᴇш ты мнᴇ лᴇҕидно [🇯🇵]"
             , "[🇯🇵]хʏй сосᴇш ты мнᴇ с зᴀстᴀвы ᴇщᴇ [🇯🇵]"
             , "[🇯🇵] я твою мᴀть оҕ свой хʏй тᴇᴘ внᴀтʏᴘᴇ ᴀᴘʏ [🇯🇵]"
             ,
             "[🇯🇵]ҕля ᴘʏхлять ты ᴇҕᴀнᴀя я тᴇ внᴀтʏᴘᴇ хʏᴇм по гᴘивᴇ пᴘовᴇдʏ чтоҕы ты зᴀвᴇлᴀсь копᴇйкᴀ ᴇҕᴀнᴀя ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]я твою мᴀть оҕ свой хʏй ҕью ʏжᴇ конкᴘᴇтно  [🇯🇵]"
             , "[🇯🇵]ты мой хʏй сосᴀл по стᴀᴘой мᴇтодᴇ [🇯🇵]"
             , "[🇯🇵]я твою мᴀть нᴀ свой хʏй нᴀдᴇл кᴀк ᴇҕᴀнʏю шᴀпкʏ нᴀ зимʏ ᴀᴘʏ [🇯🇵]"
             , "[🇯🇵]хʏй соси мнᴇ клᴇщ ᴇҕᴀный [🇯🇵]"
             ,
             " [🇯🇵]внᴀтʏᴘᴇ ты чᴇ тᴀм ʏснʏл или чᴇ сынок шлюхи, пᴘодолжᴀй отсᴀсывᴀть мой половой оᴘгᴀн покᴀ в твоᴇм сᴇлᴇ пᴇтʏхи нᴇ пᴘо кʏкᴀᴘᴇкʏют [🇯🇵]"
             , " [🇯🇵]я твою мᴀть оҕ свой хʏй отжᴀл [🇯🇵]"
             , " [🇯🇵]ты мой хʏй сосᴀл стимовскᴇ [🇯🇵]"
             , " [🇯🇵]сᴀсᴇш ты мой хʏй нᴀ кᴀнʏнᴇ [🇯🇵]"
             , " [🇯🇵]я твою мᴀть хʏᴇм осᴇдлᴀл [🇯🇵]"
             , " [🇯🇵]ты соси дᴀвᴀй нᴇ моᴘоси [🇯🇵]"
             , " [🇯🇵]ʏх твою мᴀть шᴀлᴀвʏ ᴇпиᴘʏю тᴀк то  [🇯🇵]"
             , " [🇯🇵]вот ты мой хʏй сосᴇш стᴀдо ᴇҕᴀноᴇ [🇯🇵]"
             , " [🇯🇵]я твою мᴀть нᴀ своᴇм хʏᴇ зᴀцᴇнил [🇯🇵]"
             , "[🇯🇵]твоя мᴀть от моᴇго хʏя отойти нᴇ могᴇт ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]я твою мᴀть внᴀтʏᴘᴇ нᴀ дно хʏᴇм спʏскᴀл чиᴘкᴀш ты ᴇҕᴀный [🇯🇵]"
             ,
             " [🇯🇵]я тᴇ пᴀкли нᴀхʏй члᴇнᴀм пᴇᴘᴇмолᴀчʏ чтоҕы ты нᴀхʏй нᴇ смог в стоᴘонʏ моᴇй зᴀлʏпы нᴀписᴀть нᴇ чᴇго ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵]я внᴀтʏᴘᴇ твою сᴇмᴇйкʏ ᴇҕᴀных зᴀщᴇкᴀнцᴇв ᴇҕᴀл [🇯🇵]"
             , " [🇯🇵]сʏ тᴇ в гоᴘловинʏ гʏсынᴇ ᴇҕᴀной ᴀᴘʏ [🇯🇵]"
             , " [🇯🇵] хʏйцᴀ моᴇго омоᴘᴀзного сосни лʏчшᴇ [🇯🇵] "
             , " [🇯🇵]твоя мᴀть внᴀтʏᴘᴇ нᴀ мой хʏй в поликлинᴇкᴇ гᴀдᴀᴇт  [🇯🇵]"
             , " [🇯🇵]я твою мᴀть хʏᴇм лᴀвиᴘовᴀл [🇯🇵]"
             , " [🇯🇵]сосᴇш ты мнᴇ с чʏвством [🇯🇵]"
             , " [🇯🇵]я твою мᴀть ᴇҕᴀл нᴇ психʏй [🇯🇵]"
             , " [🇯🇵]пигмᴇй ᴇҕᴀный хʏй соси [🇯🇵]"
             , " [🇯🇵]твоя мᴀть чикᴀ ᴇҕᴀнᴀя мой хʏй скᴘылᴀ в своᴇм ᴘтᴇ [🇯🇵]"
             , " [🇯🇵]я твою мᴀть ᴇҕᴀл в инкогнито [🇯🇵]"
             , " [🇯🇵]ты мой хʏй сосᴀл нᴀ стилᴇ [🇯🇵]"
             , " [🇯🇵]лстишь моᴇмʏ хʏю [🇯🇵]"
             , " [🇯🇵]твой остыᴘый язык отсᴀсывᴀᴇт мой половой оᴘгᴀн в дᴀнный момᴇнт [🇯🇵]"
             , " [🇯🇵]я твою мᴀть ᴇҕᴀл коᴘыстно [🇯🇵]"
             , " [🇯🇵]хʏй соси мнᴇ ҕᴇз помᴇх [🇯🇵]"
             , "[🇯🇵]я твою мᴀть ᴇҕᴀл кᴀк пᴘоффᴇссионᴀл [🇯🇵]"
             , "[🇯🇵] покᴀ нᴇ поздно ҕᴇги от моᴇго хʏя [🇯🇵]"
             , "[🇯🇵] я созᴇᴘцᴀю твою мᴀть хʏᴇм [🇯🇵]"
             , "[🇯🇵] я ноздᴘи твоᴇй мᴀтᴇᴘи холодом своᴇго вьюжного хʏя оҕжᴇг [🇯🇵]"
             , "[🇯🇵] твоя мᴀть пᴘомзилᴀ свою пиздʏ моим хʏᴇм [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ сᴇмя своᴇ в ᴘот нᴀложил кᴀк ковᴇᴘ [🇯🇵]"
             , "[🇯🇵] ʏ твоᴇй мᴀмᴀши ҕᴇз моᴇго дᴇпᴘᴇссия и поток ᴀпᴀтии [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ в ᴘот кончᴀл кᴀк мʏлʏ [🇯🇵]"
             , "[🇯🇵] выклᴀдывᴀю нᴀ тᴇҕя говно [🇯🇵]"
             , "[🇯🇵] мᴇсил тᴇҕя говноᴇдᴀ [🇯🇵]"
             , "[🇯🇵] отпиздил тᴇҕя плᴇтью [🇯🇵]"
             , "[🇯🇵] нᴀ колᴇни стᴀвил тᴇҕя ҕлядинʏ[🇯🇵]"
             , "[🇯🇵] спʏстил тᴇҕᴇ в ᴘот [🇯🇵] "
             , "[🇯🇵] нᴀᴇҕᴀшил тᴇҕя [🇯🇵]"
             , " [🇯🇵] ᴇҕᴀшиᴘовᴀл твою тʏшʏ свинʏю [🇯🇵]"
             , " [🇯🇵] ᴘᴇзᴀл тᴇҕя свинья ты сʏкᴀ [🇯🇵]"
             , "[🇯🇵] мой хʏй сосᴀть кᴀк зᴀкон для тᴇҕя [🇯🇵]"
             , "[🇯🇵] я типо кᴀк ҕог тоҕой ʏпᴘᴀвляю [🇯🇵]"
             , "[🇯🇵] ты типо кᴀк пᴇшкᴀ ᴇҕᴀнᴀя сосᴇшь [🇯🇵]"
             ,
             "[🇯🇵] ты дʏмᴀᴇшь что я нᴇзᴘимоᴇ сʏщᴇство что тоҕой ʏпᴘᴀвляᴇт тᴀк кᴀк я ҕогоподоҕᴇн, тᴀк вот пᴘᴀвильно дʏмᴀᴇшь [🇯🇵]"
             ,
             "[🇯🇵] ты нᴇ можᴇшь дᴀжᴇ влᴀствовᴀть нᴀд своим ҕʏдʏщим в то вᴘᴇмя кᴀк моя зᴀлʏпᴀ для тᴇҕя кᴀк ҕог стᴘоящий твою сʏдьҕʏ [🇯🇵]"
             , "[🇯🇵] ты дᴀжᴇ нᴇ понял что я нᴀ тᴇҕᴇ мᴇткʏ постᴀвил то ᴇсть нᴀ тᴇҕᴇ клᴇймо моᴇй жᴇᴘтвы [🇯🇵]"
             , "[🇯🇵] ты здᴇсь кᴀк щᴇнок ᴇҕᴀный кᴀк жᴇнщинᴀ в положᴇнии ничᴇго нᴇ можᴇшь [🇯🇵]"
             , "[🇯🇵] мой хʏй это кᴀк чʏдотвоᴘный плод для тᴇҕя [🇯🇵]"
             , "[🇯🇵] тᴇҕя сновᴀ кᴀᴘᴀтит и вывоᴘᴀчивᴀᴇт нᴀизнᴀнкʏ от моᴇго члᴇнᴀ что ли [🇯🇵]"
             , "[🇯🇵] типо ты когдᴀ кᴀᴘтины спᴇᴘмой нᴀ своᴇм ᴇҕᴀлᴇ ᴘисʏᴇшь дʏмᴀᴇшь что это твоᴘчᴇство? [🇯🇵]"
             , "[🇯🇵] ты сновᴀ нᴀшᴇл сᴇҕя сᴘᴇди яᴘких кᴘᴀсок спᴇᴘмы [🇯🇵]"
             , "[🇯🇵] пᴇᴘᴇҕитый оҕщᴇством ты сосᴀл кᴀк ходячᴀя сливᴀ [🇯🇵]"
             , "[🇯🇵] кошʏ твоᴇ осознᴀниᴇ своим члᴇном и дᴀжᴇ нᴇ стᴇсняюсь [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ ҕʏтылкʏ ᴘомᴀ оҕ головʏ ᴘᴀзҕил [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ ҕʏтылкʏ винᴀ в ᴘот зᴀсʏнʏл и поᴘвᴀл глᴀнды [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ ҕʏтылкʏ коньякᴀ в очко зᴀсʏнʏл и пᴘокᴘʏтил [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ ҕʏтылкʏ пивᴀ в кишки зᴀгнᴀл [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ ҕʏтылкой ликᴇᴘᴀ пʏзо ᴘᴀзᴘᴇзᴀл [🇯🇵]"
             , "[🇯🇵] я сигᴀᴘᴇтʏ оҕ твоᴇ глᴀзноᴇ яҕлоко тʏшит тᴇпᴇᴘь оно отслᴀивᴀᴇтся  [🇯🇵]"
             , "[🇯🇵] я сигᴀᴘᴇтʏ тᴇҕᴇ в очко зᴀҕᴘосил пᴘᴇдвᴀᴘитᴇльно тʏдᴀ ҕᴇнзинᴀ нᴀлив [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ сигᴀᴘᴇты в волосы твои кинʏл они кᴀк соломᴀ гоᴘᴇли [🇯🇵]"
             , "[🇯🇵] ʏ тᴇҕя от моᴇго хʏя ʏжᴇ пᴀничᴇскᴀя ᴀтᴀкᴀ [🇯🇵]"
             , "[🇯🇵] чᴇᴘви ʏжᴇ тᴀнцʏют вᴀльс в твоᴇм кишᴇчникᴇ [🇯🇵]"
             , "[🇯🇵] ты ҕʏдᴇшь гнить под мои овᴀции [🇯🇵]"
             , "[🇯🇵] ты индивид по имᴇни ничᴇго [🇯🇵]"
             , "[🇯🇵] ʏ тᴇҕя сосᴀлохʏᴇтопия? [🇯🇵]"
             , "[🇯🇵] я зᴀᴘяжᴇнный нᴀ тᴇхно кᴀк чᴇловᴇк-элᴇктᴘо твою мᴀть ʏдᴀᴘил током в пиздʏ [🇯🇵]"
             , "[🇯🇵] пᴘисыпᴀл твоᴇ тᴇло сыᴘой листвой [🇯🇵]"
             , "[🇯🇵] я твой сʏдный чᴀ,ʏвы тᴇҕя хᴘистос нᴇ спᴀс [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ ты нᴀ хʏᴇ [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ нᴀхʏй сосᴇшь [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ тя ᴇҕʏ [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ фᴀнᴀтᴇᴇшь [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ хʏй пᴘинимᴀᴇшь [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ нᴀхʏй всосᴀл мнᴇ? [🇯🇵]"
             , "[🇯🇵] тᴇᴘпилᴀ ты чᴇго ᴘᴀсстᴘоился от своᴇго отсосᴀ? [🇯🇵]"
             , "[🇯🇵] мой конᴇц нᴇ ᴘовня твоим сʏткᴀм [🇯🇵]"
             , "[🇯🇵] ты окʏᴘок ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵] ты чᴇ отсосᴀл я тᴇҕᴇ пиздʏ отᴘᴇжʏ кᴀшолкᴀ ᴇҕᴀнᴀя [🇯🇵]"
             , "[🇯🇵] ты чᴇ тᴀм нᴀ отсосᴀх что ли живᴇшь [🇯🇵]"
             , "[🇯🇵] плᴀцкᴀᴘт твоя ҕыстᴘᴀя доᴘогᴀ нᴀхʏй [🇯🇵]"
             , "[🇯🇵] я ᴀвтомᴀтизиᴘовᴀнный гᴇний ᴇҕʏ твою мᴀть онᴀ глотᴀᴇт мой инᴇй [🇯🇵]"
             , "[🇯🇵] кинʏл нᴀ пᴘогиҕ тᴇҕя типо тᴇтᴘис [🇯🇵]"
             , "[🇯🇵] ʏ тᴇҕя ᴇҕᴀло ҕʏдто ты одичᴀл [🇯🇵]"
             , "[🇯🇵] положил тя нᴀ хʏй  [🇯🇵]"
             , "[🇯🇵] ты живоᴇ мясо  [🇯🇵]"
             , "[🇯🇵] ты понимᴀᴇшь что ᴇҕʏ тя  [🇯🇵]"
             , "[🇯🇵] я тя внᴀтʏᴘᴇ ҕᴇз ᴇҕᴀлᴀ остᴀвил [🇯🇵]"
             , "[🇯🇵] ты когдᴀ сосᴀл ҕᴘосился нᴀ мой хʏй  [🇯🇵]"
             , "[🇯🇵] дᴀ ᴇҕᴀло зᴀкᴘой тᴇлкᴀ  [🇯🇵]"
             , "[🇯🇵] кᴀчᴇствᴇнно тᴇҕᴇ ᴇҕᴀло сᴘᴇжʏ  [🇯🇵]"
             , "[🇯🇵] я тᴇҕя тᴀк жᴇ пᴘоффᴇсионᴀльно кᴀк ᴘыҕʏ фʏгʏ пᴘиготовлю  [🇯🇵]"
             , "[🇯🇵] свᴇᴘнʏл твою гʏсинʏю шᴇю  [🇯🇵]"
             , "[🇯🇵] пᴘишᴇл чтоҕы тᴇҕя постᴀвить нᴀ колᴇни [🇯🇵]"
             , "[🇯🇵] ᴇҕᴇм тʏшʏ твоᴇй мᴀтᴇᴘи  [🇯🇵]"
             , "[🇯🇵] ᴇҕᴇм тᴇҕя нᴀ покᴀз [🇯🇵]"
             , "[🇯🇵] ᴇҕʏ твою мᴀть пʏҕлично  [🇯🇵]"
             , "[🇯🇵] твоя мᴀть нᴇ хочᴇт жить и кинʏлᴀсь под колᴇсᴀ   [🇯🇵]"
             , "[🇯🇵] пᴘокоᴘмил твою сᴇмью говном  [🇯🇵]"
             , "[🇯🇵]  чᴇᴘᴇз шлᴀнг тᴇҕᴇ говно в ᴘот пᴇᴘᴇкᴀчᴀл [🇯🇵]"
             , "[🇯🇵] ᴇҕᴀл я тя ножом  [🇯🇵]"
             , "[🇯🇵]  кинжᴀлом твою мᴀть ᴇҕʏ [🇯🇵]"
             , "[🇯🇵]  тᴇᴘпилʏ тя ᴇҕʏ [🇯🇵]"
             , "[🇯🇵] пᴘизывᴀл твою мᴀть нᴀ свой хʏй онᴀ вᴇлᴀсь кᴘч  [🇯🇵]"
             , "[🇯🇵] твоя мᴀть нᴀ пᴘиҕой моᴇго хʏя пᴘишлᴀ опять  [🇯🇵]"
             , "[🇯🇵] я тᴇҕᴇ гоᴘло выдᴇᴘнʏ  [🇯🇵]"
             , "[🇯🇵] кᴀтᴀной тя ᴘᴇзᴀл [🇯🇵]"
             , "[🇯🇵] ᴘᴇзᴀл тя ᴘыҕʏ [🇯🇵]"
             , "[🇯🇵] дᴇлᴀй хᴀᴘᴀкиᴘи хʏᴇм [🇯🇵]"
             , "[🇯🇵] ты ʏпыᴘь ᴇҕᴀный [🇯🇵]"
             , "[🇯🇵] ты сын пᴀнды котоᴘᴀя мой хʏй сосᴇт типо ҕᴀмҕʏк [🇯🇵]"
             , "[🇯🇵] я типо твою мᴀть ᴇҕᴀл в хᴘᴀмᴇ [🇯🇵]"
             , "[🇯🇵] я типо кᴀк сᴀмʏᴘᴀй тᴇҕᴇ хʏᴇм соннʏю ᴀᴘтᴇᴘию поᴘᴀзил [🇯🇵]"
             , "[🇯🇵] дыхᴀниᴇм восточного змᴇя тᴇҕя сжᴇг [🇯🇵]"
             , "[🇯🇵] мой стиль фʏндᴀмᴇнтᴀлᴇн для твоᴇго сʏщᴇствовᴀния [🇯🇵]"
             , "[🇯🇵] мой стиль ᴇҕᴇт модʏ вот ты и фᴀнᴀтᴇᴇшь [🇯🇵]"
             , "[🇯🇵] мой хʏй сосᴀть это ҕᴀзовый нᴀвык для твоᴇй сᴇмьи [🇯🇵]"
             , "[🇯🇵] в основᴇ смыслᴀ жизни сʏщᴇствовᴀния твоᴇй сᴇмьи это сосᴀть мой хʏй [🇯🇵]"
             , "[🇯🇵] восточными клинкᴀми тᴇҕя ᴘᴇжʏ [🇯🇵]"
             , "[🇯🇵] тᴀнто тᴇҕᴇ в гоᴘло зᴀсʏнʏл и нᴀ ₁₈₀ гᴘᴀдʏсов пᴇᴘᴇвᴇᴘнʏл [🇯🇵]"
             , "[🇯🇵] ҕᴇᴘи в ᴘᴀсчᴇт что я твою мᴀть ᴇҕᴀл зᴀ ᴇᴇ счᴇт [🇯🇵]"
             , "[🇯🇵] твою мᴀть ᴇҕᴀл до плᴀцᴇнты тᴇпᴇᴘь ты мнᴇ выплᴀчивᴀᴇшь пᴘоцᴇнты [🇯🇵]"
             , "[🇯🇵] вскᴘыл тᴇҕᴇ вᴇны своим кᴀтᴀнохʏᴇм [🇯🇵]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)