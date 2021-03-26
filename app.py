import modules


def gen_user_report():

    scrapping = modules.Scraping
    validation = modules.Validation
    make_doc = modules.Make_doc

    github_link = input('Cole aqui o link do seu perfil no Github: ')

    if validation.url_is_secure(github_link) and validation.url_is_valid(github_link):

        html = scrapping.get_HTML(github_link)
        profile_pic = scrapping.get_profile_picture(html, ".avatar-user")
        username = scrapping.get_username(html, ".p-name")    
        make_doc.create_canvas()
        make_doc.write_doc(profile_pic, username, github_link)
        print('Document created! ')
        return 
        
    
    print(f'parece que a url inserida não é válida. verifique se escreveu seu link corretamente -->"{github_link}" ')

gen_user_report()
