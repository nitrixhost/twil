from libraries.database import Kontak

kontak = Kontak()

def insertKont(args,sid):
    param = {"category":args['category'],"telp":args['telp'],"name":args['name'],"token":sid.get('user_id')}
    kontak.insertKontak(param)
    return {"success":"ok"}

def getCategory(user):
    data = kontak.getKontakCategory({"token":user.get('user_id')})
    datas = list(data)
    grund = []
    for po in datas:
        grun = {"name":po.get('name'),"telp":po.get('telp'),"category":po.get('category')}
        grund.append(grun)

    return grund