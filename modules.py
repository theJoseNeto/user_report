from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import requests


class Scraping:

    def get_HTML(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        return html

    def get_profile_picture(html, selector):
        image = html.select_one(selector)  # ".avatar-user"
        image = image.get('src')
        return image

    def get_username(html, selector):
        user = html.select_one(selector).text  # ".p-name"
        return user

    def get_repositories(link_repositories):
        list_repos = []
        response = requests.get(link_repositories)
        soup = BeautifulSoup(response.text, 'html.parser')
        main = soup.find(id="user-repositories-list")
        all_repos = main.find_all('li')

        for v in all_repos:
            title_project = v.find(class_='wb-break-all').text
            link_project = v.find('a')['href']
            list_repos.insert(-1,
                              f"{title_project}. Link: https://github.com{link_project}")

        return list_repos


class Validation:

    def url_is_secure(url, secure = True):
        if not 'https://' in url:
            secure = False               
        return secure

    def url_is_valid(url, valid = True):
        if not 'https://github.com/' in url:
           valid = False
        return valid



class Make_doc:

    def create_canvas():
        pdf = canvas.Canvas('example.pdf')
        return pdf

    def config_font(pdf_file):
        pdf_file.setFont('Helvetica', 11)
        return

    def get_repos_and_write_in_pdf(
            pdf,
            link_to_repositories):
        y = 500
        count = 0
        list_repos = Scraping.get_repositories(f"{link_to_repositories}?tab=repositories")
        while count < len(list_repos):
            y -= 50
            doc = pdf.drawString(0, y, list_repos[count])
            count += 1
        return

    def write_doc(avatar, username, repos):

        pdf = Make_doc.create_canvas()
        pdf.setTitle('User report taken from github account')
        Make_doc.config_font(pdf)
        pdf.drawImage(avatar, 30, 700, 80, 80)
        pdf.drawString(0, 500, username)
        # repositories
        Make_doc.get_repos_and_write_in_pdf(pdf, repos)
        pdf.save()

