#!/bin/bash


declare -a done_opt
declare -a done_spc
declare -a fuckup
declare -a interupted

for output in *.log; do
   #echo $output
    if grep -q "Normal termination" $output; then
        if grep -q "Frequ" $output; then
            done_opt+=($output)
        else 
            done_spc+=($output)
        fi

    elif grep -q "Error termination" $output; then
        fuckup+=($output)
    
    elif grep -q "Erroneous write" $output; then
        fuckup+=($output)

    else
        interupted+=($output)
    fi
done


echo NORMALLY TERMINATED
echo ------------------------
echo "opt/freq jobs"
echo "Freq: showing 3 lowest modes"
for output in ${done_opt[@]}; do
    token="$(grep -m 1 Frequencies $output)"
    echo $output:  $token
done
echo ------------------------
echo SPC jobs
for output in ${done_spc[@]}; do
    token="$(grep "SCF Done" $output)"
    echo $output:  ${token::-18}
done
echo ------------------------
echo ------------------------

echo ERROR TERMINATION
for output in ${fuckup[@]}; do
    echo $output
done

echo ------------------------
echo ------------------------

echo INTERUPTED
for output in ${interupted[@]}; do
    echo $output
done
