#!/bin/bash

say -v '?' | while read line;
    do
        voice=$(echo $line | awk '{print $1}');
        phrase=$(echo $line | awk '{split($0,a,"#"); print a[2]}');
        echo "($voice) $phrase";
        say -v $voice "$voice: $phrase";
    done
