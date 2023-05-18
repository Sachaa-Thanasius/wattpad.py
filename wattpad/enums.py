"""
wattpad.enums
--------------

Enums for the Wattpad API.
"""

from enum import Enum


# Source: https://www.wattpad.com/apiv2/getlang
class Language(Enum):
    ENGLISH: 1
    FRENCH: 2
    ITALIAN: 3
    GERMAN: 4
    SPANISH: 5
    PORTUGUESE: 6
    RUSSIAN: 7
    CHINESE_TRADITIONAL: 8
    JAPANESE: 9
    KOREAN: 10
    OTHER: 11
    CHINESE_SIMPLIFIED: 12
    DUTCH: 13
    POLISH: 14
    ROMANIAN: 15
    ARABIC: 16
    HEBREW: 17
    FILIPINO: 18
    VIETNAMESE: 19
    INDONESIAN: 20
    HINDI: 21
    MALAY: 22
    TURKISH: 23
    CZECH: 24
    MALAYALAM: 25
    SWEDISH: 26
    NORWEGIAN: 27
    HUNGARIAN: 28
    DANISH: 29
    GREEK: 30
    PERSIAN: 31
    THAI: 32
    ICELANDIC: 33
    FINNISH: 34
    ESTONIAN: 35
    LATVIAN: 36
    LITHUANIAN: 37
    CATALAN: 38
    BOSNIAN: 39
    SERBIAN: 40
    CROATIAN: 41
    SLOVENE: 42
    BULGARIAN: 43
    SLOVAK: 44
    BELARUSIAN: 45
    UKRAINIAN: 46
    BENGALI: 47
    URDU: 48
    TAMIL: 49
    SWAHILI: 50
    AFRIKAANS: 51
    # Missing 52
    GUJARATI: 53
    ODIA: 54
    PUNJABI: 55
    ASSAMESE: 56
    MARATHI: 57

    def __str__(self):
        lookup: [Language, str] = {
            Language.ENGLISH:               "English",
            Language.FRENCH:                "Fran\u00e7ais",
            Language.ITALIAN:               "Italiano",
            Language.GERMAN:                "Deutsch",
            Language.SPANISH:               "Espa\u00f1ol",
            Language.PORTUGUESE:            "Portugu\u00eas",
            Language.RUSSIAN:               "\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
            Language.CHINESE_TRADITIONAL:   "\u7e41\u9ad4\u4e2d\u6587",
            Language.JAPANESE:              "\u65e5\u672c\u8a9e",
            Language.KOREAN:                "\ud55c\uad6d\uc5b4",
            Language.OTHER:                 "Other",
            Language.CHINESE_SIMPLIFIED:    "\u7b80\u4f53\u4e2d\u6587",
            Language.DUTCH:                 "Nederlands",
            Language.POLISH:                "Polski",
            Language.ROMANIAN:              "Rom\u00e2n\u0103",
            Language.ARABIC:                "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
            Language.HEBREW:                "\u05e2\u05d1\u05e8\u05d9\u05ea",
            Language.FILIPINO:              "Filipino",
            Language.VIETNAMESE:            "Ti\u1ebfng Vi\u1ec7t",
            Language.INDONESIAN:            "Bahasa Indonesia",
            Language.HINDI:                 "\u0939\u093f\u0928\u094d\u0926\u0940",
            Language.MALAY:                 "Bahasa Melayu",
            Language.TURKISH:               "T\u00fcrk\u00e7e",
            Language.CZECH:                 "\u010cesky",
            Language.MALAYALAM:             "\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02",
            Language.SWEDISH:               "Svenska",
            Language.NORWEGIAN:             "Norsk",
            Language.HUNGARIAN:             "Magyar",
            Language.DANISH:                "Dansk",
            Language.GREEK:                 "\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac",
            Language.PERSIAN:               "\u0641\u0627\u0631\u0633\u06cc",
            Language.THAI:                  "\u0e20\u0e32\u0e29\u0e32\u0e44\u0e17\u0e22",
            Language.ICELANDIC:             "\u00cdslenska",
            Language.FINNISH:               "Suomi",
            Language.ESTONIAN:              "Eesti",
            Language.LATVIAN:               "Latvie\u0161u",
            Language.LITHUANIAN:            "Lietuvi\u0173",
            Language.CATALAN:               "Catal\u00e0",
            Language.BOSNIAN:               "\u0411\u043e\u0441\u0430\u043d\u0441\u043a\u0438",
            Language.SERBIAN:               "\u0421\u0440\u043f\u0441\u043a\u0438",
            Language.CROATIAN:              "Hrvatski",
            Language.SLOVENE:               "Sloven\u0161\u010dina",
            Language.BULGARIAN:             "\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438",
            Language.SLOVAK:                "Sloven\u010dina",
            Language.BELARUSIAN:            "\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0456",
            Language.UKRAINIAN:             "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430",
            Language.BENGALI:               "\u09ac\u09be\u0982\u09b2\u09be",
            Language.URDU:                  "\u0627\u064f\u0631\u062f\u064f\u0648\u200e",
            Language.TAMIL:                 "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
            Language.SWAHILI:               "Kiswahili",
            Language.AFRIKAANS:             "Afrikaans",
            Language.GUJARATI:              "\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0",
            Language.ODIA:                  "\u0b13\u0b21\u0b3c\u0b3f\u0b06",
            Language.PUNJABI:               "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
            Language.ASSAMESE:              "\u0985\u09b8\u09ae\u09c0\u09af\u09bc\u09be",
            Language.MARATHI:               "\u092e\u0930\u093e\u0920\u0940"
        }
        return lookup[self]


# Source: https://www.wattpad.com/api/v3/categories?language=1
class Category(Enum):
    NONE = -1
    UNKNOWN_VALUE = 0
    TEEN_FICTION = 1
    POETRY = 2
    FANTASY = 3
    ROMANCE = 4
    SCIENCE_FICTION = 5
    FANFICTION = 6
    HUMOR = 7
    MYSTERY_OR_THRILLER = 8
    HORROR = 9
    CLASSICS = 10
    ADVENTURE = 11
    PARANORMAL = 12
    SPIRITUAL = 13
    ACTION = 14
    # Missing 15
    NONFICTION = 16
    SHORT_STORY = 17
    VAMPIRE = 18
    RANDOM = 19
    # Missing 20
    GENERAL_FICTION = 21
    WEREWOLF = 22
    HISTORICAL_FICTION = 23
    CHICK_LIT = 24

    def __str__(self):
        lookup: dict[Category, str] = {
            Category.MYSTERY_OR_THRILLER: "Mystery / Thriller",
            Category.NONFICTION:          "Non-Fiction",
            Category.CHICK_LIT:           "ChickLit"
        }
        return lookup.get(self, self.name.replace("_", " ").title())
