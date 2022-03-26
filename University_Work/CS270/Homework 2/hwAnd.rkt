#lang racket

(define (andi a b)
  (if a
    a
    b
  )
)

(define (andlist L)
  (foldr andi #f L)
)

(andlist '(#f #f #f #f))
(andlist '(#f #t #f #f))


