Python file word_count.py counts number of occurrences of words in a given file and displays it to standard output.

Example of usage in command line:
python word_count text_example/f4.txt

Assertion error will occur if no filename was provided as command line argument.
Input file is read in segments of size buff_size (default 4096 bytes) in order to count words from files which are too large to be loaded into memory.
Problem which could occur using this approach is if we have file content: "Hello world" and we read 8 characters at the time.
After first pass through file we would extract "Hello wo". String "wo" should not be considered as a word - additional characters should be loaded as well.
This scenario is covered in test_word_count_file_too_big_for_memory() test method in test_word_count.py file.

Text file punctuation.txt consists of English punctuation symbols, separated by newlines, which are not considered words. Those symbols will be excluded from word search.
After reading text segment from file, said segment will be processed using regular expressions to remove newlines, standalone and suffix punctuation as well as multiple white spaces.

Finally, processed text is split by white space and added into dictionary. Dictionary key is string representation of word, while number of occurrences is value.
Structure for word occurrences is dictionary because lookup time is O(1) (whereas if list was used it would be O(n))

If any error occurs it will be caught in except block where it can be logged or handled appropriately.
