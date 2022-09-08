""" from https://github.com/keithito/tacotron """

'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
'''

from pypinyin import pinyin, Style

'''Chinese cleaners'''

_tones = ["1", "2", "3", "4"]

_revision_ch = {
    "ang": "aŋ",
    "eng": "əŋ",
    "ing": "iŋ",
    "ong": "ɔŋ",

    "ai": "aɪ",
    "ei": "ɛɪ",
    "ui": "uɛɪ",
    "iu": "iɔu",
    "ie": "iɛ",
    "ue": "üɛ",
    "an": "æn",
    "en": "ən",
    # ü前有j,q,x或y时会被去掉两点
    "ju": "jü",
    "jue": "jüɛ",
    "jun": "jün",
    "juan": "jüæn",
    "qu": "qü",
    "que": "qüɛ",
    "qun": "qün",
    "quan": "qüæn",
    "xu": "xü",
    "xue": "xüɛ",
    "xun": "xün",
    "xuan": "xüæn",
    "yu": "yü",
    "yue": "yüɛ",
    "yun": "yün",
    "yuan": "yüæn",

    "un": "uən",
    "zhi": "dʒI",
    "chi": "tʃI",
    "shi": "ʃI",
    "zh": "dʒ",
    "ch": "tʃ",
    "sh": "ʃ",
    "zi": "zI",
    "ci": "tsI",
    "si": "sI",
    "c": "ts",
    "v": "ü",
    "e": "ə",
    "o": "ɔ"
}

def chinese_cleaners(text):
  phones = []
  for phone in pinyin(text, style=Style.TONE3):
    phone = phone[0]
    for item in _revision_ch.items():
      old = item[0]
      new = item[1]
      phone = phone.replace(old, new)
    phones.append(phone)
    text = " ".join(phones)

  return text
