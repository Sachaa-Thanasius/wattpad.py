"""
wattpad.types_
--------------

Typings / data structures for the Wattpad API.
"""

from typing import Optional

import msgspec

__all__ = ("PartialUser", "User", "PartialPart", "Part", "Story", "Comment", "ReadingList")


safety_names = {"is_muted": "IsMuted", "is_blocked": "IsBlocked"}


partial_user_names = {"username": "name", "name": "fullname", "background_colour": "backgroundColour"}


user_names = {
    "is_private": "isPrivate",
    "background_url": "backgroundUrl",
    "gender_code": "genderCode",
    "create_date": "createDate",
    "modify_date": "modifyDate",
    "votes_received": "votesReceived",
    "num_stories_published": "numStoriesPublished",
    "num_following": "numFollowing",
    "num_followers": "numFollowers",
    "num_messages": "numMessages",
    "num_lists": "numLists",
    "is_muted": "isMuted",
    "external_id": "externalId",
    "show_social_network": "showSocialNetwork",
}


partial_part_names = {"create_date": "createDate"}


part_names = {
    "modify_date": "modifyDate",
    "video_id": "videoId",
    "photo_url": "photoUrl",
    "comment_count": "commentCount",
    "vote_count": "voteCount",
    "read_count": "readCount",
    "word_count": "wordCount",
    "has_banned_images": "hasBannedImages",
}


story_names = {
    "create_date": "createDate",
    "modify_date": "modifyDate",
    "vote_count": "voteCount",
    "read_count": "readCount",
    "comment_count": "commentCount",
    "first_part_id": "firstPartId",
    "num_parts": "numParts",
    "first_published_part": "firstPublishedPart",
    "last_published_part": "lastPublishedPart",
    "tag_rankings": "tagRankings",
    "is_ad_exempt": "isAdExempt",
    "is_paywalled": "isPaywalled",
    "paid_model": "paidModel",
    "rating_locked": "ratingLocked",
}


comment_names = {
    "create_date": "createDate",
    "start_position": "startPosition",
    "end_position": "endPosition",
    "is_offensive": "isOffensive",
    "is_reply": "isReply",
    "num_replies": "numReplies",
    "paragraph_id": "paragraphId",
    "parent_id": "parentId",
    "part_id": "partId",
    "legacy_id": "legacyId",
}


reading_list_names = {"num_stories": "numStories"}


class _Language(msgspec.Struct):
    id: int
    name: str


class _TextUrl(msgspec.Struct):
    text: str


class _Safety(msgspec.Struct, rename=safety_names):
    is_muted: bool
    is_blocked: bool


class _Programs(msgspec.Struct):
    wattpad_stars: bool
    wattpad_circle: bool


class _TagRanking(msgspec.Struct):
    name: str
    rank: int
    total: int


class PartialUser(msgspec.Struct, rename=partial_user_names):
    username: str
    avatar: str
    name: Optional[str] = None
    background_colour: Optional[str] = None


class User(msgspec.Struct, rename=user_names):
    username: str
    avatar: str
    is_private: bool
    background_url: str
    name: str
    description: str
    status: str
    gender: str
    gender_code: str
    language: int
    locale: str
    create_date: str  # datetime with tz
    modify_date: str  # datetime with tz
    location: str
    verified: bool
    ambassador: bool
    facebook: str
    twitter: str
    website: str
    lulu: str
    smashwords: str
    bubok: str
    votes_received: int
    num_stories_published: int
    num_following: int
    num_followers: int
    num_messages: int
    num_lists: int
    verified_email: bool
    preferred_categories: list[str] = []
    allow_crawler: bool
    deeplink: str
    is_muted: bool  # provided by default, but inside safety, which is optional

    # Need specific query with ?field=
    safety: Optional[_Safety] = None
    highlight_colour: Optional[str] = None
    programs: Optional[_Programs] = None
    external_id: Optional[str] = None
    show_social_network: Optional[bool] = None


class PartialPart(msgspec.Struct, rename=partial_part_names):
    id: int
    create_date: str  # datetime with tz


class Part(PartialPart, rename=part_names):
    title: str
    url: str
    rating: int
    draft: bool
    modify_date: str  # datetime with tz
    length: int
    video_id: str
    photo_url: str
    comment_count: int
    vote_count: int
    read_count: int

    # Need specific query with ?field=
    dedication: dict = {}
    word_count: Optional[int] = None
    text_url: Optional[_TextUrl] = None
    deleted: Optional[bool] = None
    hash: Optional[str] = None
    voted: Optional[bool] = None
    has_banned_images: Optional[bool] = None


class Story(msgspec.Struct, rename=story_names):
    id: int
    title: str
    create_date: str  # datetime with tz
    modify_date: str  # datetime with tz
    vote_count: int
    read_count: int
    comment_count: int
    language: _Language
    user: PartialUser
    description: str
    cover: str
    cover_timestamp: str  # datetime with tz
    completed: bool
    categories: list[int] = []
    tags: list[str] = []
    rating: int
    mature: bool
    copyright: int
    url: str
    first_part_id: int
    num_parts: int
    first_published_part: PartialPart
    last_published_part: PartialPart
    parts: list[Part] = []
    deleted: bool

    # Need specific query with ?field=
    tag_rankings: list[_TagRanking] = []
    highlight_colour: str | None = None
    promoted: bool | None = None
    sponsor: list = []
    is_ad_exempt: bool | None = None
    story_text_url: _TextUrl | None = None
    is_paywalled: bool | None = None
    paid_model: str | None = None
    rating_locked: bool | None = None


class Comment(msgspec.Struct, rename=comment_names):
    author: PartialUser
    body: str
    create_date: str  # datetime with tz
    start_position: int
    end_position: int
    id: str
    is_offensive: bool
    is_reply: bool
    num_replies: int
    paragraph_id: str
    parent_id: Optional[str] = None
    part_id: int
    deeplink: str
    legacy_id: int


class ReadingList(msgspec.Struct, rename=reading_list_names):
    id: int
    name: str
    user: PartialUser
    num_stories: int
    cover: str
    sample_covers: list[str] = []

    # Need specific query with ?field=
    promoted: Optional[bool] = None
