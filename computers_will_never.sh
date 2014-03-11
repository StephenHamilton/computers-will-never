#!/bin/bash

paste -d " " <(yes Computers will never) <(shuf -r verbs.txt) <(shuf -r processedNouns.txt)
