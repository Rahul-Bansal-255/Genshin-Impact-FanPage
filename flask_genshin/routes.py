from flask import render_template, url_for
from flask_genshin import app
from flask_genshin.utils import pic_name_list

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/wallpapers')
def wallpapers():
    return render_template('wallpapers.html')

@app.route('/characters')
def characters():
    
    pic_list = pic_name_list('genshin_chars/')
    char_names = list()
    for i in range(0, len(pic_list)):
        char_names.append((pic_list[i].split('_'))[1])

    return render_template('characters.html', pic_list=pic_list, char_names=char_names, len=len)

@app.route('/weapons')
def weapons():

    swords_pic = pic_name_list('genshin_weapons/swords')
    books_pic = pic_name_list('genshin_weapons/books')
    bows_pic = pic_name_list('genshin_weapons/bows')
    claymore_pic = pic_name_list('genshin_weapons/claymore')
    polearm_pic = pic_name_list('genshin_weapons/polearm')

    return render_template('weapons.html', swords_pic=swords_pic, books_pic=books_pic, bows_pic=bows_pic, claymore_pic=claymore_pic, polearm_pic=polearm_pic)