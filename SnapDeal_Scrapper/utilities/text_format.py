import re


class TextFormat:

    def __init__(self):
        pass

    def format_text(self, text):

        encoded_string = text.strip().encode('utf-8')

        formated_string = re.sub('[^A-Za-z &]', '', encoded_string).replace(' ', '_').replace('&', 'and')

        return formated_string.title()