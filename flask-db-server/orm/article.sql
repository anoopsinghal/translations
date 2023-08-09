CREATE TABLE IF NOT EXISTS article (
	id INTEGER PRIMARY KEY,
   	md5hash varchar(32) NOT NULL,
	langCode varchar(4) NOT NULL,
	article varchar(2000) NOT NULL,
	UNIQUE(md5hash, langCode) ON CONFLICT IGNORE
);