#lang racket

(define (orList L)
  (if (or #f (first L))
    #t
   (if (empty? (rest L)) #f (orList (rest L)))
  )
)

(orList '(#f #f #f))

(xor #f #t)

