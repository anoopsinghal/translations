/** @format */

const express = require("express");

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/", (request, response) => {
  response.json({ message: "Hey! This is your server response!" });
});

const crypto = require("crypto");

const sqlite3 = require("sqlite3");

// Connecting Database
let db = new sqlite3.Database(":memory:", (err) => {
  if (err) {
    console.log("Error Occurred - " + err.message);
  } else {
    console.log("DataBase Connected");

    var createQuery =
      "CREATE TABLE Article ( id INTEGER PRIMARY KEY, md5hash varchar(32) NOT NULL, langCode varchar(4) NOT NULL, article varchar(2000) NOT NULL, UNIQUE(md5hash, langCode) ON CONFLICT REPLACE);";
    console.log(createQuery);

    db.run(createQuery, (err) => {
      if (err) {
        console.log("Error Occurred - " + err.message);
        return;
      } else {
        console.log("created table");
      }
    });
  }
});

class ArticleDAO {
  // omitting constructor code
  constructor(db) {
    this.db = db;
  }
  run(sql, params = []) {
    this.db.run(sql, params, function (err) {
      if (err) {
        console.log("Error running sql " + sql);
        console.log(err);
      } else {
        console.log("created article");
      }
    });
  }
}

app.post("/save-translation", (request, response) => {
  console.log("routes");
  console.log("request.body : " + request.body);
  var fromLang = request.body.fromLang;
  var fromStr = request.body.fromStr;
  var toLang = request.body.toLang;
  var toStr = request.body.toStr;

  let md5hash = crypto.createHash("md5").update(fromStr).digest("hex");

  var dao = new ArticleDAO(db);
  dao.run(
    `INSERT INTO Article (md5hash, langCode, article)
      VALUES (?, ?, ?)`,
    [md5hash, fromLang, fromStr]
  );

  dao.run(
    `INSERT INTO Article (md5hash, langCode, article)
      VALUES (?, ?, ?)`,
    [md5hash, toLang, toStr]
  );

  response.status(200).end();
});

module.exports = app;
