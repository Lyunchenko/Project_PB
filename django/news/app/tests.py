import unittest
import parser_news
import news


class TestNews(unittest.TestCase):

    def test_set_news(self):
        obj = news.News()
        example = {'id': 1,
                   'title': 'record.title',
                   'link': 'record.link',
                   'date': 'date',
                   'description': 'record.description'}
        obj.set_news(example)
        self.assertEqual(obj._news[1], example) # элемент бодавлен в словарь
        self.assertEqual(len(obj._news), 1) # в словаре только 1 элемент
        obj.set_news(example)
        self.assertEqual(len(obj._list_news), 1) # элемент повторно не добавлен
        example = {'id': 2,
                   'title': 'record.title',
                   'link': 'record.link',
                   'date': 'date',
                   'description': 'record.description'}
        obj.set_news(example)
        self.assertEqual(obj._news[2], example) # элемент бодавлен в словарь
        self.assertEqual(len(obj._news), 2) # в словаре 2 элемента


    def test_set_attribute(self):
        obj = news.News()
        example = {'id': 1,
                   'title': 'record.title',
                   'link': 'record.link',
                   'date': 'date',
                   'description': 'record.description'}
        obj.set_news(example)
        example = {'id': 2,
                   'title': 'record.title',
                   'link': 'record.link',
                   'date': 'date',
                   'description': 'record.description'}
        obj.set_news(example)
        obj.set_attribute(2, 'text', 'text news')
        example = {'id': 2,
                   'title': 'record.title',
                   'link': 'record.link',
                   'date': 'date',
                   'description': 'record.description',
                   'text': 'text news'}
        self.assertEqual(obj._news[2], example)

        

class TestParserNews(unittest.TestCase):

    def test_add_del_channel(self):
        
        obj = parser_news.ParserNews()
        self.assertEqual(len(obj._channels), 0) # Создание объекта с пустым списком каналов
        
        obj.set_channel('url')
        self.assertIn('url', obj._channels) # Добавление адреса rss канала
        self.assertEqual(len(obj._channels), 1) # Добавление адреса rss канала

        obj.set_channel('url')
        self.assertIn('url', obj._channels) # Повторное добавление существующего канала
        self.assertEqual(len(obj._channels), 1) # Повторное добавление существующего канала
        
        obj.set_channel('url2')
        self.assertIn('url2', obj._channels) # Добавление 2-х каналов
        self.assertEqual(len(obj._channels), 2) # Добавление 2-х каналов

        obj.del_channel('url')
        self.assertNotIn('url', obj._channels) # Удаление канала
        self.assertEqual(len(obj._channels), 1) # Удаление канала

        obj.del_channel('url')
        self.assertNotIn('url', obj._channels) # Удаление несуществующего канала
        self.assertEqual(len(obj._channels), 1) # Удаление несуществующего канала


if __name__ == '__main__':
    unittest.main()







'''
Описание модуля unittest:
    https://pythonworld.ru/moduli/modul-unittest.html

Специальные функци:
    def setUp(self):
        # Код настройки - перед запуском тестов
        pass

    def tearDown(self):
        # Код после выполнения тестов
        pass

Пропуск тестов:
    @unittest.skip(reason) - пропустить тест. reason описывает причину пропуска.
    @unittest.skipIf(condition, reason) - пропустить тест, если condition истинно.
    @unittest.skipUnless(condition, reason) - пропустить тест, если condition ложно.
    @unittest.expectedFailure - пометить тест как ожидаемая ошибка.

Функции для проверок:
    assertEqual(a, b) — a == b
    assertNotEqual(a, b) — a != b
    assertTrue(x) — bool(x) is True
    assertFalse(x) — bool(x) is False
    assertIs(a, b) — a is b
    assertIsNot(a, b) — a is not b
    assertIsNone(x) — x is None
    assertIsNotNone(x) — x is not None
    assertIn(a, b) — a in b
    assertNotIn(a, b) — a not in b
    assertIsInstance(a, b) — isinstance(a, b)
    assertNotIsInstance(a, b) — not isinstance(a, b)
    assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc
    assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc и сообщение соответствует регулярному выражению r
    assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение
    assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение и сообщение соответствует регулярному выражению r
    assertAlmostEqual(a, b) — round(a-b, 7) == 0
    assertNotAlmostEqual(a, b) — round(a-b, 7) != 0
    assertGreater(a, b) — a > b
    assertGreaterEqual(a, b) — a >= b
    assertLess(a, b) — a < b
    assertLessEqual(a, b) — a <= b
    assertRegex(s, r) — r.search(s)
    assertNotRegex(s, r) — not r.search(s)
    assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен
'''