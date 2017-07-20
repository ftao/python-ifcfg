#!/bin/bash

rm -rf coverage_html_report
coverage erase
coverage run `which nosetests` --verbosity=3 $SOURCES
RET=$?

echo; echo
coverage combine
coverage html

coverage report
echo; echo
exit $RET
