import libraries.kontak
import json

user = {"user_id":"Dez7tAYORGMyk4yWojXnoWAnfY1IAbLvDP5Ic3sKpIg"}
df = libraries.kontak.getCategory(user)
print(type(df))


