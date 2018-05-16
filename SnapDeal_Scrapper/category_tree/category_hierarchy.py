from redis_queue import RedisQueue
from get_request import GetRequest
from constants import ROOT_URL
from utilities.text_format import TextFormat


class HierarchyTree:

    def __init__(self):
        pass

    def find_category_name(self, div_container):
        name_container = div_container.find('div', {'class': 'SmBox_Head'})
        if name_container:
            txt_format_obj = TextFormat()
            return txt_format_obj.format_text(name_container.text)

    def find_subcategories(self, div_container):
        sub_category_contaienrs  = div_container.findAll('div', {'class': 'SMSubCat'})
        if len(sub_category_contaienrs) > 0 :
            for sub_category_contaienr in sub_category_contaienrs:
                view_more = sub_category_contaienr.find('div', {'class': 'morelink'})
                if view_more:
                    txt_format_obj = TextFormat()
                    sub_category_link = view_more.a['href']
                    sub_category_name = txt_format_obj.format_text(sub_category_contaienr.findAll('li')[0].text)
                    return sub_category_name, sub_category_link
                # ToDO find links when there is no view more button

    def find_first_level(self):
        request_obj = GetRequest()

        request_content = request_obj.get_content(ROOT_URL)

        div_containers = request_content.findAll('div')

        for div_container in div_containers:
            # print div_container.prettify()
            try:
                if 'Tab' in div_container['id']:
                    category_name = self.find_category_name(div_container)
                    if category_name:
                        pass

            except KeyError:
                # print 'in except'
                pass

    def find_till_leaf_level(self):
        pass

k = HierarchyTree()

k.find_first_level()