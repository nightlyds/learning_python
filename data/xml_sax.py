import xml.sax

class BREAKFAST_HANDLER:

    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'food':
            print("-----FOOD-----")

    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'price':
            self.price = content
        elif self.current == 'description':
            self.description = content
        elif self.current == 'calories':
            self.calories = content

    def endElement(self, name):
        if self.current == 'name':
            print('NAME: {}'.format(self.name))
        elif self.current == 'price':
            print('PRICE: {}'.format(self.price))
        elif self.current == 'description':
            print('DESCRIPTION: {}'.format(self.description))
        elif self.current == 'calories':
            print('CALORIES: {}'.format(self.calories))

        self.current = ''

handler = BREAKFAST_HANDLER()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('simple.xml')