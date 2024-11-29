#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the setter to validate the input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")


    def is_sentence(self):
        """Check if value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Check if value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Check if value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Count the number of sentences in the string."""
        # Replace sentence-ending punctuation with a common separator
        text = re.sub(r'[.!?]', '.', self.value)
        # Split on periods and filter out empty strings
        sentences = [s for s in text.split('.') if s.strip()]
        return len(sentences)

  
