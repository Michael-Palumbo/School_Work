#lang racket

; (define (sqr x) (* x x))
(define sqr (lambda (x) (* x x)))
(lambda (x) (* x x))

(sqr 4)
((lambda (x) (* x x)) 4)
; (x y)

(define (applyTwice f x)
  (f (f x))
)


(applyTwice (lambda (a) (- a 5)) 7) ; -3

; Higher Order Functions

(define (multBy x)
  (lambda (y) (* x y))
)

( (multBy 3) 5)
(define multByThree (multBy 3))
(multByThree 5)

;;;; MAP ;;;;
; (map f L)
(map (lambda (x) (+ x 1)) '(1 2 3))
(list (+ 1 1) (+ 2 2) (+ 3 1)) ; equivalent to
(map (multBy 3) '(7 5 6))

;;;; FOLDL, FOLDR ;;;;
; (foldr f init L)
(foldr + 0 '( 1 2 3))
; (+ 1 (+ 2 (+ 3 0)))

(foldl + 0 '(1 2 3))
; (+ 3 (+ 2 (+ 1 0)))

;;;;;;;;;;;;;;;;;;;;;;;;;;

(map (lambda (x) (* x 2)) '(0 1 2 3 4))
(foldr + 0 (map (lambda (x) (* x 2)) '(0 1 2 3 4)))

(define (add1 L)
  (if (null? L)
    '()
    (cons (+ 1 (first L)) (ad 1 (rest L)))
  )
)

(add1 '(1 2 3))
