#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" spellchecker """
from trie import Trie


class Spellchecker():
    """ class spellchecker, main program """

    def __init__(self):
        """ctor"""
        self.set_trie('tiny_dictionary.txt')

    def set_trie(self, filename):
        """ sets up new trie object """
        data = self.read_file(filename)
        if isinstance(data, list):
            self.trie = Trie()
            for word in data:
                self.trie.insert(word)

    def get_list(self):
        """ returns list """
        return self.trie.get_trie_list()

    # def clear_child(self):
    #     """ clears trie """
    #     self.trie = None

    @staticmethod
    def read_file(filename):
        """ returns file content in list - TEST """
        try:
            with open(filename) as file:
                data = file.read()
                return data.split('\n')
        except FileNotFoundError:
            print('Det finns ingen fil som heter "{}".'.format(filename))

    def search_word(self):
        """ serch method"""
        print('**************************************\n')
        print('Sök ord')
        search_string = input('>>>').lower()
        if self.trie.get(search_string):
            print('Ordet "{}" är rätt stavat.'.format(search_string))
        else:
            print('Du har stavat fel på "{}"/finns ej'.format(search_string))

    @staticmethod
    def valid_file(file_int, files):
        """ checks valid file """
        return file_int <= len(files) and file_int > 0

    def change_file(self):
        """ changes file and create new trie"""
        print('**************************************\n')
        print('Byt fil\n\nTillgängliga filer (skriv en siffra):')
        files = ['apa.txt', 'tiny_dictionary.txt', 'dictionary.txt']
        for idx, f in enumerate(files):
            print(idx+1, f)
        print('\n')
        try:
            filename = int(input('>>> '))
            if self.valid_file(filename, files):
                # self.clear_child()
                self.set_trie(files[filename-1])
            else:
                print('Felaktigt filnummer')
        except ValueError:
            print('Ange en siffra!')

    def print_all(self):
        """ prints all """
        # for word in self.trie.get_trie_list():
        #     print(word)
        self.trie.print_trie_fast()

    @staticmethod
    def _print_prefix(res):
        """ helper method """
        string = ''
        count = 0
        for word in res:
            string += word + '\n'
            count += 1
            if count >= 10:
                return string
        return string

    @staticmethod
    def quit(string):
        """ bool for check if quit is in search string """
        if len(string) >= 4:
            if string[-4:] == 'quit':
                return True
        return False

    def prefix(self):
        """ prefix """
        print('Skriv minst tre bokstäver. Avsluta med "quit"')
        search = ''
        counter = 1
        while True:
            search += input('\nAnge sökord: {}'.format(search))
            if len(search) >= 3 and counter >= 1:
                answer = self.trie.find_prefix(search)
                counter += 1
                if self.quit(search):
                    break
                elif answer:
                    print(self._print_prefix(answer))
                else:
                    print('Inga resultat för {}'.format(search))

            # print('\nDu sökte på {}'.format(search))

    def main(self):
        """ program looop """
        run = True
        while run:
            print(self.menu())
            choice = input('\n>>>')
            if choice == '1':
                self.search_word()
            if choice == '2':
                self.prefix()
            if choice == '3':
                self.change_file()
            if choice == '4':
                self.print_all()
            if choice == '5':
                run = False
                print('Ok, hej svejs!')

    @staticmethod
    def menu():
        """ menu content """
        return """
1. Sök ord
2. Prefixsökning
3. Byt ordlista (fil)
4. Skriv ut alla ord.
5. Avsluta
        """


if __name__ == "__main__":
    s = Spellchecker()
    s.main()
