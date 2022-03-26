#lang racket

;  ;z ; zero
; '(D x) ; represents doubling the double-notation number x
; '(DP1 x) ; represents doubling and adding 1 to x

; y = 2x    ; y must be an even number
; z = 2x+ 1 ; z must be an odd number

(define b_zero 'z) ; 0
(define b_one '(DP1 z)) ; 2(0)+1 = 1
(define b_two '(D (DP1 z))) ; 2( 2(0) + 1) = 2
(define b_three '(DP1 (DP1 z))) ; 2( 2(0) + 1) + 1 = 3


(define (inc N)
  (cond
    [(equal? N 'z) '(DP1 z)] 
    [(equal? (first N) 'D) (list 'DP1 (second N))]
    [(equal? (first N) 'DP1) (list 'D (inc (second N)))]
  )
)


; x + 0 = x
; 0 + y = y
; 2x+ 2y = 2(x + y)

;input contract: 2 double-notation numbers
;output contract: 1 double-notation numebr
(define (binadd A B)
  (cond
    [(equal? A 'z) B]
    [(equal? B 'z) A]
    [(and (equal? (first A) 'D) (equal? (first B) 'D))
     (list 'D (ibinadd (seond A) (second B)))]
  )
)

;Peano arithmetic
; 400 + 200 - 401 + 199 -> 402 + 198 -> ...
;Double-notaion arithmetic
; 400 + 200 ops -> 200 + 100 ops -> 100 + 50 ops -> ...
