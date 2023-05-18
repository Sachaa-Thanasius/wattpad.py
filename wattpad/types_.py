"""
wattpad.types_
--------------

Typings for the Wattpad API.
"""

from typing import TypedDict, NotRequired


class _Language(TypedDict):
    id: int
    name: str


class _TextUrl(TypedDict):
    text: str


class _Safety(TypedDict):
    isMuted: bool
    isBlocked: bool


class _Programs(TypedDict):
    wattpad_stars: bool
    wattpad_circle: bool


class _TagRanking(TypedDict):
    name: str
    rank: int
    total: int


class PartialUser(TypedDict):
    name: str
    avatar: str
    fullname: NotRequired[str]
    backgroundColour: NotRequired[str]


class User(TypedDict):
    username: str
    avatar: str
    isPrivate: bool
    backgroundUrl: str
    name: str
    description: str
    status: str
    gender: str
    genderCode: str
    language: int
    locale: str
    createDate: str             # datetime with tz
    modifyDate: str             # datetime with tz
    location: str
    verified: bool
    ambassador: bool
    facebook: str
    twitter: str
    website: str
    lulu: str
    smashwords: str
    bubok: str
    votesReceived: int
    numStoriesPublished: int
    numFollowing: int
    numFollowers: int
    numMessages: int
    numLists: int
    verified_email: bool
    preferred_categories: list
    allowCrawler: bool
    deeplink: str
    isMuted: bool               # provided by default, but inside safety, which is optional

    # Need specific query with ?field=
    safety: NotRequired[_Safety]
    highlight_colour: NotRequired[str]
    programs: NotRequired[_Programs]
    externalId: NotRequired[str]
    showSocialNetwork: NotRequired[bool]


class PartialPart(TypedDict):
    id: int
    createDate: str             # datetime with tz


class Part(PartialPart):
    title: str
    url: str
    rating: int
    draft: bool
    modifyDate: str             # datetime with tz
    length: int
    videoId: str
    photoUrl: str
    commentCount: int
    voteCount: int
    readCount: int

    # Need specific query with ?field=
    dedication: NotRequired[dict]
    wordCount: NotRequired[int]
    text_url: NotRequired[_TextUrl]
    deleted: NotRequired[bool]
    hash: NotRequired[str]
    voted: NotRequired[bool]
    hasBannedImages: NotRequired[bool]


class Story(TypedDict):
    id: int
    title: str
    createDate: str             # datetime with tz
    modifyDate: str             # datetime with tz
    voteCount: int
    readCount: int
    commentCount: int
    language: _Language
    user: PartialUser
    description: str
    cover: str
    cover_timestamp: str        # datetime with tz
    completed: bool
    categories: list[int]
    tags: list[str]
    rating: int
    mature: bool
    copyright: int
    url: str
    firstPartId: int
    numParts: int
    firstPublishedPart: PartialPart
    lastPublishedPart: PartialPart
    parts: list[Part]
    deleted: bool

    # Need specific query with ?field=
    tagRankings: NotRequired[list[_TagRanking]]
    highlight_colour: NotRequired[str]
    promoted: NotRequired[bool]
    sponsor: NotRequired[list]
    isAdExempt: NotRequired[bool]
    story_text_url: NotRequired[_TextUrl]
    isPaywalled: NotRequired[bool]
    paidModel: NotRequired[str]
    ratingLocked: NotRequired[bool]


class Comment(TypedDict):
    author: PartialUser
    body: str
    createDate: str             # datetime with tz
    startPosition: int
    endPosition: int
    id: str
    isOffensive: bool
    isReply: bool
    numReplies: int
    paragraphId: str
    parentId: str | None
    partId: int
    deeplink: str
    legacyId: int


class ReadingList(TypedDict):
    id: int
    name: str
    user: PartialUser
    numStories: int
    cover: str
    sample_covers: list[str]

    # Need specific query with ?field=
    promoted: NotRequired[bool]