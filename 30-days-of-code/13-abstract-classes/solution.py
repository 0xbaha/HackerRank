from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,price,title,author):
        self.price = price
        Book.__init__(self,author,title)
    def display(self):
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Price: {price}')

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()