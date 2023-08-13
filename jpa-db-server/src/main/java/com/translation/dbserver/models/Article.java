package com.translation.dbserver.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Article {

  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  private long id;

  private String md5hash;
  private String langCode;
  private String article;

  public Article(String md5hash, String langCode, String article){
    this.md5hash = md5hash;
    this.langCode = langCode;
    this.article = article;
  }
}