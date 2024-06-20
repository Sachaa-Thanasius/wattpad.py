"""
wattpad.enums
--------------

Enums for the Wattpad API.
"""

from enum import Enum

__all__ = ("LanguageType", "Category")


class APIBase(Enum):
    REG = "https://www.wattpad.com"
    API = "https://api.wattpad.com"


class APIVer(Enum):
    V2 = "/apiv2"
    V3 = "/api/v3"
    V4 = "/v4"
    V5 = "/v5"


# Source: https://www.wattpad.com/apiv2/getlang
class LanguageType(Enum):
    ENGLISH = 1
    FRENCH = 2
    ITALIAN = 3
    GERMAN = 4
    SPANISH = 5
    PORTUGUESE = 6
    RUSSIAN = 7
    CHINESE_TRADITIONAL = 8
    JAPANESE = 9
    KOREAN = 10
    OTHER = 11
    CHINESE_SIMPLIFIED = 12
    DUTCH = 13
    POLISH = 14
    ROMANIAN = 15
    ARABIC = 16
    HEBREW = 17
    FILIPINO = 18
    VIETNAMESE = 19
    INDONESIAN = 20
    HINDI = 21
    MALAY = 22
    TURKISH = 23
    CZECH = 24
    MALAYALAM = 25
    SWEDISH = 26
    NORWEGIAN = 27
    HUNGARIAN = 28
    DANISH = 29
    GREEK = 30
    PERSIAN = 31
    THAI = 32
    ICELANDIC = 33
    FINNISH = 34
    ESTONIAN = 35
    LATVIAN = 36
    LITHUANIAN = 37
    CATALAN = 38
    BOSNIAN = 39
    SERBIAN = 40
    CROATIAN = 41
    SLOVENE = 42
    BULGARIAN = 43
    SLOVAK = 44
    BELARUSIAN = 45
    UKRAINIAN = 46
    BENGALI = 47
    URDU = 48
    TAMIL = 49
    SWAHILI = 50
    AFRIKAANS = 51
    # Missing 52
    GUJARATI = 53
    ODIA = 54
    PUNJABI = 55
    ASSAMESE = 56
    MARATHI = 57

    def __str__(self):
        lookup: dict[LanguageType, str] = {
            LanguageType.ENGLISH: "English",
            LanguageType.FRENCH: "Fran\u00e7ais",
            LanguageType.ITALIAN: "Italiano",
            LanguageType.GERMAN: "Deutsch",
            LanguageType.SPANISH: "Espa\u00f1ol",
            LanguageType.PORTUGUESE: "Portugu\u00eas",
            LanguageType.RUSSIAN: "\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
            LanguageType.CHINESE_TRADITIONAL: "\u7e41\u9ad4\u4e2d\u6587",
            LanguageType.JAPANESE: "\u65e5\u672c\u8a9e",
            LanguageType.KOREAN: "\ud55c\uad6d\uc5b4",
            LanguageType.OTHER: "Other",
            LanguageType.CHINESE_SIMPLIFIED: "\u7b80\u4f53\u4e2d\u6587",
            LanguageType.DUTCH: "Nederlands",
            LanguageType.POLISH: "Polski",
            LanguageType.ROMANIAN: "Rom\u00e2n\u0103",
            LanguageType.ARABIC: "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
            LanguageType.HEBREW: "\u05e2\u05d1\u05e8\u05d9\u05ea",
            LanguageType.FILIPINO: "Filipino",
            LanguageType.VIETNAMESE: "Ti\u1ebfng Vi\u1ec7t",
            LanguageType.INDONESIAN: "Bahasa Indonesia",
            LanguageType.HINDI: "\u0939\u093f\u0928\u094d\u0926\u0940",
            LanguageType.MALAY: "Bahasa Melayu",
            LanguageType.TURKISH: "T\u00fcrk\u00e7e",
            LanguageType.CZECH: "\u010cesky",
            LanguageType.MALAYALAM: "\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02",
            LanguageType.SWEDISH: "Svenska",
            LanguageType.NORWEGIAN: "Norsk",
            LanguageType.HUNGARIAN: "Magyar",
            LanguageType.DANISH: "Dansk",
            LanguageType.GREEK: "\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac",
            LanguageType.PERSIAN: "\u0641\u0627\u0631\u0633\u06cc",
            LanguageType.THAI: "\u0e20\u0e32\u0e29\u0e32\u0e44\u0e17\u0e22",
            LanguageType.ICELANDIC: "\u00cdslenska",
            LanguageType.FINNISH: "Suomi",
            LanguageType.ESTONIAN: "Eesti",
            LanguageType.LATVIAN: "Latvie\u0161u",
            LanguageType.LITHUANIAN: "Lietuvi\u0173",
            LanguageType.CATALAN: "Catal\u00e0",
            LanguageType.BOSNIAN: "\u0411\u043e\u0441\u0430\u043d\u0441\u043a\u0438",
            LanguageType.SERBIAN: "\u0421\u0440\u043f\u0441\u043a\u0438",
            LanguageType.CROATIAN: "Hrvatski",
            LanguageType.SLOVENE: "Sloven\u0161\u010dina",
            LanguageType.BULGARIAN: "\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438",
            LanguageType.SLOVAK: "Sloven\u010dina",
            LanguageType.BELARUSIAN: "\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0456",
            LanguageType.UKRAINIAN: "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430",
            LanguageType.BENGALI: "\u09ac\u09be\u0982\u09b2\u09be",
            LanguageType.URDU: "\u0627\u064f\u0631\u062f\u064f\u0648\u200e",
            LanguageType.TAMIL: "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
            LanguageType.SWAHILI: "Kiswahili",
            LanguageType.AFRIKAANS: "Afrikaans",
            LanguageType.GUJARATI: "\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0",
            LanguageType.ODIA: "\u0b13\u0b21\u0b3c\u0b3f\u0b06",
            LanguageType.PUNJABI: "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
            LanguageType.ASSAMESE: "\u0985\u09b8\u09ae\u09c0\u09af\u09bc\u09be",
            LanguageType.MARATHI: "\u092e\u0930\u093e\u0920\u0940",
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
            Category.NONFICTION: "Non-Fiction",
            Category.CHICK_LIT: "ChickLit",
        }
        return lookup.get(self, self.name.replace("_", " ").title())
