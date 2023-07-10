class Flashcard:
  def __init__(self, word, translations):
    self.word = word
    self.translations = translations

  def get_translation(self, language_code):
    if language_code in self.translations:
      return self.translations[language_code]
    else:
      return "Translation not available"
