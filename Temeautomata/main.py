import wikipedia
import io

language = "ro"
wikipedia.set_lang(language)

x = input("Despre ce subiect este tema? ")

titlu = wikipedia.page(x).title
continut = wikipedia.page(x).content

content = titlu + "\n" + continut

with io.open('tema.txt' , 'w', encoding="utf-8") as f:
        f.write(content)
