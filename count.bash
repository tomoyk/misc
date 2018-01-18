#!/bin/bash

detex Report_bio/report_bio.tex | gsed '/^$/d' | tr -d '\n' | php -r "echo mb_strlen(trim(fgets(STDIN)));"

echo
