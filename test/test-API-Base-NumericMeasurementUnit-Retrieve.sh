#!/usr/bin/env bash


# CoreAPI direct
coreapi get http://localhost:8000/api/base/numeric-measurement-units/1

# CoreAPI via schema
coreapi get http://localhost:8000/api/schema
coreapi action base numeric-measurement-units read --param id=1


# HTTP
http http://localhost:8000/api/base/numeric-measurement-units/1/