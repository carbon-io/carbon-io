#!/bin/bash

if ! which pandoc &> /dev/null; then 
    printf '"pandoc" is required to build manpages from markdown source, '\
'please install and rerun\n'
    exit 1
fi

BASEDIR=$(dirname ${BASH_SOURCE[0]})
BASENAME=$(basename ${BASH_SOURCE[0]}) 

function gen_manpages {
    # TODO
    echo "gen_manpages"
}

function usage {
    cat << _END
usage: ${BASENAME} [options]

    options:
        -h, --help  - print this help
_END
    exit ${1-1}
}

for (( i=1; i<$(($#+1)); i++ )); do
    case $(eval echo \$$i) in
        -h|--help)
            usage 0
            ;;
        *)
            ;;
    esac
done

# convert markdown to manpages using pandoc
# TODO

