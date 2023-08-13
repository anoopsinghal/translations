package com.translation.dbserver.controllers;

import java.net.URI;
import java.security.MessageDigest;
import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.DigestUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.translation.dbserver.models.Article;
import com.translation.dbserver.models.ArticleRepository;
import com.translation.dbserver.pojos.TranslationPojo;

@RestController
public class ArticleController {
  @Autowired
  ArticleRepository articleRepo;

	@GetMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
	}

	@PostMapping("/saveTranslation")
	public ResponseEntity<TranslationPojo> saveTranslation(@RequestBody TranslationPojo translation) {
    String md5Hash = DigestUtils.md5DigestAsHex(translation.fromStr.getBytes()).toUpperCase();
    
    articleRepo.saveAll(Arrays.asList(new Article(md5Hash, translation.fromLang, translation.fromStr),
    new Article(md5Hash, translation.toLang, translation.toStr)));

    HttpHeaders headers = new HttpHeaders();         
    return new ResponseEntity<>(translation,headers,HttpStatus.CREATED);        
  }
}

