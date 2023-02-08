class TextFileError(Exception):
    pass


class UnsupportedFileType(TextFileError):
    pass


class FilenameAlreadyExists(TextFileError):
    pass


class DifferentTypeFiles(TextFileError):
    pass


class TextFileIsEmpty(TextFileError):
    pass
