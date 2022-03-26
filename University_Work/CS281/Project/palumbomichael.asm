.sdata
.align 2

global_ra:

$LC0:
        .ascii  "start fun 1\012\000"
string1:
        .word   $LC0
$LC1:
        .ascii  "start fun 2\012\000"
string2:
        .word   $LC1
$LC2:
        .ascii  "we should never get here\012\000"
stringerr:
        .word   $LC2

.text
.align 2

.text
.globl  main

print_int:
        addiu   $sp,$sp,-24
        sw      $fp,20($sp)
        move    $fp,$sp
        sw      $4,24($fp)
        li      $2,1                        # 0x1
        sw      $2,8($fp)
        lw      $2,8($fp)
        lw      $3,24($fp)
        add $a0,$3,$zero
        add $v0,$2,$zero
        syscall
        lw      $2,24($fp)
        move    $sp,$fp
        lw      $fp,20($sp)
        addiu   $sp,$sp,24
        j       $31
print_str:
        addiu   $sp,$sp,-24
        sw      $fp,20($sp)
        move    $fp,$sp
        sw      $4,24($fp)
        li      $2,4                        # 0x4
        sw      $2,8($fp)
        lw      $2,8($fp)
        lw      $3,24($fp)
        add $a0,$3,$zero
        add $v0,$2,$zero
        syscall
        move    $2,$0
        move    $sp,$fp
        lw      $fp,20($sp)
        addiu   $sp,$sp,24
        j       $31

fun1:
        addiu   $sp,$sp,-32
        sw      $31,28($sp)
        sw      $fp,24($sp)
        move    $fp,$sp
        sw      $4,32($fp)
        lw      $3,28($fp)
        la      $2,global_ra
        sw      $3,0($2)
        la      $2,string1
        lw      $2,0($2)
        move    $4,$2
        jal     print_str
        li      $2,1                        # 0x1
        move    $sp,$fp
        lw      $31,28($sp)
        lw      $fp,24($sp)
        addiu   $sp,$sp,32
        j       $31

fun2:
        addiu   $sp,$sp,-32
        sw      $31,28($sp)
        sw      $fp,24($sp)
        move    $fp,$sp
        sw      $4,32($fp)
        addiu   $2,$fp,28
        la      $3,global_ra
        lw      $3,0($3)
        sw      $3,0($2)
        la      $2,string2
        lw      $2,0($2)
        move    $4,$2
        jal     print_str
        li      $2,2                        # 0x2
        move    $sp,$fp
        lw      $31,28($sp)
        lw      $fp,24($sp)
        addiu   $sp,$sp,32
        j       $31

main:
        addiu   $sp,$sp,-40
        sw      $31,36($sp)
        sw      $fp,32($sp)
        move    $fp,$sp
        sw      $4,40($fp)
        sw      $5,44($fp)
        li      $4,10                 # 0xa
        jal     fun1
        sw      $2,24($fp)
        lw      $4,24($fp)
        jal     print_int
        lw      $3,24($fp)
        li      $2,2                        # 0x2
        bne     $3,$2,$L10
        li      $2,2                        # 0x2
        b       $L11
$L10:
        li      $4,10                 # 0xa
        jal     fun2
        sw      $2,24($fp)
        la      $2,stringerr
        lw      $2,0($2)
        move    $4,$2
        jal     print_str
        li      $2,1                        # 0x1
$L11:
        move    $sp,$fp
        lw      $31,36($sp)
        lw      $fp,32($sp)
        addiu   $sp,$sp,40
        j       $31