#lang racket

(define (sum1 n)
 (if (<= n 1) 1
  (+ (* n n) (sum1 (- n 1)))
 )
)

(sum1 1)
(sum1 2)
(sum1 3)
(sum1 4)
(sum1 6)
(sum1 7)
(sum1 8)

(define (sum2 n)
 (if (<= n 1) 1
  (+ (- (* 2 n) 1) (sum2 (- n 1)))
 )
)

(sum2 1)
(sum2 2)
(sum2 3)
(sum2 4)
(sum2 5)
(sum2 6)
(sum2 7)
(sum2 8)
(sum2 9)

(define (sum3 n)
 (if (<= n 0) 0
  (+ (* n (* n (expt -1 n))) (sum3 (- n 1)))
 )
)

(sum3 1)
(sum3 2)
(sum3 3)
(sum3 4)
(sum3 5)
(sum3 6)
(sum3 7)

(define (sum4 n)
 (if (<= n 0) 0
  (+ (* n (+ n 1)) (sum4 (- n 1)))
 )
)

(sum4 1)
(sum4 2)
(sum4 3)
(sum4 4)
(sum4 5)
(sum4 6)
(sum4 7)
(sum4 8)

(display "Question 5\n")

(define (sum5 n)
 (if (<= n 0) 0
  (+ (- (* n 8) 5) (sum5 (- n 1)))
 )
)

(sum5 1)
(sum5 2)
(sum5 3)
(sum5 4)
(sum5 5)
(sum5 7)
(sum5 8)
(sum5 9)
