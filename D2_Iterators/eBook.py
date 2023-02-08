# C4 - EBook Class
import math


class EBook:

    def __init__(self, txt_file_path: str, words_per_page: int = 100):
        self._path = txt_file_path
        self._words_per_page = words_per_page
        self._bookmarks = dict()
        self._iterator = 1
        self._iterator_end = self.get_amount_of_pages()

    def _get_whole_file_content(self) -> str:
        with open(self._path, 'r') as f:
            file_content = f.read()
        return file_content

    def get_amount_of_pages(self) -> int:
        file_content = self._get_whole_file_content()
        return math.ceil((file_content.count(' ') + 1) / self._words_per_page)

    def display_page_content(self, page_number: int) -> str:
        if page_number > self.get_amount_of_pages():
            raise IndexError
        words_list = self._get_whole_file_content().split(' ')
        ret_str = ""
        for word in words_list[(page_number * self._words_per_page):(page_number * self._words_per_page + self._words_per_page)]:
            ret_str += word+' '
        return ret_str

    def bookmark_page(self, bookmark_name: str, bookmark_page: int):
        if bookmark_page > self.get_amount_of_pages():
            raise IndexError
        self._bookmarks[bookmark_name] = bookmark_page
        return

    def delete_bookmark_by_name(self, bookmark_name: str):
        if bookmark_name not in self._bookmarks.keys():
            raise NameError
        self._bookmarks.pop(bookmark_name)
        return

    def delete_bookmarks_by_page(self, bookmark_page: int):
        if bookmark_page > self.get_amount_of_pages():
            raise IndexError
        keys_to_del = []
        for key in self._bookmarks.keys():
            if self._bookmarks[key] == bookmark_page:
                keys_to_del.append(key)
        for del_key in keys_to_del:
            self._bookmarks.pop(del_key)
        return

    def display_all_bookmarks(self):
        return self._bookmarks

    def display_bookmarked_page(self, bookmark_name: str):
        if bookmark_name not in self._bookmarks.keys():
            raise NameError
        return self.display_page_content(self._bookmarks[bookmark_name])

    def __iter__(self):
        self._iterator = 1
        return self

    def __next__(self):
        curr_val = self._iterator
        if curr_val > self._iterator_end:
            raise StopIteration
        self._iterator += 1
        return self.display_page_content(curr_val)

# if __name__ == "__main__":
#     my_book = EBook('data/alice_in_wonderland.txt')
#     print(my_book.get_amount_of_pages())
#     print(my_book.display_page_content(200))
#     my_book.bookmark_page("banana", 5)
#     my_book.bookmark_page("banana2", 7)
#     print(my_book.display_all_bookmarks())
#     print(my_book.display_bookmarked_page("banana"))
#     my_book.delete_bookmarks_by_page(5)
#     my_book.delete_bookmark_by_name("banana2")
#     print(my_book.display_all_bookmarks())
#     for page in my_book:
#         print(page)

