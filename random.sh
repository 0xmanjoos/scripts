#!/bin/bash
tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 32 | head -n 1
