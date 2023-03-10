#!/bin/bash

text=$(xsel -o)

python /Users/damonpickett/ai-development/dbug/dbug.py "$text"