[ -z $1 ] && echo "Usage: $0 [URL]" && exit 1
curl -sI $1 | grep -i 'location' | cut -d ' ' -f 2