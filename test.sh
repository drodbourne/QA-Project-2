#!/bin/bash
declare -a directories=("char_frontend_api" "char_name_api" "char_class_api" "char_attribute_api")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov=application --cov-report=xml --junitxml=junit/test-results.xml
  deactivate
  cd ..
done