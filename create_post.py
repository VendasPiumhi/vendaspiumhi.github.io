# -*- coding:utf8 -*-
import os,datetime
from pathlib import Path
from shutil import copyfile

email = input("Email ~> ")
vendedor = input("Name ~> ")
preço = float(input("Price ~> "))
fotos_d = input("Images directory ~> ")
post_name = input("Post name ~> ")
title = input("Title ~> ")
category = input("Category ~> ")
number = input("Number ~> ")
used    = input("Used ~> ")

fotos_p = []

def fotos():
    x = Path(f"assets/img/{email}")
    if not x.exists(): x.mkdir()
    fotos = list(Path(fotos_d).glob("*"))
    print(fotos)

    for foto in fotos:
        f_name = foto.name
        f_path = f"assets/img/{email}/" + foto.name
        f = foto.open("rb").read()
        open(f_path, "wb").write(f)
        fotos_p.append(f_path)

# [{f"'{i}', " for i in fotos_p}]
if __name__ == "__main__":
    fotos()

    post = \
f"""---
layout: post
title: "{title}"
date: {str(datetime.datetime.now()).split('.')[0] + ' -0300'}
categories: {category}
author: {vendedor}

fotos: {str(fotos_p)}
preco: "R${preço}"
email: "{email}"
numero: "{number}"
usado: "{used}"
---

    """

    with open(f"_posts/{post_name}","w") as fd:
        fd.write(post)
        print("Success")