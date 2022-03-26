#lang racket
'()
; cons
; (cons value list)
(cons 3 '())
(cons 2 (cons 3 '()))
(cons 1 (cons 2 (cons 3 '())))

; side note
(cons 3 1) ; creates a pair (second value should a reference to a list)

(list 1 2 3)

; null? asks whether the list is empty
(null? '()) ; #t
(null? '(1)) ; #f
(null? 4) ; #f not a list
(null? `(())) ; #f list contains a list

; cons? asks whether the list has something in it
(cons? `(1)) ; #t
(cons? '()) ; #f
(cons? '(3)) ; #f not a list
(cons? '(())) ; #t list contains a list

(define L '( 1 2 3 4 5))

; *first* returns the first value in a list
(first L) ; 1

; *rest* returns the remaining list without the first element
(rest L) ; '(2 3 4 5)
(first (rest (rest L)))

(rest '(1)) ; returns empty list

; (rest '()) ; returns error

; Nested Lists

'((1))
(cons (cons 1 '()) '())

'( (1) ((2)) )
(cons
 (cons 1 '())
 (cons (cons 2 '()) '())
)

L ; unchanged

(define (size L)
 (if (null? L) 0
  (+ 1 (size (rest L )))))
(size L) ; 5
(size '()) ; 0
