import urllib.request
import re
import read_menu


def open_allrecipes(menu_item):
    recipe_search = menu_item
    recipe_search_updated = "https://www.allrecipes.com/search/results/?search=" + recipe_search.replace(" ", "+")
    f = urllib.request.urlopen(recipe_search_updated)
    data = f.read().decode()

    return data


def open_recipe_from_search_page(data):
    search_for_string = 'class="card__titleLink manual-link-behavior elementFont__title margin-8-bottom"'
    the_url_should_be_in_here = re.compile(r'<a class="card__titleLink manual-link-behavior elementFont__titleLink '
                                           r'margin-8-bottom"\n\s*.*\n\s*href=(.*)\n[^>]*')
    url = re.search(the_url_should_be_in_here, data)
    url = re.findall(the_url_should_be_in_here, url.group(0))
    if url is not None:
        return url
    return "no matching recipe"


def collect_menu_recipes():
    menu = read_menu.read_menu("Menu.xlsx", "Menu1")
    recipes = []
    for menu_item in menu:
        recipes.append(open_recipe_from_search_page(open_allrecipes(menu_item)))
    return recipes


