#!/bin/dash

print_message() {
	
	if [ $# -lt 1 ]; then
		echo "Usage: $0 message <num>" 
	fi
	
	if [ $# -eq 1 ]; then
		echo "Warning: $1"
	fi

	if [ $# -eq 2 ]; then
		echo "Error: $1"
		exit "$2"
	fi

}

# print_message
print_message "hello"
print_message "error" 42
