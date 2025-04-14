import pytest

from main import *

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self,collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book(self, collector):

        collector.add_new_book('Идиот')

        assert 'Идиот' in collector.books_genre

    def test_set_book_genre(self, collector):

        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот','Детективы')

        assert 'Детективы' in collector.books_genre.values()


    def test_get_book_genre(self,collector): # Deleted parametrize

        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот','Детективы')

        assert collector.get_book_genre('Идиот') == 'Детективы' # Change assert

    def test_get_books_with_specific_genre(self, collector):

        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Детективы')
        collector.add_new_book('Джейн Эйр')
        collector.set_book_genre('Джейн Эйр', 'Ужасы') # Add new other genre

        two_books_with_specific_genre = collector.get_books_with_specific_genre('Детективы')

        assert two_books_with_specific_genre == ['Идиот'] # Change assert


    def test_get_books_genre(self, collector): # Remove genre

        collector.add_new_book('Идиот')
        collector.add_new_book('Джейн Эйр')

        list_of_books = collector.get_books_genre()

        assert len(list_of_books) == 2

    def test_get_books_for_children(self, collector):

        collector.add_new_book('Тачки')
        collector.set_book_genre('Тачки', 'Мультфильмы')
        collector.add_new_book('Джейн Эйр')
        collector.set_book_genre('Джейн Эйр', 'Ужасы') # Add not for children genre

        assert 'Тачки' in collector.get_books_for_children() and 'Джейн Эйр' not in collector.get_books_for_children()

    def test_add_add_book_in_favorites(self, collector):

        collector.add_new_book('Тачки')
        collector.add_book_in_favorites('Тачки')

        assert 'Тачки' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):

        collector.add_new_book('Тачки')
        collector.add_book_in_favorites('Тачки')
        collector.delete_book_from_favorites('Тачки')

        assert 'Тачки' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):

        collector.add_new_book('Тачки')
        collector.add_book_in_favorites('Тачки')

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('name', ['', 'ЭтаКнигаИмеетНазваниеИзСорокаДвухСимволов!',]) # Add test with parametrize
    def test_add_new_book_with_len_more_that_need(self, collector, name):

        collector.add_new_book(name)

        assert name not in collector.books_genre






















