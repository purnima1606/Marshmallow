class Spam:

    def __init__(self, text):
        self.text = text

    # internal method
    def _clean_up(self):
        return self.text.strip()

    def split_text(self):
        temp = self._clean_up()
        return temp.split()

    def get_len(self):
        temp = self._clean_up()
        return len(temp)


s = Spam("    hello world    ")
print(s.get_len())      # 11 - after removing leading and trailing whitespaces

