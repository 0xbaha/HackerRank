#!/bin/bash

read line
if [ ${#line} -ge 20 ]; then
    # printing first 20 characters now since line is long enough
    echo "$line" | head -c20
else
    echo "$line"
    char_count=${#line}
    char_count=`expr $char_count + 1`
    # increasing char_count since line ends with one character that ${#line} doesn't count
    while((char_count<20))
    do
        read line
        need_count=$((20-char_count))
        if [ ${#line} -gt $need_count ]; then
            echo "$line" | head -c$need_count
            char_count=`expr $char_count + $need_count`
        else
            echo "$line"
            char_count=`expr $char_count + ${#line}`
            char_count=`expr $char_count + 1`
        fi
    done
fi