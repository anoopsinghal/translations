import json, math, string, random, logging

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, Index

import hashlib

logger = logging.getLogger()

Base = declarative_base()

class Article(Base):
  __tablename__ = 'article'

  # db id
  id = Column(Integer, primary_key=True, nullable=False)

  # translations for all languages are tied together with md5 of english
  md5hash = Column(String(32), nullable=False)

  # language code
  langCode = Column(String(4), nullable = False)

  # actual sentence in the given language
  article = Column(String(2000), nullable = False)

  def __init__(self, id, endMD5, langCode, sentence):
     self.id = id
     self.engMD5 = endMD5
     self.langCode = langCode
     self.sentence = sentence
  # end __init__

  import hashlib

  @staticmethod
  def saveTranslation(session, transjson):
    # get md5hash of the first string to tie both entries together
    md5hash = hashlib.md5(transjson['fromStr'].encode('utf-8')).hexdigest()

    print(md5hash)
    print(transjson)

    fromLang = transjson["fromLang"]
    fromStr = transjson["fromStr"]
    toLang = transjson["toLang"]
    toStr = transjson["toStr"]
    # build json
    articles = [{"md5hash":md5hash, "langCode":transjson['fromLang'], "article":transjson["fromStr"]}
                , {"md5hash":md5hash, "langCode":transjson['toLang'], "article":transjson["toStr"]}
                ]

    # save to db. conflicts will be ignored
    session.bulk_insert_mappings(Article, articles, return_defaults=True, render_nulls=True)
    session.flush()
    session.commit()
  # end saveTranslation
# end class
