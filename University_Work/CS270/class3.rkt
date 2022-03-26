;Proofs

; They have three parts
;  They have a start (where we start)
;  An End, where we are trying to get to
;  And the Middle, the stuff we're going to be doing

; Prove that (if (> 6 10) (< 4 5) (> 9 1)) is #t 
;1: (if (> 6 10) (< 4 5) (> 9 1)) <---Premise
;          #f      
;2: (if    #f    (< 4 5) (> 9 1))  Eval >
;3: (> 9 1) Eval if
;4:    #t


; prod
; 5 * 0 = 0
; 5 * 1 = 5 + 0
; 5 * 2 = 5 + 5+ 0
(define (prod x y)
 (if (= y 0)
  0
  (+ x (prod x (- y 1)))
 )
)
; (prod 5 2) evaluates to 10
; 1. (prod 5 2) ; Premise
; 2. (if (= y 0) 0  (+ 5 (prod 5 (- 2 1))  Apply def of prod
; 3. (if #f 0  (+ 5 (prod 5 (- 2 1)) Eval if
; 4. (if #f 0  (+ 5 (prod 5 (- 2 1)) Eval - 
; 5. 
