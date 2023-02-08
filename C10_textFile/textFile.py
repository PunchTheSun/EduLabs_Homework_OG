import csv
import json
import os.path
from abc import ABC, abstractmethod
from io import TextIOWrapper
from textFile_Exceptions import *


class TextFile(ABC):

    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError()
        _, ext = os.path.splitext(file_path)
        if ext != self.get_file_ext():
            raise UnsupportedFileType()

        self._file_path = file_path

    def get_file_size(self):
        return os.path.getsize(self._file_path)

    def get_content(self):
        with open(self._file_path, 'r') as f:
            ret_val = self._read_file_content(f)
        return ret_val

    @abstractmethod
    def _read_file_content(self, f: TextIOWrapper):
        raise NotImplementedError()

    @abstractmethod
    def get_file_ext(self):
        raise NotImplementedError()


class CsvFile(TextFile):

    def __init__(self, file_path: str, delimiter: str = ","):
        super().__init__(file_path)
        self._delimiter = delimiter

    def _read_file_content(self, f: TextIOWrapper):
        return list(csv.DictReader(f, delimiter=self._delimiter))

    def _get_headers(self):
        with open(self._file_path, 'r') as f:
            csv_file = csv.reader(f, delimiter=self._delimiter)
            csv_file = list(csv_file)
            return csv_file[0]

    def get_file_ext(self):
        return '.csv'

    def get_row_num(self) -> int:
        csv_file = self.get_content()
        return len(csv_file) + 1

    def get_col_num(self):
        csv_file = self.get_content()
        return len(csv_file[0])

    def get_row(self, row_num: int, has_header: bool = True):
        csv_file = self.get_content()
        if row_num > self.get_row_num() or row_num < 1:
            raise IndexError
        if has_header:
            return csv_file[row_num-1]
        ret_dict = dict()
        key_index = 1
        for header in csv_file[0].keys():
            ret_dict[key_index] = csv_file[row_num-1][header]
            key_index += 1
        return ret_dict

    def get_col(self, col_num: int, has_header: bool = True):
        csv_file = self.get_content()
        if col_num > self.get_col_num() or col_num < 1:
            raise IndexError
        key_to_num = dict()
        key_to_num_index = 1
        for header in csv_file[0].keys():
            key_to_num[key_to_num_index] = header
            key_to_num_index += 1
        ret_list = []
        if not has_header:
            ret_list.append(key_to_num[col_num])
        for i in range(self.get_row_num()-1):
            ret_list.append(csv_file[i][key_to_num[col_num]])
        return ret_list

    def get_cell(self, row_num: int, col_num: int, has_header: bool = True):
        if col_num > self.get_col_num() or col_num < 0 or row_num > self.get_row_num() or row_num < 0:
            raise IndexError
        csv_col = self.get_col(col_num, has_header)
        return csv_col[row_num-1]

    def __add__(self, other):
        if self.get_file_ext() != other.get_file_ext():
            raise DifferentTypeFiles
        first_filename_no_ext, _ = os.path.basename(self._file_path).split('.')
        sum_csv_filename = first_filename_no_ext + '_' + os.path.basename(other._file_path)
        sum_csv_path = os.path.join(os.path.dirname(self._file_path), sum_csv_filename)
        if os.path.exists(sum_csv_path):
            raise FilenameAlreadyExists
        first = self.get_content()
        second = other.get_content()
        headers = self._get_headers()
        for header in other._get_headers():
            if header not in headers:
                headers.append(header)
        for row in second:
            first.append(row)
        with open(sum_csv_path, 'w') as f:
            sum_csv = csv.DictWriter(f, fieldnames=headers)
            sum_csv.writeheader()
            sum_csv.writerows(first)
        return


class JsonFile(TextFile):

    def _read_file_content(self, f: TextIOWrapper):
        return json.load(f)

    def get_file_ext(self):
        return '.json'

    def is_list(self) -> bool:
        if isinstance(self.get_content(), list):
            return True
        return False

    def is_object(self) -> bool:
        if isinstance(self.get_content(), dict):
            return True
        return False


class TxtFile(TextFile):

    def _read_file_content(self, f: TextIOWrapper):
        return f.read()

    def get_file_ext(self):
        return '.txt'

    def get_words_num(self):
        txt_file = self.get_content()
        return txt_file.count(" ")+1

    def get_avg_word_len(self):
        txt_file = self.get_content()
        words = txt_file.split(" ")
        if not words:
            raise TextFileIsEmpty
        words_length = 0
        words_count = 0
        for word in words:
            words_count += 1
            words_length += len(word)
        return words_length/words_count

    def get_line(self, line_num: int):
        txt_file = self.get_content()
        txt_in_lines = txt_file.split("\n")
        if line_num > len(txt_in_lines) or line_num < 1:
            raise IndexError
        return txt_in_lines[line_num-1]

    def __add__(self, other):
        if self.get_file_ext() != other.get_file_ext():
            raise DifferentTypeFiles
        first_filename_no_ext, _ = os.path.basename(self._file_path).split('.')
        sum_txt_filename = first_filename_no_ext + '_' + os.path.basename(other._file_path)
        sum_txt_path = os.path.join(os.path.dirname(self._file_path), sum_txt_filename)
        if os.path.exists(sum_txt_path):
            raise FilenameAlreadyExists
        first = self.get_content()
        second = other.get_content()
        combined = first + "\n" + second
        with open(sum_txt_path, 'w') as f:
            f.write(combined)
        return


# if __name__ == '__main__':
#     csv1_path = "data\grades.csv"
#     csv2_path = "data\more_grades.csv"
#     txt1_path = "data\\text_file_1.txt"
#     txt2_path = "data\\text_file_2.txt"
#     json1_path = "data\json_file_1.json"
#     json2_path = "data\json_file_2.json"
#     csv1 = CsvFile(csv1_path)
#     csv2 = CsvFile(csv2_path)
#     txt1 = TxtFile(txt1_path)
#     txt2 = TxtFile(txt2_path)
#     json_file1 = JsonFile(json1_path)
#     json_file2 = JsonFile(json2_path)
    # print(csv1.get_rows_num())
    # print(csv1.get_col_num())
    # print(csv1.get_row(3, False))
    # print(csv2.get_row(3))
    # print(csv2.get_col(2))
    # print(csv1.get_col(2, False))
    # print(csv1.get_cell(4, 3, False))
    # print(csv2.get_cell(3, 3))
    # print(txt2.get_words_num())
    # print(txt1.get_avg_word_len())
    # print(txt2.get_line(2))
    # print(json_file1.is_list())
    # print(json_file2.is_list())
    # print(json_file1.is_object())
    # print(json_file2.is_object())
    # txt1 + txt2
