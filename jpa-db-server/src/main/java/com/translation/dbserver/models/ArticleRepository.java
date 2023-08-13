package com.translation.dbserver.models;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.repository.CrudRepository;

public interface ArticleRepository extends PagingAndSortingRepository<Article, Long>, CrudRepository<Article,Long> {
}
