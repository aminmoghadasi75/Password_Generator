"""
Password Generator Module

This module provides different classes for generating passwords based on specific criteria.

Classes:
- PasswordGenerator (ABC): Abstract base class for password generators.
- PinPassword: Generates a numeric PIN password.
- RandomPassword: Generates a random alphanumeric password with optional inclusion of numbers and symbols.
- MemorablePassword: Generates a memorable password using words from a vocabulary.

Usage:
You can instantiate an object of the desired password generator class and call the generate() method to get a password.

Example:
    p_obj = MemorablePassword(num_of_words=5, separator='**', capitalization=True)
    generated_password = p_obj.generate()
    print(generated_password)
"""
import random
import string
from abc import ABC, abstractclassmethod

import nltk
import numpy as np


class PasswordGenerator(ABC):
    @abstractclassmethod
    def generate(self):
        """Abstract method to be implemented by subclasses for password generation."""
        pass


class PinPassword(PasswordGenerator):
    def __init__(self, length: int = 8):
        """PinPassword class generates a numeric PIN password.

        :param length: Length of the PIN password, defaults to 8
        :type length: int, optional
        """
        self.length = length

    def generate(self)-> int:
        """Generates a PIN password."""
        return int(''.join(map(str,np.random.randint(0, 10, size= self.length))))


class RandomPassword(PasswordGenerator):
    def __init__(self, length: int = 8, *, include_numbers: bool = False , include_symbols: bool = False):
        """__init__ Generating a random password.

        RandomPassword class generates a random alphanumeric password.

        :param length: Length of the password, defaults to 8
        :type length: int, optional
        :param include_numbers: Include numbers in the password, defaults to False
        :type include_numbers: bool, optional
        :param include_symbols: Include symbols in the password , defaults to False
        :type include_symbols: bool, optional
        """
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers :
            self.characters += string.digits
        if include_symbols :
            self.characters += string.punctuation

    def generate(self) -> str:
            """Generates a random password."""
            return ''.join(random.choices(population=self.characters, k=self.length))


class MemorablePassword(PasswordGenerator):

    def __init__(self ,
                num_of_words: int  = 4,
                separator: str = '_',
                capitalization: bool = False,
                vocabs : list = None ) :
        """__init__ _summary_

        MemorablePassword class generates a memorable password using words from a vocabulary.

        :param num_of_words: Number of words in the password, defaults to 4
        :type num_of_words: int, optional
        :param separator: Separator between words in the password, defaults to '_'
        :type separator: str, optional
        :param capitalization: Capitalize the words in the password, defaults to False
        :type capitalization: bool, optional
        :param vocabs: List of words to choose from, default is NLTK English words
        :type vocabs: list, optional
        """
        self.words = num_of_words
        self.separator = separator
        self.capitalize = capitalization
        self.vocabs = vocabs
        if self.vocabs == None :
            self.vocabs = nltk.corpus.words.words()

    def generate(self)-> str :
        """Generates a memorable password."""
        words = self.vocabs
        if self.capitalize :
            return f'{self.separator}'.join(list(map(lambda x : x.capitalize(), random.choices(population=words,k=self.words))))
        else :
            return f'{self.separator}'.join(random.choices(population=words,k=self.words))


def test_random_password():
    random_pass = RandomPassword(length= 100, include_numbers= True, include_symbols= True)
    password = random_pass.generate()
    print(password)
    assert len(password) == 100, 'length of random password is incorrect'
    assert any(char in string.digits for char in password),'there is no number in random password '
    assert any(char in string.punctuation for char in password) , 'there is no punctuation in random password '


def test_memorable_password():
    memorable_pass = MemorablePassword(
        num_of_words=100 ,
        separator='_',
        capitalization=True,
        vocabs=nltk.corpus.words.words()
        )
    password = memorable_pass.generate()
    print(password)
    assert len(password.split('_')) == 100, 'length of memorable password is incorrect'
    assert all(vocab[0] in nltk.corpus.words.words() for vocab in (password.split('_'))), 'Vocab is not in nltk list'


def test_pin_password():
    pin_pass = PinPassword(length=100)
    password = pin_pass.generate()
    print(password)
    x_l = []
    for i in str(password):
        x_l.append(i)
    assert len(x_l) == 100 , 'length of PIN password is incorrect'
    assert all(char in string.digits for char in x_l)


def main():
    print('Testing the Random Password Generator')
    test_random_password()
    print('Testing the Memorable Password Generator')
    test_memorable_password()
    print('Testing the PIN Password Generator')
    test_pin_password()


if __name__ == '__main__':
    main()
