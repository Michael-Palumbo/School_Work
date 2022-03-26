#lang racket

;Stair case problem

(define (puzzle n)
 (if (<= n 0) 1
  (+ (if (< (- n 2) 0) 0 (puzzle (- n 2))) (if (< (- n 1) 0) 0 (puzzle (- n 1))))
 )
)

(puzzle 1) ; 1
(puzzle 2) ; 2
(puzzle 3) ; 3
(puzzle 4) ; 5
(puzzle 5) ; 8
(puzzle 6) ; 13
(puzzle 7)
(puzzle 8)
(puzzle 9)
(puzzle 10)


(define (help_prime n i)
 (if (> (* i i) n) #t
  (if (= (remainder n i) 0) #f
   (help_prime n (+ i 1))
  )
 )
)
(define (is_prime n)
  (if (<= n 1) #f
   (help_prime n 2)
  )
)

(display "1 - ")
(is_prime 1)
(display "2 - ")
(is_prime 2)
(display "4 - ")
(is_prime 4)
(display "16 - ")
(is_prime 16)
(display "19 - ")
(is_prime 19)
(display "20 - ")
(is_prime 20)

(define (sum_digits n)
 (if (= (quotient n 10) 0) n
  (+ (remainder n 10) (sum_digits (quotient n 10)))
 )
)

(sum_digits 123)
(sum_digits 456)
