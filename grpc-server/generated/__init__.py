# IMPORTANT: DO NOT DELETE!
# Make the generated modules importable in Python.
# This is a solution for an issue with how protobufs deal with relative imports
# More info here: https://github.com/protocolbuffers/protobuf/issues/1491
import os
import sys

sys.path.append(os.path.dirname(__file__))
