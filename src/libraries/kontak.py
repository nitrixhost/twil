from libraries.database import Kontak

kontak = Kontak()

def insertKont(args,sid):
    param = {"category":args['category'],"telp":args['telp'],"name":args['name'],"token":sid.get('user_id')}
    kontak.insertKontak(param)
    return {"success":"ok"}

def getCategory(user):
    data = kontak.getKontakCategory({"token":user.get('user_id')})
    datas = list(data)
    if not datas:
        return {"success":"no","reason":"empty kontak"}
    else:
        for po in datas:
            yield {"name":po.get('name'),"telp":po.get('telp'),"category":po.get('category')}

def getCategorybyName(args,user):
    param = {"token":user.get('user_id'),"category":args['category']}
    data = kontak.getKontakCategory(param)
    datas = list(data)
    if not datas:
        return {"success":"no","reason":"empty kontak"}
    else:
        for po in datas:
            yield {"name":po.get('name'),"telp":po.get('telp')}