set term postscript eps color
set output 'queue_wait.eps'
set ylabel 'wait'
set xlabel 'time'
plot 'qt.txt' using 1:2

