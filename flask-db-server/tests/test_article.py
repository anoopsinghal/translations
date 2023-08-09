import pytest
from orm.article import Article
from .session_fixture import session

class TestArticleORM:
  def testSave(self, session):
    json = {"fromLang":"en", "fromStr":"This is test", "toLang":"de", "toStr":"ein test"}
    Article.saveTranslation(session, json)
  # end testSave
# end TestActivityORM