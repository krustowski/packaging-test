#!/bin/bash

# service_start.sh
# Sample script run when demo_libuv.service is started
# by Krystof Sara / 5. 7. 2020

function die {
	echo $1
	exit 1
} 

demo_libuv || /usr/bin/demo_libuv || die "demo_libuv binary not installed..."
