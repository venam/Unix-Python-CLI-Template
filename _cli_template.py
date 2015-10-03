#compdef cli_template

_arguments \
  '(-v -i test)-h[Print help message]' \
  '(test -h -i)-v[prints version]' \
  '(test -v -h)-i[Goes into interactive mode]' \
  '(-i -h -v)test[test]:emotion:(chose between those)'
