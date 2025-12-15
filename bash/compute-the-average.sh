#https://www.hackerrank.com/challenges/bash-tutorials---compute-the-average/problem?isFullScreen=true

read n
sum=0
for i in $(seq 1 $n); do
  read m
  sum=$((sum + m))
done

result=$(awk "BEGIN {printf \"%.3f\", $sum/$n}")
echo $result
# printf %.3f "$((sum/n))" # doesn't work: bash doesn't support floating point ops