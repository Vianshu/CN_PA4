set term postscript eps color
set output 'cwnd.eps'
set ylabel 'cwnd'
set xlabel 'time'
plot './ns-allinone-3.42/ns-3.42/tcp-example.cwnd' using 1:2

