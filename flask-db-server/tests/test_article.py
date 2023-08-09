import pytest
from orm.article import Article
from .session_fixture import session

class TestArticleORM:
  def testSave(self, session):
    json = {"fromLang":"en", "fromStr":"This is test", "toLang":"de", "toStr":"ein test"}
    Article.saveTranslation(session, json)

    json = {"fromLang": "en", "fromStr": "This is test", "toLang": "fr", "toStr": "mon test"}
    Article.saveTranslation(session, json)

    session.commit()
  # end testSave
# end TestActivityORM